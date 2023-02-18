import requests
import json
import random
import os
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

PEXELS_API_KEY = config["DEFAULT"]["PexelsApiKey"]
URL = "https://api.pexels.com/videos/search?query=Man doing Exercise&per_page=100&size=small&orientation=portrait"
RESPONSE_PATH = "pexelsApiResponse.json"

class PexelsApi:
    def init(self) -> None:
        pass

    def run(self):
        if not os.path.isfile(RESPONSE_PATH) or os.path.getsize(RESPONSE_PATH) <= 0:
            self.send_request()
        
        video_url = self.get_video_url()
        self.download_video(video_url)


    def send_request(self):
        headers = {
            "Authorization": PEXELS_API_KEY,
        }
        res = requests.get(URL)

        if res.status_code != 200:
            raise "Error happens when fetching the videos objects"

        data = res.json()
        with open(RESPONSE_PATH, "w") as f:
           json.dump(data, f)

    def get_video_url(self) -> str:
        json_file = json.load(open(RESPONSE_PATH))
        videos = json_file["videos"]
        index = random.randint(0, len(videos) - 1)
        return videos[index]['video_files'][0]['link']

    def download_video(self, video_url: str):
        response = requests.get(video_url, stream=True)
        with open("video.mp4", "wb") as f:
            for chunk in response.iter_content(chunk_size=8192): 
                f.write(chunk)




            