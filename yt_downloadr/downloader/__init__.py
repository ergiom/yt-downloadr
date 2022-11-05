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
from yt_downloadr.info_extractor.info import BasicInfo


class Downloader(ABC):
    '''
        Download video from youtube link

        Attributes
        ----------
        dir: str
            directory for storing downloaded videos

        info: BasicInfo
            video info

        format_id: str
            video format id

        Methods
        -------
        download: pathlib.Path
            downloads video from provided link, in specified format and returns its path
    '''

    def __init__(self, directory: str, info: BasicInfo, format_id: str) -> None:
        self.__dir: str = directory
        self.__format_id: str = format_id
        self.__info = info
        self.__path: Path = None

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
