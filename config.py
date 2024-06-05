from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_NAME = os.environ.get('DB_NAME')

# url = 'postgresql+psycopg2://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s'

RABBITMQ_HOST_P = os.environ.get('RABBITMQ_HOST_P')
RABBITMQ_USER_P = os.environ.get('RABBITMQ_USER_P')
RABBITMQ_PASS_P = os.environ.get('RABBITMQ_PASS_P')
RABBITMQ_PORT_P = os.environ.get('RABBITMQ_PORT_P')

BROKER_URL = os.environ.get('BROKER_URL')
