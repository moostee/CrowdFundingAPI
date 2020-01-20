class Response:
    ''' A Response class wrapper for all HTTP responses'''
    
    @staticmethod
    def success(message='success', data=None, responseCode='00'):
        """Returns a success HTTP response"""
        return {
            "message": message,
            "responseCode": responseCode,
            "data": data,
        }

    @staticmethod
    def error(message='Error occured while processing your request', error=None, responseCode='99'):
        """Returns a failure HTTP response"""
        return {
            "message": message,
            "responseCode": responseCode,
            "error": error
        }
    
    @staticmethod
    def successfulResponse(requestId, data=None, message = "success"):
        return {
            "requestId" : requestId,
            "responseCode" : "00",
            "responseMessage" : message,
            "data" : data
        }

    @staticmethod
    def unSuccessfulResponse(requestId,message="Unsuccessful"):
        return {
            "requestId" : requestId,
            "responseCode" : "02",
            "responseMessage" : message
        }
    
    @staticmethod
    def ExceptionResponse(requestId):
        return {
            "requestId" : requestId,
            "responseCode" : "99",
            "responseMessage" : "An Error occured while processing your request. Please try again later."
        }