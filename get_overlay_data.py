import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random

def get_youtube_api_key():
    # YouTube API anahtarınızı buraya ekleyin
    #ben alamadım vaktim yoktu googleapıs den proje oluşturarak alabiliyoruz
    return "YOUR_YOUTUBE_API_KEY"

def get_random_youtube_video():
    api_key = get_youtube_api_key()
    youtube = build("youtube", "v3", developerKey=api_key)

    try:
        # YouTube API'sinden rastgele bir video al
        search_response = youtube.search().list(
            q="",
            type="video",
            part="id",
            maxResults=50
        ).execute()

        # Alınan videolardan rastgele birini seç
        random_video = random.choice(search_response.get("items", []))

        video_id = random_video["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        return {"video_id": video_id, "video_url": video_url}
    except HttpError as e:
        print(f"Hata: {e}")
        return None

if __name__ == "__main__":
    random_youtube_video = get_random_youtube_video()

    if random_youtube_video:
        print(random_youtube_video)
    else:
        print("Rastgele YouTube videosu alınamadı.")
