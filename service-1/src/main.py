import json
import string
from typing import Union
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, HTTPException, Response, UploadFile
import uvicorn
from api.rabbitmq import send
from api.s3 import download_file, upload_file
from db.postgres import *
import uuid



app = FastAPI(title= "service 1")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def up():
    return f"Hey!"


@app.post("/submit_email/")
async def submit_email(email: str, file: UploadFile = File(...)):
    try:
        # insert to db
        id_new = uuid.uuid4()
        address = str(id_new) + "." + file.filename.split(".")[-1]
        
        # Save email and file address to the database
        query = request_table.insert().values(email=email, state="pending")
        await database.execute(query=query)
        
        # Save file on S3
        upload_file(file.file, address)
        
        return f"Your submission was registered with ID: {id_new}"
    
    except Exception as e:
        query = request_table.insert().values(email=email, state="failure")
        await database.execute(query=query)
        # Handle other unexpected errors by returning a generic error response
        return JSONResponse(status_code=500, content={"message": "Internal server error", "details": str(e)})





# curl -X GET "http://localhost:8000/check_email/?id=5"
@app.get("/check_email/")
async def check_email(id: str):
    query = request_table.select().where(request_table.c.id == id)
    result = await database.fetch_one(query=query)
    if not result:
        raise HTTPException(status_code=404, detail="Email not found")
    elif result["state"] == "pending":
        send(id)
    else:
        raise HTTPException(status_code=400, detail="You cannot request this code")

    return {"result": 'Sending to job_table..'}


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)