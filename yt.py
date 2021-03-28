
import youtube_dl


def download_video(file_name, url):
    ydl_opts = {
        'outtmpl': file_name,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        return True


download_video("1.mp4", 'https://timesofindia.indiatimes.com/videos/news/bjp-vs-tmc-matua-community-and-its-electoral-significance-in-bengal/videoshow/81713301.cms')
