class SimpleNote(ABC):
    def create_note(self, front: str, back: str):
        front_html = f'<span style="color: rgb(0, 0, 255);"><b>{prefox} {front}</b></span><br>\
        [sound:{front}.mp3]\
        '
        return genanki.Note(
            model=deck_model,
            fields=[
                front_html,
                back
                ])