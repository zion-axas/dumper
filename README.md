## PG Dumper: dump pg docker db and load to s3

### Create folder and clone dumper repo:

`mkdir /root/dumper && cd /root/dumper`  
`git clone https://<repo-url>`

### Create and activate python venv:

`python -m venv venv && source venv/bin/activate`

### Install requirements:

`pip install -r requirements.txt`

### Deactivate venv:

`deactivate`

### Create .env settings file:

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

! don't forget to name your pg db container in docker-compose.yml:

```
services:
  db:
    container_name: dbstore
    image: postgres:12
```

### Add execute permision:

`chmod +x dumper.sh`

### Set crontab service:

`crontab -e` - open crontab settings  
`0 4 * * * cd /root/dumper && ./dumper.sh >> /var/log/cron_dumper.log 2>&1` - add line  
set time ^^^ and workdir ^^^^

## Its done!

### To dump manually:

`./dumper.sh`

### To remove file from s3:

`chmod +x remover.sh`  
`./remover.sh https://<file_url>`

### To read logs:

`cat /var/log/cron_dumper.log`
