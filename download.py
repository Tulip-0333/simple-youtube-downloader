import argparse
import pytube

# Set up command line argument parser
parser = argparse.ArgumentParser(description="Download a YouTube video.")
parser.add_argument("url", help="the URL of the video to download")
parser.add_argument("-r", "--resolution", help="the resolution of the video to download", choices=["144p", "240p", "360p", "480p", "720p", "1080p"])
args = parser.parse_args()

# Fetch video information
video = pytube.YouTube(args.url)

# Print video information
print(f"Title: {video.title}")
print(f"Length: {video.length} seconds")
print(f"Available resolutions: {[stream.resolution for stream in video.streams.filter(only_video=True)]}")

# Get the desired video stream based on resolution
if args.resolution:
    stream = video.streams.filter(res=args.resolution, only_video=True).first()
else:
    stream = video.streams.get_highest_resolution()

# Download the video
print("Downloading...")
stream.download()
print("Video downloaded successfully!")
