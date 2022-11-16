# download video from youtube
from pytube import YouTube

# get video url from user
url = input("Enter the video url: ")
# create YouTube object
yt = YouTube(url)
# get the video with the highest resolution
video = yt.streams.get_highest_resolution()

# start download
video.download()

# display message success
print("Video downloaded successfully")

# information about the video
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Description: ", yt.description)
print("Ratings: ", yt.rating)
print("Author: ", yt.author)