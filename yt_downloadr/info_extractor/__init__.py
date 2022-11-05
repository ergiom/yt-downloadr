'''
    Classes
    -------
    InfoExtractor
        abstract InfoExtractor

    Exceptions
    ----------
    InfoExtractorError(YtDownloadrError)
        Exception for InfoExtractor
'''

from abc import ABC, abstractmethod
from yt_downloadr import YtDownloadrError
from .info import BasicInfo

class InfoExtractor(ABC):
    '''
        abstract InfoExtractor
    '''
    def __init__(self) -> None:
        self._raw_info: dict = None
        self._link: str = None

    @abstractmethod
    def extract(self, link: str) -> BasicInfo:
        '''Factory method for BasicInfo'''


class InfoExtractorError(YtDownloadrError):
    '''Exception for InfoExtractor'''
