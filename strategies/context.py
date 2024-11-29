from . import BaseAudio 
from ..utils.download import download_audio

class AudioContext:
    def __init__(self):
        self.download = download_audio

    def set_strategy(strategy: BaseAudio):
        self.strategy = strategy

    def get_audio(self, file_name: str):
        self.download(
            self.set_strategy.get_audio_url(file_name),
            file_name
        )

    
