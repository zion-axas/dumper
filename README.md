## PG Dumper: dump pg docker db and load to s3

### Create venv:

`python -m venv venv`

### Activate venv:

`source venv/bin/activate`

### Install requirements:

`pip install -r requirements.txt`

### Deactivate venv:

`deactivate`

### Set .env settings file:

```
# pg
CONTAINER_NAME=mycontainer
POSTGRES_USER=postgres

# s3
S3_SERVICE_NAME=s3
S3_ENDPOINTS_URL=https://storage.yandexcloud.net

S3_ACCESS_KEY_ID=YCAJEqdWXmQpZaD**********
S3_SECRET_ACCESS_KEY=YCOgpRPar5ylfFZ7zZ8iUzRiiq2jZl**********

S3_BUCKET_NAME=myapp
```

### Add execute permision:

`chmod +x dumper.sh`

### Set crontab service:

`crontab -e`  
`0 4 * * * /root/dumper/dumper.sh >> /var/log/cron_dumper.log 2>&1`

### To dump manually:

`./dumper.sh`

### To remove file from s3:

`chmod +x remover.sh`  
`./remover.sh https://file_url`
