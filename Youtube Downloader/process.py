from pytube import YouTube


class Video:

    def __init__(self, link):
        self.yt = YouTube(link)

    # Get Video Title
    def title(self):
        return self.yt.title

    # Get Video Thumbnail
    def thumbnail(self):
        return self.yt.thumbnail_url

    # Get Video Size
    def size(self):
        video = self.yt.streams.get_highest_resolution()
        return round(int(video.filesize) / (1024*1024), 2)

    # Download the video
    def download(self):
        # Set Screen Resolution
        video = self.yt.streams.get_highest_resolution()
        # download the video
        video.download()


if __name__ == '__main__':
    vid = Video("https://www.youtube.com/watch?v=GQ9NS6nEiao")
    vid.title()
    vid.thumbnail()
    vid.download()
