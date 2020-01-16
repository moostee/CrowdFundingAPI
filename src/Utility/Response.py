from rest_framework.response import Response as response

class Response:
    ''' A Response class wrapper for all HTTP responses'''
    
    @staticmethod
    def success(message='success', data=None, responseCode='00',  headers=None, content_type='application/json'):
        """Returns a success HTTP response"""
        responseData = {
            "message": message,
            "responseCode": responseCode,
            "data": data,
        }
        return response(data=responseData, headers=headers, content_type=content_type)

    @staticmethod
    def error(message='Error occured while processing your request', error=None, responseCode='99', headers=None, content_type='application/json'):
        """Returns a failure HTTP response"""
        responseData = {
            "message": message,
            "responseCode": responseCode,
            "error": error
        }
        return response(data=responseData, headers=headers, content_type=content_type)
