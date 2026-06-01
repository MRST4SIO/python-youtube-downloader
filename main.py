import yt

url = "https://youtu.be/TOuF7ZbcCUs?si=8H0HNdt4RYqgcFSK"


formats_list = yt.get_formats_list(url)

video_id, audio_id = yt.format_pick(formats_list)

yt.video_and_audio_download(url, video_id=video_id, audio_id=audio_id)
