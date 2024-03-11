import sqlalchemy
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException
import databases

DATABASE_URL = "postgresql://abtin.aptitude:14eLKlAsRVud@ep-winter-scene-a2tueh36.eu-central-1.aws.neon.tech/neondb?sslmode=require"

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

# Create a database connection pool
database = databases.Database(DATABASE_URL)

metadata.create_all(engine)




