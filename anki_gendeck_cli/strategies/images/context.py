from typing import List
from os.path import join
from ..utils.download import download_media

class ImageContext:
    def __init__(self, image_dir="image"):
        self.strategy = None
        self.image_dir = image_dir
        self.download = download_audio

    def set_strategy(self, strategy: 'BaseImage') -> None:
        self.strategy = strategy

    def get_image_urls(self, file_name: str) -> List[str]:
        strategy_obj = self.strategy(file_name)
        return strategy_obj.get_image_urls()
