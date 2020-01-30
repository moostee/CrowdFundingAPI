import jwt
from datetime import datetime, timedelta
from .Response import Response as ResponseWrapper
from rest_framework.response import Response


class Jwt:

    @staticmethod
    def EncodeJWT(payload, secret, theAlgorithm='HS256'):
        payload['exp'] = datetime.now() + timedelta(days=2)
        return jwt.encode(payload, secret, algorithm=theAlgorithm)

    @staticmethod
    def DecodeJWT(encodedJWT, secret, theAlgorithm=['HS256']):
        return jwt.decode(encodedJWT, secret, algorithm=theAlgorithm, leeway=datetime.timedelta(hours=2))
