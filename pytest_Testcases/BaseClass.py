import logging


class BaseClass:

    def getLogDetails(self):
        logger = logging.getLogger(__name__)
        logFile = logging.FileHandler('APILogFile.log')
        logFormatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        logFile.setFormatter(logFormatter)
        logger.addHandler(logFile)
        logger.setLevel(logging.INFO)
        return logger


