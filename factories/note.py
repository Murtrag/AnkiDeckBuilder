from genanki import Note
from .interfaces import BaseNote, BaseDeckModel



class SimpleNote(BaseNote):
    def create_note(
        self,
        deck_model: BaseDeckModel,
        sound_strategy: 'BaseAudio',
        front: str,
        back: str
        ):

        prefix, *front = front.split(" ")
        front = " ".join(front)

        audio_obj = sound_strategy(front)
        sound_url = audio_obj.get_audio_url()

        front_html = f'<span style="color: rgb(0, 0, 255);"><b>{prefix} {front}</b></span><br>\
        [sound:{front}.mp3]\
        '
        return Note(
            model=deck_model,
            fields=[
                front_html,
                back
                ])