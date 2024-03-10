from db.postgres import initiate_db
import json
import string
from typing import Union
from fastapi import FastAPI, File, HTTPException, Response, UploadFile
import uvicorn
from api.rabbitmq import send
from api.s3 import download_file, upload_file
from db.postgres import *
import uuid

initiate_db()
app = FastAPI(title= "service 1")


@app.post("/submit_email/")
async def submit_email(email: str, file: UploadFile = File(...)):
    # insert to db
    query = request_table.insert().values(email=email)

    await database.execute(query=query)
    id_new = uuid.uuid4()
    address = str(id_new) + "." + file.filename.split(".")[-1]
    # save file on s3
    upload_file(file, address)
    
    return f"Your submission was registered with ID: {id_new}"


# curl -X GET "http://localhost:8000/check_email/?id=5"
@app.get("/check_email/")
async def check_email(id: int):
    query = request_table.select().where(request_table.c.id == id)
    result = await database.fetch_one(query=query)
    if not result:
        raise HTTPException(status_code=404, detail="Email not found")
    elif result["enable"] == 0:
        send(id)
    else:
        raise HTTPException(status_code=400, detail="You cannot request this code")

    return {"result": 'Sending to job_table..'}


if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)