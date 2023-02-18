import random
import time
import requests
import base64

__all__ = ["TikTokTTS"]

voices = ["en_us_007", "en_us_009", "en_uk_003"]

class TikTokTTS:
    def __init__(self) -> None:
        headers = {
            "User-Agent": "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)",
            "Cookie": "sessionid=73c267765f5ac56067cbfa98e98a51cf",
        }

        self.URI_BASE = (
            "https://api16-normal-c-alisg.tiktokv.com/media/api/text/speech/invoke/"
        )
        self.max_chars = 300
        self._session = requests.Session()
        self._session.headers = headers

    def run(self, text: str, filepath: str):
        voice = voices[2]

        data = self.get_generated_audio(voice=voice, text=text)

        status_code = data["status_code"]
        if status_code != 0:
            raise Exception("error in" + data["message"])

        try:
            raw_voices = data["data"]["v_str"]
        except:
            print(
                "The TikTok TTS returned an invalid response. Please try again later, and report this bug."
            )

        decoded_voices = base64.b64decode(raw_voices)
        with open(filepath, "wb") as f:
            f.write(decoded_voices)

    def get_generated_audio(self, text: str, voice: str):
        return self.get_voices(text, voice)


    def get_voices(self, text: str, voice: str):
        text = text.replace("+", "plus").replace("&", "and").replace("r/", "")
        params = {
            "req_text": text,
            "speaker_map_type": 0,
            "aid": 1233,
            "text_speaker": voice,
        }

        try:
            response = self._session.post(self.URI_BASE, params=params)
        except ConnectionError:
            time.sleep(random.ranrange(1, 7))

        return response.json()
