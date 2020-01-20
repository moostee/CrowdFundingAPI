import requests as request

class Request:
    '''An API Request class wrapper for all HTTP requests'''

    @staticmethod
    def post(url, data, params=None, headers=None):
        """Returns a json data of the HTTP POST request"""
        return Request.wrapper(request.post, url, data=data, params=params, headers=headers)
    
    @staticmethod
    def get(url, params=None, headers=None):
        """Returns a json data of the HTTP GET request"""
        return Request.wrapper(request.get, url, data=None, params=params, headers=headers)
    
    @staticmethod
    def patch(url, data, params=None, headers=None):
        """Returns a json data of the HTTP PATCH request"""
        return Request.wrapper(request.patch, url, data=data, params=params, headers=headers)
    
    @staticmethod
    def put(url, data, params=None, headers=None):
        """Returns a json data of the HTTP PUT request"""
        return Request.wrapper(request.put, url, data=data, params=params, headers=headers)
    
    @staticmethod
    def wrapper(method, url, data=None, params=None, headers=None, *args, **kwargs):
        """An exception wrapper that returns the response or raises an exception on failure"""
        try:
            response = method(url, data=data, params=params, headers=headers, verify=False)
        except Exception as exception:
            raise exception
        return(response.json())
