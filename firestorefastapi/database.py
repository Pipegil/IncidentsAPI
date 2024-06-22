import os
from google.cloud import firestore

dir_path = os.path.dirname(os.path.abspath(__file__))
service_account_path = os.path.join(dir_path, 'service_account.json')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path
db = firestore.Client()