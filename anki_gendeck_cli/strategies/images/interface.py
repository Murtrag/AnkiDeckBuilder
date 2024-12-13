from abc import ABC, abstractmethod

class BaseImage(ABC):
    def __init__(self, text: str):
        self._text = text
    
    @abstractmethod
    def get_image_urls(self)-> str:
        pass