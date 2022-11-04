'''Test YdlInfoExtractor'''

import pytest
import yt_dlp
from yt_downloadr.info_extractor.info import BasicInfo
from yt_downloadr.info_extractor import InfoExtractorError
from yt_downloadr.info_extractor.ydl_info_extractor import YdlInfoExtractor


class MockYdl:
    @staticmethod
    def extract_info_correct(*args, **kwargs):
        pass

    @staticmethod
    def extract_info_error(*args, **kwargs):
        raise Exception

    @staticmethod
    def sanitize_info_correct(*args, **kwargs):
        return {
            'title': 'some title',
            'formats': [
                {
                    'format_id': '123',
                    'ext': 'mp4',
                    'format_note': '720p',
                    'filesize': '1234'
                }
            ]
        }

    @staticmethod
    def sanitize_info_incomplete_no_formats(*args, **kwargs):
        return {
            'title': 'some title',
        }

    @staticmethod
    def sanitize_info_correct_one_format_complete_one_format_incomplete(*args, **kwargs):
        return {
            'title': 'some title',
            'formats': [
                {
                    'format_id': '123',
                    'ext': 'mp4',
                    'format_note': '720p',
                    'filesize': '1234'
                },
                {
                    'format_id': 'no_size',
                    'ext': 'mp4',
                    'format_note': '720p',
                }
            ]
        }

    @staticmethod
    def sanitize_info_error(*args, **kwargs):
        raise Exception


class Returns:
    @staticmethod
    def returned_basic_info(*args, **kwargs):
        return BasicInfo(
            link='some_link',
            title='some title',
            formats={
                '123': {
                    'extension': 'mp4',
                    'resolution': '720p',
                    'size': '1234'
                }
            }
        )


class TestYdlInfoExtractor:
    def test_extract_info_raises_when_ydl_raises(self):
        pytest.MonkeyPatch().setattr(
            yt_dlp.YoutubeDL, 'extract_info', MockYdl.extract_info_error)
        ydl_extractor = YdlInfoExtractor()
        with pytest.raises(InfoExtractorError):
            ydl_extractor.extract('some_link')

    def test_sanitize_info_raises_when_ydl_raises(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'extract_info',
                                     MockYdl.extract_info_correct)
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'sanitize_info',
                                     MockYdl.sanitize_info_error)
        ydl_extractor = YdlInfoExtractor()
        with pytest.raises(InfoExtractorError):
            ydl_extractor.extract('some_link')

    def test_raises_when_received_incomplete_info(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'extract_info',
                                     MockYdl.extract_info_correct)
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'sanitize_info',
                                     MockYdl.sanitize_info_incomplete_no_formats)
        ydl_extractor = YdlInfoExtractor()
        with pytest.raises(InfoExtractorError):
            ydl_extractor.extract('some_link')

    def test_passes_when_some_formats_incomplete(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'extract_info',
                                     MockYdl.extract_info_correct)
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'sanitize_info',
                                     MockYdl.sanitize_info_correct_one_format_complete_one_format_incomplete)
        ydl_extractor = YdlInfoExtractor()
        info = ydl_extractor.extract('some_link')
        assert info == Returns.returned_basic_info()

    def test_passes_when_correct(self):
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'extract_info',
                                     MockYdl.extract_info_correct)
        pytest.MonkeyPatch().setattr(yt_dlp.YoutubeDL, 'sanitize_info',
                                     MockYdl.sanitize_info_correct)
        ydl_extractor = YdlInfoExtractor()
        info = ydl_extractor.extract('some_link')
        assert info == Returns.returned_basic_info()
