import jwt
import os
import environ
from datetime import datetime,timedelta

env = environ.Env()
environ.Env.read_env()

class Jwt:

    @staticmethod
    def EncodeJWT(payload, secret, algorithm='HS256'):       
        if env('expiryInSeconds') is not None :
            secondItExpiries = int(env('expiryInSeconds'))
            setattr(payload, 'exp', datetime.utcnow() + timedelta.seconds(seconds=secondItExpiries))

        return jwt.encode(payload, secret, algorithm=theAlgorithm)

    @staticmethod
    def DecodeJWT(encodedJWT,algorithms=['HS256']):
        return jwt.decode(payload, secret, algorithm=theAlgorithm)
