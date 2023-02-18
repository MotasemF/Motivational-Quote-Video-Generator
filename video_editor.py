from moviepy.editor import *
from moviepy.video.tools.drawing import *
from moviepy.video.fx.all import crop
from PIL import ImageFont
from moviepy.video.fx.all import resize
from gtts import gTTS
from tiktok_tts import TikTokTTS

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_DURATION = 12
FONT_PATH = 'Itim-Regular.ttf'
FONT_SIZE = 60
FONT_COLOR = 'white'
FPS = 30

class Generator:
    def __init__(self) -> None:
        pass

    def run(self, quote_text: str, background_video_path: str, audio_path: str):
        bg_clip = VideoFileClip(background_video_path, audio=False)
        (w, h) = bg_clip.size
        bg_clip = crop(bg_clip, width=VIDEO_WIDTH, height=VIDEO_HEIGHT, x_center=w/2, y_center=h/2)
        bg_clip = bg_clip.resize((VIDEO_WIDTH, VIDEO_HEIGHT))
        bg_clip = bg_clip.fx(vfx.colorx, 0.2)
        bg_clip = bg_clip.loop(duration = VIDEO_DURATION)

        audio_clip = AudioFileClip(audio_path).set_start(1)
        audio_composite = CompositeAudioClip([audio_clip])

        txt_clip  = TextClip(quote_text, fontsize=FONT_SIZE, font=FONT_PATH, color=FONT_COLOR, align='center', size=(VIDEO_WIDTH - 200, VIDEO_HEIGHT) , method='caption')
        txt_clip = txt_clip.set_start(1)

        final_clip = CompositeVideoClip([bg_clip, txt_clip.set_position(('center', 'center'))], size=(VIDEO_WIDTH, VIDEO_HEIGHT)).set_duration(VIDEO_DURATION)
        final_clip.audio = audio_composite
        final_clip.write_videofile(f"out/{quote_text}.mp4", fps=FPS)
            