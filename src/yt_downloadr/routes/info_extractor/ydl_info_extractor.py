'''
    Classes
    -------
    YdlInfoExtractor(InfoExtractor)
        InfoExtractor for extracting info from yt-dlp
'''

from yt_dlp import YoutubeDL as Ydl
from .info import BasicInfo
from . import InfoExtractor, InfoExtractorError

YDL_CONFIG = {
    'simulate': True,
}


class YdlInfoExtractor(InfoExtractor):
    '''
        InfoExtractor for extraction info from yt-dlp

        Methods
        -------
        extract: BasicInfo
            extracts info received from yt_dlp.YoutubeDL
    '''

    def extract(self, link: str) -> BasicInfo:
        '''Extract info received from yt_dlp.YoutubeDL'''
        self._link = link
        ydl = self._create_ydl()
        self._get_raw_info(ydl)
        extracted_info = self._extract_info()

        return extracted_info

    def _create_ydl(self) -> Ydl:
        try:
            ydl = Ydl(YDL_CONFIG)
        except Exception as exc:
            raise InfoExtractorError(
                "Failed to create yt_dlp.YoutubeDL instance") from exc

        return ydl

    def _get_raw_info(self, ydl: Ydl) -> None:
        try:
            info = ydl.extract_info(self._link)
            self._raw_info = ydl.sanitize_info(info)
        except Exception as exc:
            raise InfoExtractorError("Failed to download video info") from exc

    def _extract_info(self) -> BasicInfo:
        try:
            title = self._raw_info['title']
            formats = self._configure_formats()
            video_id = self._raw_info['id']
        except Exception as exc:
            raise InfoExtractorError("Received info is incomplete") from exc

        basic_info = BasicInfo(
            link=self._link,
            title=title,
            formats=formats,
            video_id=video_id
        )

        return basic_info

    def _configure_formats(self) -> dict:
        raw_formats = self._raw_info['formats']
        formats = {}
        for raw_format in raw_formats:
            try:
                format_id = raw_format['format_id']
                extension = raw_format['ext']
                resolution = raw_format['format_note']
                size = raw_format['filesize']
            except KeyError as exc:
                continue
            formats[format_id] = {
                'extension': extension,
                'resolution': resolution,
                'size': size
            }

        return formats
