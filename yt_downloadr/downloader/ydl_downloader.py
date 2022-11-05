'''
    Classes
    -------
    YdlDownloader(Downloader)
        Concrete Downloader implementation with yt_dlp
'''

from pathlib import Path
from yt_dlp import YoutubeDL as Ydl
from yt_downloadr.info_extractor.info import BasicInfo
from . import Downloader, DownloaderError


YDL_OPTIONS = {
    'noplaylist': True
}


class YdlDownloader(Downloader):
    '''
        Concrete Downlaoder implementation with yt_dlp

        Methods
        -------
        download -> Path
            download video and return its path
    '''

    def download(self, info: BasicInfo, format_id: str) -> Path:
        '''Download video and return its path'''
        self.__info = info
        self.__format_id = format_id

        self._create_path()
        ydl = self._create_downloader()
        self._download(ydl)

        return self.__path

    def _create_path(self) -> None:
        dir_path = Path(self.__dir)
        self._assure_format_id()
        extension = self._get_extension()
        video_id = self._get_video_id()

        file_name = f'{video_id}_{self.__format_id}.{extension}'
        path = dir_path / file_name

        self.__path = path

    def _create_downloader(self) -> Ydl:
        options = dict(**YDL_OPTIONS)
        options['format'] = self.__format_id
        options['opttmpl'] = str(self.__path)

        try:
            ydl = Ydl(options)
        except Exception as exc:
            raise DownloaderError("Failed to create ydl downloader") from exc

        return ydl

    def _download(self, ydl: Ydl) -> None:
        link = self._get_link()

        try:
            ydl.download(link)
        except Exception as exc:
            raise DownloaderError("Could not download selected video") from exc

    def _get_extension(self) -> str:
        return self.__info.formats[self.__format_id]['extension']

    def _get_video_id(self) -> str:
        return self.__info.video_id

    def _assure_format_id(self) -> None:
        if self.__format_id not in self.__info.formats.keys():
            raise DownloaderError("Selected format is not available")

    def _get_link(self) -> str:
        return self.__info.link
