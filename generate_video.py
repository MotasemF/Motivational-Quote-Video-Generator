from random_quote import RandomQuote
from tiktok_tts import TikTokTTS
from pexels_api_video import PexelsApi
from video_editor import Generator

NUM_OF_VIDEOS = 10

for i in range(NUM_OF_VIDEOS):
    random_quote = RandomQuote()
    quote = random_quote.get()

    pexels = PexelsApi()
    pexels.run()

    tts = TikTokTTS()
    tts.run(quote, "audio.mp3")

    generator = Generator()
    generator.run(quote_text=quote, background_video_path="video.mp4", audio_path="audio.mp3")