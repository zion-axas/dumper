import logging
import os

from dotenv import load_dotenv

load_dotenv(override=True)

S3_SERVICE_NAME = os.getenv("S3_SERVICE_NAME")
S3_ENDPOINTS_URL = os.getenv("S3_ENDPOINTS_URL")
S3_ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

level = logging.INFO

logging.basicConfig(
    level=level,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s] %(levelname)s %(module)s:%(lineno)d:%(funcName)s() - %(message)s",
)
