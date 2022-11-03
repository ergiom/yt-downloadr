'''
    Classes
    -------
    InfoExtractor
        abstract InfoExtractor
'''

from abc import ABC, abstractmethod
from .info import BasicInfo

class InfoExtractor(ABC):
    '''
        abstract InfoExtractor
    '''
    def __init__(self) -> None:
        self.__raw_info: dict = None

    @abstractmethod
    def extract(self, link: str) -> BasicInfo:
        '''Factory method for BasicInfo'''
