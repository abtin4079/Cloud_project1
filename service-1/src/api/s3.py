import sys
import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

domain = 'https://s3.ir-thr-at1.arvanstorage.ir'
bucketName = 'objectivecloud'
accessKey = '5b16d526-1447-4354-9458-d5ebb8b394a1'
secretKey = 'b7827d14f9b68499a361f81e8d04c83541cdecf37e5bc8ccb76750b668df9ab1'


try: 
    s3_resource = boto3.resource(
        's3',
        endpoint_url=domain,
        aws_access_key_id=accessKey,
        aws_secret_access_key=secretKey
    )
except Exception as exc:
    logging.info(exc)
else:

    bucket = s3_resource.Bucket(bucketName)


def list_files():
    for obj in bucket.objects.all():
        logging.info(f"object_name: {obj.key}, last_modified: {obj.last_modified}")


def upload_file(file, object_name):
    # contents = file.file.read()
    try:
        print(f"inja{bucket}")
        bucket.put_object(
            ACL='private',
            Body=file,
            Key=object_name
        )
        print(f'INFO:     File-{object_name} uploaded successfully')
    except Exception as exc:
        logging.info(exc)
    

def get_url(filename):
    filename = str(filename).split("'")[1]
    url = f"{domain}/{bucketName}/{filename}"
    return url


def download_file(object_name, download_path):
    bucket.download_file(
        object_name,
        download_path
    )


def delete_file(object_name):
    object_name = 'parspack.png'
    object = bucket.Object(object_name)
    object.delete()

if __name__ == "__main__":
    attachment = open("F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1/13_-_him_i_-_g-eazy_halsey_320.mp3", 'rb')
    upload_file(file= attachment, object_name='I_Him')