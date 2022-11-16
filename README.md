# Youtube-Downloader

Download videos from youtube using Python

## Install Modules

```bash
pip install -r requirements.txt
```

## Import Modules

```python
from pytube import YouTube
```

## Get Video Link

```python
url = input("Enter the video url: ")
# create a YouTube object
yt = YouTube(url)
```

## Get the video with the highest resolution

```python
video = yt.streams.get_highest_resolution()
```

## Download the video

```python
video.download()
# display message success
print("Video downloaded successfully")
```

## Get Video Title

```python
print("Title: ", yt.title)
```

## Get Video Description

```python
print("Description: ", yt.description)
```

## Get Video Length

```python
print("Length: ", yt.length)
```

## Get Video Views

```python
print("Views: ", yt.views)
```

## Get Video Rating

```python
print("Rating: ", yt.rating)
```

## Get Video Author

```python
print("Author: ", yt.author)
```

# Author

[**@faresemad**](https://github.com/faresemad)(Fares Emad)
