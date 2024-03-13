import json
import sys
sys.path.append('F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1')



import string
from typing import Union
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, HTTPException, Response, UploadFile
from sqlalchemy import update
import uvicorn
from service_1.src.api.rabbitmq_publisher import send
from service_2.api.rabbitMQ_consumer import *

from service_2.api.shazam import *  # Adjust import statement
from service_3.api.search import *
from service_1.src.api.s3 import download_file, upload_file
from service_1.src.db.postgres import *
import uuid




app = FastAPI(title= "service 2")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def up():
    return f"welcome to service two"








#################################################################### SERVICE 2
from fastapi import HTTPException

@app.get('/send_to_shazam')
async def send_to_shazam():
    try:
        # Receive the address from RabbitMQ
        receiveFromRabbitMQ()
        print(100)
        # Receive the address ID from RabbitMQ
        address_received = get_address()
        print(f"INFO:     Received 12 {address_received} from RabbitMQ")
    


        # Download an S3 file to the laptop
        download_file(str(address_received), "F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1/service_2/track/track2.mp3")
        attachment = open("F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1/service_2/track/track2.mp3", 'rb')
        print(102)
        # Send to Shazam API
        songid_with_shazam = shazamApi(attachment)
        songid = searchMusic(songid_with_shazam)
        print(103)
        # Define the update statement
        update_statement_service_2 = (
            update(request_table)
            .where(request_table.c.songid == address_received)  # Specify the condition
            .values(songid=songid, state="ready")  # Set the new values for the columns
        )
        await database.execute(update_statement_service_2)

        return {"message": "Success"}
    
    except Exception as e:
        # Handle specific exceptions or generic errors
        if isinstance(e, HTTPException):
            # Handle FastAPI HTTP exceptions
            return {"message": f"HTTP Exception: {e.detail}"}
        else:
            # Handle other exceptions
            return {"message": f"Error: {str(e)}"}






if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=7000, reload=True)