from genanki import Note
from .interfaces import BaseNote, BaseDeckModel
from ..strategies.audio import AudioContext



class SimpleNote(BaseNote):
    def create_note(
        self,
        deck_model: BaseDeckModel,
        sound_strategy: 'BaseAudio',
        word: str,
        back: str
        ):

        prefix, *front = word.split(" ")
        front = " ".join(front)
        sound_name = front if front != "" else prefix
            

        audio_obj = sound_strategy(sound_name)
        # sound_url = audio_obj.get_audio_url()

        context = AudioContext()
        context.set_strategy(sound_strategy)
        try:
            context.get_audio(sound_name)
        except Exception as e:
            print(e)

        front_html = f'<span style="color: rgb(0, 0, 255); background-color: rgb(0, 170, 0);"><b>{word}</b></span><br>\
        [sound:{sound_name}.mp3]\
        '
        return Note(
            model=deck_model,
            fields=[
                front_html,
                back
                ])