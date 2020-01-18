import logging


class Logger():
    def __init__(self, __name__):
        self.logger = logging.getLogger(__name__)

    
    def Info(self, message):
        self.logger.info("""
        MESSAGE => %s n\
        """% message);
    
    
    def Error(self, exception):
        self.logger.error("""
        ERRORMESSAGE => %s """%exception,exc_info=1);