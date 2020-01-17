import jwt

class Jwt:

    @staticmethod
    def EncodeJWT(payload, secret, theAlgorithm='HS256'):  
        return jwt.encode(payload, secret, algorithm=theAlgorithm)

    @staticmethod
    def DecodeJWT(encodedJWT, secret, theAlgorithm=['HS256']):
        return jwt.decode(encodedJWT, secret, algorithm=theAlgorithm)