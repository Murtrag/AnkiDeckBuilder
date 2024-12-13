from os.path import join

from anki_gendeck_cli.utils.download import download_media

class AudioContext:
    def __init__(self, audio_dir="audio"):
        self.strategy = None
        self.audio_dir = audio_dir
        self.download = download_audio

    def set_strategy(self, strategy: 'BaseAudio') -> None:
        self.strategy = strategy

    def get_audio_file(self, file_name: str) -> str:
        audio_obj = self.strategy(file_name)
        
        self.download(
            audio_obj.get_audio_url(),
            f"{file_name}.mp3",
            audio_dir=self.audio_dir,
            headers=audio_obj.headers
        )
        return join(self.audio_dir, f"{file_name}.mp3")


    
