# yt-downloadr

Simple flask webapp based on yt-dlp.
This project is mainly educational (cs50), but it might be extended in the future.

## environment

- FLASK_SECRET_KEY
- (opt) FLASK_DOWNLOAD_DIR

## example setup
Here is an example setup using waitress wsci

```bash
export FLASK_SECRET_KEY="123abc"
export FLASK_DOWNLOAD_DIR="/tmp"

waitress --call 'yt_downloadr:create_app'
```
