# yt_downloader

A small command-line YouTube downloader built on top of [`yt-dlp`](https://github.com/yt-dlp/yt-dlp). It lists the available video and audio formats for a given URL, lets you pick which ones you want, and downloads/merges them into a single `.mp4` file.

## Requirements

- Python 3.8+
- [`yt-dlp`](https://pypi.org/project/yt-dlp/)
- [`ffmpeg`](https://ffmpeg.org/) (required by `yt-dlp` to merge separate video and audio streams)

## Installation

```bash
python -m venv venv
source venv/bin/activate
pip install yt-dlp
```

Make sure `ffmpeg` is installed and available on your `PATH`.

## Usage

Set the video URL in `main.py`:

```python
url = "https://youtu.be/your_video_id"
```

Then run:

```bash
python main.py
```

The script will:

1. Fetch and list the available **video** formats (format ID, codec, extension, fps, resolution, bitrate).
2. Prompt you to pick a **video** format ID.
3. List the available **audio** formats and prompt you to pick an **audio** format ID.
4. Download the selected streams and merge them into an `.mp4` file named after the video title.

You can leave a prompt empty to skip that stream (e.g. download audio only or video only).

## Project structure

- `main.py` — entry point; sets the URL and drives the download flow.
- `yt.py` — helper functions for extracting info, listing/filtering formats, prompting for a selection, and downloading.

## Module overview (`yt.py`)

| Function | Description |
| --- | --- |
| `extract_info(url)` | Extracts metadata for a URL without downloading. |
| `get_formats_from_info(url, info=None)` | Returns the raw `formats` list from the info dict. |
| `get_formats_list(url)` | Splits formats into `[video_only, audio_only, video_and_audio]`. |
| `display_video_formats_list(formats_list)` | Prints the available video-only formats. |
| `display_audio_formats_list(formats_list)` | Prints the available audio-only formats. |
| `format_pick(formats_list)` | Displays formats and prompts for video/audio IDs. |
| `video_and_audio_download(url, video_id, audio_id)` | Downloads and merges the selected formats. |

## Notes

Downloaded media files (`*.mp4`, `*.mkv`, `*.webm`, `*.m4a`, `*.mp3`) are ignored by git.
