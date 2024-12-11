import sys
import os
from time import sleep
from strategies.dutch_strategy import DutchAudio, DutchPodAudio
from factories import SimpleDeckModel, SimpleDeck, SimpleNote, SimplePackage
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Define the name of the new deck
# This should read folder with user generated .txt files
# file_with_plain_text = input('Input file name:\n') 
file_with_plain_text = "user_raw_list/lesson_1.txt" 
# deck_name = input('Output deck name:\n')
deck_name = "lesson_1"


# Create a new deck model
deck_model = SimpleDeckModel().create_deck_model()

# Create a new deck
deck = SimpleDeck(2059417507, deck_name).create_deck()

# Create notes
with open(file_with_plain_text, 'r') as file:
    for line in file:
        # Time delay to not anger scraped websites
        sleep(10) 
        try:
            front, back = line.strip().split(' : ')
            front = front.lower()
            back = back.lower()
        except ValueError as e:
            print(f"Skipped line due to error: {e} | Line content: {line.strip()}")
            continue
        
        # Create note
        note = SimpleNote().create_note(deck_model, DutchPodAudio, front, back)
        deck.add_note(note)

# Generate package
package = SimplePackage().create_package(deck)

# Save deck
package.write_to_file(f'{deck_name}.apkg')

def main():
    # Call the main logic here
    pass

if __name__ == "__main__":
    main()
