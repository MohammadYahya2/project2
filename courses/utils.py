# courses/utils.py

import re

def convert_video_url(url):
    """
    Converts standard video URLs to their respective embed URLs.
    Supports YouTube, Vimeo, and Google Drive.
    """
    # YouTube
    youtube_match = re.match(r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)(?P<id>[a-zA-Z0-9_-]{11})', url)
    if youtube_match:
        video_id = youtube_match.group('id')
        return f'https://www.youtube.com/embed/{video_id}'

    # Vimeo
    vimeo_match = re.match(r'(https?://)?(www\.)?vimeo\.com/(?P<id>\d+)', url)
    if vimeo_match:
        video_id = vimeo_match.group('id')
        return f'https://player.vimeo.com/video/{video_id}'

    # Google Drive
    gdrive_match = re.match(r'(https?://)?(drive\.google\.com/file/d/)(?P<id>[^/]+)/view', url)
    if gdrive_match:
        file_id = gdrive_match.group('id')
        return f'https://drive.google.com/file/d/{file_id}/preview'

    # If no match, return the original URL
    return url
