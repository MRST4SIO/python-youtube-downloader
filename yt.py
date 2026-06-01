import yt_dlp
from typing import List, Dict, Any, Union


def extract_info(url: str):
    ytl_opts = {
        'quiet': True,
        'no_warnings': True
    }
    with yt_dlp.YoutubeDL(ytl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info

def get_formats_from_info(url: str, info=None):
    if info is None:
        info = extract_info(url)
    if not isinstance(info, dict):
        print("Info is incorrect: expected a dict")
        return []
    return info.get('formats', [])

def get_formats_list(url) -> List[List[Dict[str, Any]]]:

  info = extract_info(url)
  if not isinstance(info, dict):
    return [[], [], []]
  formats = info.get('formats', [])

  video_formats = []
  audio_formats = []
  video_and_audio_formats = []

  for f in formats:

    vcodec = f.get('vcodec', 'none')
    acodec = f.get('acodec', 'none')
    
    if vcodec != 'none' and acodec != 'none':
        video_and_audio_formats.append(f)
    elif vcodec != 'none' and acodec == 'none':
        video_formats.append(f)
    elif vcodec == 'none' and acodec != 'none':
        audio_formats.append(f)

  formats_list = [video_formats, audio_formats, video_and_audio_formats]
  

  return formats_list


def display_video_formats_list(formats_list: List[List[Dict[str, Any]]]):
    print("VIDEO:")
    for f in formats_list[0]:
      format_id = f.get("format_id")
      vcodec = f.get("vcodec")
      ext = f.get("ext")
      fps = f.get("fps")
      res = f.get("resolution")
      tbr = f.get("tbr")
      print(format_id, vcodec, ext, fps, res, tbr)

    
def display_audio_formats_list(formats_list: List[List[Dict[str, Any]]]):
    
    print("AUDIO:")
    for f in formats_list[1]:
      format_id = f.get("format_id")
      acodec = f.get("acodec")
      ext = f.get("ext")
      tbr = f.get("tbr")
      print(format_id, acodec, ext, tbr)

          
def format_pick(formats_list) -> Union[str | None, str | None]:
  display_video_formats_list(formats_list)
  video_id = input("Pick VIDEO format ID: ") or None
  display_audio_formats_list(formats_list)
  audio_id = input("Pick AUDIO format ID: ") or None
  
  return (video_id, audio_id)

def video_and_audio_download(url: str, video_id: str, audio_id: str):

  if video_id and audio_id:
    fmt = f"{video_id}+{audio_id}"
  else:
    fmt = video_id or audio_id

  if not fmt:
    return {'status': 'error', 'errors': ['no format selected']}

  ydl_options = {
      'quiet': True,
      'no_warnings': True,
      'format': fmt,
      'outtmpl': '%(title)s.%(ext)s',
      'merge_output_format': 'mp4',
  }

  try:
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
      ydl.download([url])
  except Exception as e:
    print(f"Download error: {e}")
    return {'status': 'error', 'errors': [str(e)]}

  return {'status': 'ok'}