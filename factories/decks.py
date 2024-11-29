

class SimpleDeck(BaseDeck):
    def create_deck(self):
        return genanki.Deck(
            self.id,
            self.name
        )