import logging
from logdna import LogDNAHandler
import datetime

from enum import Enum



class levels(int,Enum):
    info= logging.INFO
    warning = logging.WARNING
    critical = logging.CRITICAL
    debug=logging.DEBUG
    error = logging.ERROR

class Log():
    def __init__(self,key):
        self.logger = logging.getLogger("logdna")
        self.logDna = LogDNAHandler(key)
        self.logger.addHandler(self.logDna)

    def log(self,level:levels,message):\

        self.logger.log(level,f"{self.getTime()} : {message}")

    def getTime(self):
        CTime = datetime.datetime.now()
        CTime = CTime.strftime("%H-%M-%S")
        return CTime
