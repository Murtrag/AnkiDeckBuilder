from abc import ABC, abstractmethod

class BaseAudio(ABC):
    def __init__(self, text: str):
        self._text = text
    
    def get_media_url(self)-> str:
        pass

    # def download_audio(self)-> None:
    #     pass