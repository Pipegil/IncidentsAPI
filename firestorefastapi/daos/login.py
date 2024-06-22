from google.cloud import firestore
from google.cloud.firestore_v1 import FieldFilter


class LoginDAO:
    def __init__(self):
        self.collection = firestore.client().collection('users')

    def verify(self, email: str, password: str):
        query = self.collection.where(filter=FieldFilter('email', '==', email)).where(
            filter=FieldFilter('password', '==', password)).limit(1)
        docs = query.stream()
        for doc in docs:
            return doc.to_dict()
        return None
