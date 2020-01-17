import logging


class Logger():
    logger = logging.getLogger(__name__)

    @staticmethod
    def Info(debugMessage):
        logger.info(debugMessage);
    
    @staticmethod
    def Error():
        logger.error();