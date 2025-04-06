import sys
import importlib
import pip

def update_package(package_name):
    pip.main(['install', '--upgrade', package_name])

def run_gallery_dl(url, args):
    update_package('gallery-dl')
    import gallery_dl
    config = gallery_dl.config.load()
    job = gallery_dl.job.DownloadJob(url, config)
    print("gallery-dl by Mike Fährmann, et. al.")
    job.run()

def run_yt_dlp(url, args):
    update_package('yt-dlp')
    import yt_dlp

    ydl_opts = {}
    # Parse additional args into ydl_opts if needed

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py [gallery-dl|yt-dlp] [URL] [additional args...]")
        sys.exit(1)

    tool = sys.argv[1]
    url = sys.argv[2]
    additional_args = sys.argv[3:]

    if tool == 'gallery-dl':
        run_gallery_dl(url, additional_args)
    elif tool == 'yt-dlp':
        run_yt_dlp(url, additional_args)
    else:
        print(f"Unknown tool: {tool}")
        sys.exit(1)

if __name__ == "__main__":
    main()