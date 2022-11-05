'''
    Classes
    -------
    VideoRoute
        returns for get and post http methods
'''

from pathlib import Path
from flask import render_template, send_file, abort
from yt_downloadr.routes.info_extractor import InfoExtractor, InfoExtractorError
from yt_downloadr.routes.downloader import Downloader, DownloaderError
from yt_downloadr.routes.info_extractor.info import BasicInfo


class VideoRoute:
    '''
        Returns for get and post http methods

        Attributes
        ----------
        downloader: Downloader
            downloads video in specified format

        info_extractor: InfoExtractor
            extracts info about specified video

        Methods
        -------
        get
            flask return for http get request
        post
            flask return for http post request
    '''

    def __init__(self, downloader: Downloader, info_extractor: InfoExtractor,
                 video_id: str) -> None:
        self._downloader = downloader
        self._info_extractor = info_extractor
        self._link = self._create_link(video_id)

    def get(self):
        '''
            Flask return for http get request
        '''

        info = self._get_info()

        return render_template('video.html', info=info)

    def post(self, form: dict):
        '''
            Flask return for http post request
        '''

        info = self._get_info()
        path = self._download(info, form)

        return send_file(path)

    def _create_link(self, video_id: str) -> str:
        link = f'http://youtube.com/watch?v={video_id}'

        return link

    def _get_info(self) -> BasicInfo:
        try:
            info = self._info_extractor.extract(self._link)
        except InfoExtractorError:
            return abort(400)

        return info

    def _download(self, info, form) -> Path:
        try:
            path = self._downloader.download(info, form['format_id'])
        except DownloaderError:
            return abort(503)

        return path
