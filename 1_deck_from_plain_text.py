from time import sleep
from strategies.dutch_strategy import DutchAudio
from factories import SimpleDeckModel, SimpleDeck, SimpleNote, SimplePackage

# Define the name of the new deck
# This should read folder with user generated .txt files
file_with_plain_text = input('Input file name:\n') 
deck_name = input('Output deck name:\n')


# Create a new deck model
deck_model = SimpleDeckModel().create_deck_model()

# Create a new deck
deck = SimpleDeck(2059417507, deck_name).create_deck()

with open(file_with_plain_text, 'r') as file:
    words = file.read()

words_lines = words.split('\n')
for line in words_lines:
    sleep(10)
    try:
        front, back = line.split(' : ')
        front = front.lower()
        back = back.lower()
        # sound_url = f'https://diki.pl/images-common/en/mp3/{front}.mp3'

    except Exception as e:
        print(f'skipped: {e}')
        continue
    # Create note
    note = SimpleNote().create_note(deck_model, DutchAudio, front, back)
    deck.add_note(note)

# Generate package
package = SimplePackage().create_package(deck)

package.write_to_file(f'{deck_name}.apkg')
