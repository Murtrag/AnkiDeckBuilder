import base64
from .interface import BaseAudio

class DutchAudio(BaseAudio):
    def __init__(self, text: str):
        super().__init__(text)
        self._voice = 'Femke22k'
        self._speed = '80'

    def get_audio_url(self):
        base_url = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream"
        encoded_text = base64.b64encode(self._text.encode("utf-8")).decode("utf-8")
        url = f"{base_url}/voiceName={self._voice}?voiceSpeed={self._speed}&inputText={encoded_text}"
        return url
    
    