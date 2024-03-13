import sys
import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

domain = 'https://s3.ir-thr-at1.arvanstorage.ir'
bucketName = 'objectivecloud'
accessKey = '5b16d526-1447-4354-9458-d5ebb8b394a1'
secretKey = 'b7827d14f9b68499a361f81e8d04c83541cdecf37e5bc8ccb76750b668df9ab1'

bucketName1 = 'abtinz'
accessKey1 = '5b16d526-1447-4354-9458-d5ebb8b394a1'
secretKey1 = 'b7827d14f9b68499a361f81e8d04c83541cdecf37e5bc8ccb76750b668df9ab1'

domain_liara = "https://abtinz.storage.iran.liara.space"
accessKey_liara = "1ks3r33umkocll19"
secretKey_liara = "49ecb253-d666-4bf2-b6d6-12f0e84065e6"


try: 
    s3_resource = boto3.resource(
        's3',
        endpoint_url=domain,
        aws_access_key_id=accessKey1,
        aws_secret_access_key=secretKey1
    )
except Exception as exc:
    logging.info(exc)
else:

    bucket = s3_resource.Bucket(bucketName1)


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
    url = f"{domain}/{bucketName1}/{filename}"
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
    download_file('aida_file', "F:/UNIVERCITY/term8/cloud computing/homework/HW1/9923020_HW1/service_2/track/track.mp3")