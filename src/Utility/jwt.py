import jwt
import os
import environ
from datetime import datetime,timedelta

env = environ.Env()
environ.Env.read_env()

class Jwt:

    @staticmethod
    def EncodeJWT(payload, secret, theAlgorithm='HS256'):       
        if env('expiryInSeconds') is not None :
            secondItExpires = int(env('expiryInSeconds'))
            setattr(payload, 'exp', datetime.utcnow() + timedelta.seconds(seconds=secondItExpiries))

        return jwt.encode(payload, secret, algorithm=theAlgorithm)

    @staticmethod
    def DecodeJWT(encodedJWT,theAlgorithm=['HS256']):
        return jwt.decode(encodedJWT, secret, algorithm=theAlgorithm)
