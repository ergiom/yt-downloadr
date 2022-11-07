'''yt_downloader router'''

from flask import request
from yt_downloadr import app
from yt_downloadr.routes.index_route import IndexRoute
from yt_downloadr.routes.video_route import VideoRoute
from yt_downloadr.routes.info_extractor.ydl_info_extractor import YdlInfoExtractor
from yt_downloadr.routes.downloader.ydl_downloader import YdlDownloader
from yt_downloadr.routes.forms.video import SimpleVideoForm


# routes
@app.route('/')
def index():
    '''Index path of yt_downloadr'''
    route = IndexRoute()

    return route.get()


@app.route('/video/<video_id>', methods=["GET", "POST"])
def video(video_id):
    '''Video path of yt_downloadr'''
    download_dir = app.config['DOWNLOAD_DIR']
    downloader = YdlDownloader()
    info_extractor = YdlInfoExtractor()
    route = VideoRoute(
        downloader=downloader,
        info_extractor=info_extractor,
        video_id=video_id
    )

    form = SimpleVideoForm()

    if request.method == "GET":
        return route.get()

    if form.validate_on_submit():
        return route.post(form.format_id.data)
