from utils.download import download_audio

class AudioContext:
    def __init__(self):
        self.download = download_audio
        self.strategy = None

    def set_strategy(self, strategy: 'BaseAudio'):
        self.strategy = strategy

    def get_audio(self, file_name: str) -> None:
        audio_obj = self.strategy(file_name)
        # breakpoint()
        self.download(
            audio_obj.get_audio_url(),
            file_name,
            headers=audio_obj.headers
        )

    
