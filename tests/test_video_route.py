import pytest
from pathlib import Path
import yt_downloadr.routes.video_route as vroute
from yt_downloadr.routes.info_extractor.ydl_info_extractor import YdlInfoExtractor, InfoExtractorError
from yt_downloadr.routes.downloader.ydl_downloader import YdlDownloader, DownloaderError
from yt_downloadr.routes.info_extractor.info import BasicInfo

class MockFlask:
    @staticmethod
    def abort(*args, **kwargs):
        raise StatusError

    @staticmethod
    def render_template(*args, **kwargs):
        return 'pass'

    @staticmethod
    def send_file(*args, **kwargs):
        return 'send'


class StatusError(RuntimeError):
    '''4XX or 5XX http status'''


class DownloaderException(YdlDownloader):
    def download(self, *args, **kwargs):
        raise DownloaderError


class DownloaderPass(YdlDownloader):
    def download(self, *args, **kwargs):
        return Path('.')


class InfoExtractorException(YdlInfoExtractor):
    def extract(self, *args, **kwargs):
        raise InfoExtractorError


class InfoExtractorPass(YdlInfoExtractor):
    def extract(self, *args, **kwargs):
        return BasicInfo('link', 'title', {}, 'id')


class TestVideoRoute:
    def test_get_raises_if_info_extractor_raises(self):
        pytest.MonkeyPatch().setattr(vroute, 'abort', MockFlask.abort)
        video_route = vroute.VideoRoute(DownloaderPass('dir'), InfoExtractorException(), 'id')
        with pytest.raises(StatusError):
            video_route.get()

    def test_get_passes(self):
        pytest.MonkeyPatch().setattr(vroute, 'render_template', MockFlask.render_template)
        video_route = vroute.VideoRoute(DownloaderPass('dir'), InfoExtractorPass(), 'id')

        assert video_route.get() == 'pass'

    def test_post_raises_if_info_extractor_raises(self):
        pytest.MonkeyPatch().setattr(vroute, 'abort', MockFlask.abort)
        video_route = vroute.VideoRoute(DownloaderPass('dir'), InfoExtractorException(), 'id')
        with pytest.raises(StatusError):
            video_route.post('id')

    def test_post_raises_if_downloader_raises(self):
        pytest.MonkeyPatch().setattr(vroute, 'abort', MockFlask.abort)
        video_route = vroute.VideoRoute(DownloaderException('dir'), InfoExtractorPass(), 'id')
        with pytest.raises(StatusError):
            video_route.post('id')

    def test_post_passes(self):
        pytest.MonkeyPatch().setattr(vroute, 'send_file', MockFlask.send_file)
        video_route = vroute.VideoRoute(DownloaderPass('dir'), InfoExtractorPass(), 'id')

        assert video_route.post('id') == 'send'
