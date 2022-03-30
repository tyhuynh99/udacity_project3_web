import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="postgre300.postgres.database.azure.com"
    POSTGRES_USER="tyhuynh@postgre300"
    POSTGRES_PW="P@ssw0rd1234"
    POSTGRES_DB="techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://servbus300.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=5FTpAO5hJ2L7mOKqu4pP9qkOEK47Bjp4je9Pind1KAo='
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'tyhuynh1199@gmail.com'
    SENDGRID_API_KEY = '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'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False