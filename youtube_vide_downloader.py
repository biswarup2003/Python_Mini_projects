from pytube import YouTube

try:
    # Replace 'VIDEO_URL' with the actual YouTube video URL
    youtube_url = 'https://www.youtube.com/embed/QP3v5RMEo4c?si=yLdlHEWURg8jMtHG'
    youtube_1 = YouTube(youtube_url)
    
    # Get the list of all available streams
    videos = youtube_1.streams.all()
    for i, stream in enumerate(videos):
        print(f"{i}: {stream}")
        
except Exception as e:
    print(f"An error occurred: {e}")
