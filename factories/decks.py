from genanki import Deck
from .interfaces import BaseDeck

class SimpleDeck(BaseDeck):
    def create_deck(self):
        return Deck(
            self.id,
            self.name
        )