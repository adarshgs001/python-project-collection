import yt_dlp

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            'proxy': '',  # 👈 disables any proxy use
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Download completed!")

    except Exception as e:
        print("⚠️ Error:", e)

video_url = input("Enter YouTube video URL: ")
download_video(video_url)