from abc import ABC, abstractmethod
import genanki

class BaseDeckModel(ABC):
    @abstractmethod
    def create_deck_model(self):
        pass


class BaseDeck(ABC):
    def __init__(self, model: BaseDeckModel, name: str, deck_id: int = 2059417507):
        self.model = model
        self.name = name
        self.id = deck_id
    
    @abstractmethod
    def create_deck(self):
        pass


class BaseNote(ABC):
    @abstractmethod
    def create_note(self, back: str, front: str):
        pass

class BasePackage(ABC):
    @abstractmethod
    def create_package(self, deck: BaseDeck):
        pass
