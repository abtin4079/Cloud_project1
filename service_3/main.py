import json
import sys
sys.path.append('F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1')



import string
from typing import Union
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, HTTPException, Response, UploadFile
from sqlalchemy.sql import select, update
import uvicorn
from service_1.src.api.rabbitmq_publisher import send
from service_2.api.rabbitMQ_consumer import *
from service_3.api.mailgun import send_simple_message
from service_3.api.track_recommender import recommender
from sqlalchemy.exc import SQLAlchemyError
from service_2.api.shazam import * 
from service_3.api.search import *
from service_1.src.api.s3 import download_file, upload_file
from service_1.src.db.postgres import *
import uuid




app = FastAPI(title= "service 3")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def up():
    return f"welcome to service three"



@app.get('/new_songs_for_you')
async def new_songs_for_you():

    try:
        # Filter for rows where the state is 'ready'
       # stmt = select([
       #     request_table.c.id,
        #    request_table.c.email,
        #   request_table.c.state,
        #   request_table.c.songid 
        #])
        #select_statement = stmt.where(request_table.c.state == "ready")
        #print(select_statement)
        print(600)
        with engine.connect() as conn:
            query = request_table.select().where(request_table.c.state == "ready")
            print(query)
            print(601)
            result = conn.execute(query)
            print(602)
            for row in result:
                songid = row[3]
                print(songid)
                email = row[1]
                responseData = recommender(songid)
                #print(responseData)
                send_simple_message(responseData, email)
                print(send_simple_message(responseData, email))

                # Define the update statement
                update_statement_service_3 = (
                    update(request_table)
                    .where(request_table.c.songid == songid)  # Specify the condition
                    .values(state="done", email="abtin.aptitude@gmail.com")  # Set the new values for the columns
                )
                await database.execute(update_statement_service_3)

        return {"message": "Success"}
    except SQLAlchemyError as e:
        # Handle the SQLAlchemy error
        print(f"SQLAlchemyError occurred: {e}")
        return {"error": str(e)}
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
        return {"error": str(e)}








if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=5000, reload=True)