import yt

urls = []

with open("chuj.txt", "r", encoding="utf-8") as f:
  for line in f:
    line = line.strip()
    if line:
      urls.append(line)


for url in urls:
  yt.audiodownloadmp3(url)