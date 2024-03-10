import sqlalchemy
import databases
import json

DATABASE_URL = "postgresql://abtin.aptitude:14eLKlAsRVud@ep-winter-scene-a2tueh36.eu-central-1.aws.neon.tech/neondb?sslmode=require"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

request_table = sqlalchemy.Table(
    "request",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("state", sqlalchemy.String),
    sqlalchemy.Column("songid", sqlalchemy.String),
)

# job_table = sqlalchemy.Table(
#     "job",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
#     sqlalchemy.Column("upload", sqlalchemy.Integer, sqlalchemy.ForeignKey("uploads.id")),
#     sqlalchemy.Column("job", sqlalchemy.String),
#     sqlalchemy.Column("status", sqlalchemy.String, default="none-executed")
# )

# results_table = sqlalchemy.Table(
#     "results",
#     metadata,
#     sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
#     sqlalchemy.Column("upload", sqlalchemy.Integer, sqlalchemy.ForeignKey("uploads.id")),
#     sqlalchemy.Column("output", sqlalchemy.String, default="none"),
#     sqlalchemy.Column("execute_date", sqlalchemy.String, default="none"),
#     sqlalchemy.Column("filelink", sqlalchemy.String, default="none")
# )

def initiate_db():
    metadata.create_all(engine)


# def get_data_from_results_table(id):
#     try:
#         with engine.connect() as conn:
#             query = results_table.select().where(results_table.c.upload == id)
#             result = conn.execute(query)
#             data = result.fetchone()
#             if data:
#                 print(f"INFO: Got data from DB for {id}")
#                 return json.dumps(dict(data))
#             else:
#                 print(f"INFO: No data found in DB for {id}")
#                 return None
#     except Exception as e:
#         print(f"ERROR: Failed to get data from DB for {id}")
#         print(f"Error message: {e}")
#         return None


# def get_data_from_job_table(id):
#     try:
#         with engine.connect() as conn:
#             query = job_table.select().where(job_table.c.upload == id)
#             result = conn.execute(query)
#             data = result.fetchone()
#             if data:
#                 print(f"INFO: Got data from DB for {id}")
#                 return json.dumps(dict(data))
#             else:
#                 print(f"INFO: No data found in DB for {id}")
#                 return None
#     except Exception as e:
#         print(f"ERROR: Failed to get data from DB for {id}")
#         print(f"Error message: {e}")
#         return None


# async def get_requests_by_email(email):
#     try:
#         async with database:
#             query = request_table.select().where(request_table.c.email == email)
#             results = await database.fetch_all(query)
#             return [json.dumps(dict(row)) for row in results]
#     except Exception as e:
#         print(f"ERROR: Failed to get data from DB")
#         print(f"Error message: {e}")
