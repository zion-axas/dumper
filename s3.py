import logging
import os

import boto3
from botocore.exceptions import ClientError

import settings


def get_s3_client():
    s3 = boto3.client(
        service_name=settings.S3_SERVICE_NAME,
        endpoint_url=settings.S3_ENDPOINTS_URL,
        aws_access_key_id=settings.S3_ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3_SECRET_ACCESS_KEY,
    )
    return s3


def get_s3():
    "объект позволяет загружать и удалять файлы на s3"
    return S3(client=get_s3_client(), bucket=settings.S3_BUCKET_NAME)


class S3:
    def __init__(self, client=None, bucket=None):
        self.client = client
        self.bucket: str | None = bucket

    def load(self, *, filename, prefix: str = "") -> str:
        """load file to s3 and return url
        example: prefix="db/dump/" """
        url_prefix = self.client._endpoint.host + "/" + self.bucket + "/"
        name = prefix + os.path.basename(filename)
        new_url = url_prefix + name  # host + bucket + prefix + file_basename
        try:
            self.client.upload_file(Filename=filename, Bucket=self.bucket, Key=name)
        except ClientError as e:
            logging.error(e)
            return "Fail"
        return new_url

    def remove(self, *, url: str = None) -> None:
        if url:
            key = url.split(self.bucket)[1][1:]
            try:
                self.client.delete_object(Bucket=self.bucket, Key=key)
            except ClientError as e:
                logging.error(e)
                return "Fail"
