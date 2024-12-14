from os.path import join
from anki_gendeck_cli.utils.download import download_media

class ImageContext:
    def __init__(self, image_dir="image"):
        self.strategy = None
        self.image_dir = image_dir
        self.download = download_media

    def set_strategy(self, strategy: 'BaseImage') -> None:
        self.strategy = strategy

    def get_image_urls(self, file_name: str) -> List[str]:
        strategy_obj = self.strategy(file_name)
        return strategy_obj.get_image_urls()
