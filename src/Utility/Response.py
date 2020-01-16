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
