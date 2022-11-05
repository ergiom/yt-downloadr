'''
    Classes
    -------
    YdlDownloader(Downloader)
        Concrete Downloader implementation with yt_dlp
'''

from pathlib import Path
from yt_dlp import YoutubeDL as Ydl
from yt_downloadr.routes.info_extractor.info import BasicInfo
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
        self._info = info
        self._format_id = format_id

        self._create_path()
        ydl = self._create_downloader()
        self._download(ydl)

        return self._path

    def _create_path(self) -> None:
        dir_path = Path(self._dir)
        self._assure_format_id()
        extension = self._get_extension()
        video_id = self._get_video_id()

        file_name = f'{video_id}_{self._format_id}.{extension}'

        try:
            path = dir_path / file_name
        except Exception as exc:
            raise DownloaderError("Invalid path") from exc

        self._path = path

    def _create_downloader(self) -> Ydl:
        options = dict(**YDL_OPTIONS)
        options['format'] = self._format_id
        options['opttmpl'] = str(self._path)

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
        return self._info.formats[self._format_id]['extension']

    def _get_video_id(self) -> str:
        return self._info.video_id

    def _assure_format_id(self) -> None:
        if self._format_id not in self._info.formats.keys():
            raise DownloaderError("Selected format is not available")

    def _get_link(self) -> str:
        return self._info.link
