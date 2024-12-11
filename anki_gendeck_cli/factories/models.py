from genanki import Model
from .interfaces import BaseDeckModel

class SimpleDeckModel(BaseDeckModel):
    def __init__(self, type: str = 'Simple Model', id: int = 1607392319):
        self._id = id
        self._type = type

    def create_deck_model(self):
        return Model(
            self._id,
            self._type,
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ]
        )