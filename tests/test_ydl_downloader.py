'''Test YdlDownloader'''

import pytest
import yt_dlp
from pathlib import Path
from yt_downloadr.routes.info_extractor.info import BasicInfo
from yt_downloadr.routes.downloader import DownloaderError
from yt_downloadr.routes.downloader.ydl_downloader import YdlDownloader


class MockYdl:
    @staticmethod
    def download_failed(*args, **kwargs):
        raise Exception("Download failed")

    @staticmethod
    def download_successfull(*args, **kwargs):
        pass


class DataForTests:
    @staticmethod
    def basic_info():
        return BasicInfo(
            link='some link',
            title='some title',
            formats={
                'format1': {
                    'extension': 'mp4',
                    'resolution': '720p',
                    'size': '1234'
                }
            },
            video_id='some_id'
        )

    @staticmethod
    def returned_path():
        return Path('.') / 'some_id_format1.mp4'


class TestYdlDownloader:
    def test_ydl_downloader_fails_when_download_fails(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'download', MockYdl.download_failed)
        ydl_downloader = YdlDownloader('.')
        with pytest.raises(DownloaderError):
            ydl_downloader.download(DataForTests.basic_info(), 'format1')

    def test_ydl_downloader_returns_path(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'download', MockYdl.download_successfull)
        ydl_downloader = YdlDownloader('.')
        path = ydl_downloader.download(DataForTests.basic_info(), 'format1')
        assert DataForTests.returned_path() == path

    def test_ydl_downloader_fails_when_format_doesnt_exists(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'download', MockYdl.download_successfull)
        ydl_downloader = YdlDownloader('.')
        with pytest.raises(DownloaderError):
            ydl_downloader.download(DataForTests.basic_info(), 'bad_format')
