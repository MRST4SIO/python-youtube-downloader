import yt

url = "https://youtu.be/Npo2I9rY5rM?si=BQMkEF0MzA2JPARf"


formats_list = yt.get_formats_list(url)

video_id, audio_id = yt.format_pick(formats_list)

yt.video_and_audio_download(url, video_id=video_id, audio_id=audio_id)
