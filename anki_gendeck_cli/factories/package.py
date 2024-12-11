import os
from genanki import Package

from .interfaces import BasePackage


class SimplePackage(BasePackage):
    def __init__(self):
        self.audio_dir = "audio"

    def create_package(self, deck: 'BaseDeck'):
        package = Package(deck)

        for root, dirs, files in os.walk(self.audio_dir):
            for file in files:
                if file.endswith(".mp3"):
                    package.media_files.append(os.path.join(root, file))
        return package
        