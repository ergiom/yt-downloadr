'''
    Classes
    -------
    Downloader
        downloads video from youtube link

    Exceptions
    ----------
    DownloaderError
        Core Downloader exception
'''

from abc import ABC, abstractmethod
from pathlib import Path
from yt_downloadr import YtDownloadrError


class Downloader(ABC):
    '''
        Download video from youtube link

        Methods
        -------
        download: pathlib.Path
            downloads video from provided link, in specified format and returns its path
    '''

    def __init__(self) -> None:
        self.__link: str = None
        self.__format_id: str = None

    @abstractmethod
    def download(self, link: str, format_id: str) -> Path:
        '''
            Downloads file from youtube link in specified format
            download -> pathlib.Path
            
            Attributes
            ----------
            link: str
                youtube video link
            
            format_id: str
                video format id
        '''

class DownloaderError(YtDownloadrError):
    '''Core Downloader exception'''
