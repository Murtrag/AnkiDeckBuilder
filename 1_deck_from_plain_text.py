import os
import json
import genanki
import requests
from time import sleep
from strategies.dutch_strategy import DutchAudio
headers = {
    "Host": "voice.reverso.net",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5",
    "Accept-Language": "en-US,en;q=0.5",
    "Range": "bytes=0-",
    "Referer": "https://dictionary.reverso.net/",
    "Cookie": "experiment_context_1aYp6zfa1=0; rumjs.geoloc.c=nl; didomi_token=eyJ1c2VyX2lkIjoiMTkyOGQ0ZTQtZDAxZC02NmMzLWEwNzItZjgwMGI3YTUxYmEyIiwiY3JlYXRlZCI6IjIwMjQtMTAtMTRUMjM6MTI6NTEuOTY5WiIsInVwZGF0ZWQiOiIyMDI0LTEwLTE0VDIzOjEyOjUzLjA5NFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpnb29nbGVhbmEtbTIyS1RwM1kiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiJdfSwidmVuZG9yc19saSI6eyJlbmFibGVkIjpbImdvb2dsZSJdfSwidmVyc2lvbiI6MiwiYWMiOiJBRm1BQ0FGay5BRm1BQ0FGayJ9; euconsent-v2=CQGe7YAQGe7YAAHABBENBLFgAP_gAEPgAAAAKhNV_G__bWlr8X73aftkeY1P9_h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3bBIQNlGJDUTVCgaogVryDMaEyUoTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vr991dx2B-t7dr83dzyy4VHn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_rE2_eT1l_tWvp7D9-cts7_XW89_fff_9Ln_-uB_-_3_sFQACTDQqIAywJCQg0DCCBACoKwgIoEAAAAJA0QEAJgwKdgYBLrCRACAFAAMEAIAAQZAAgAAAgAQiACAAoEAAEAgUAAYAEAwEABAwAAgAsBAIAAQHQMUwIIBAsAEjMiIUwIQgEggJbKhBIAgQVwhCLPAIgERMFAAAAAAVgACAsFgcSSAlQkECXEG0AABAAgEEABQgk5MAAQBmy1B4Mm0ZWmAaPmCRDTAMgCIAA.f_wACHwAAAAA; experiment_dictionary_1a3jFD0a1=1; reverso.net.LanguageInterface=en; reverso.net.dir=eng-dut; experiment_translator_1aPYai1a1=1; reverso.net.dapp-promo3=2; reverso.net.promoCm=1",
    "Sec-Fetch-Dest": "audio",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "Accept-Encoding": "identity",
    "Priority": "u=4"
}
# from googletrans import Translator

# Define the name of the new deck
# This should read folder with user generated .txt files
file_with_plain_text = input('Input file name:\n') 
deck_name = input('Output deck name:\n')
audio_dir = "audio"


# Create a new deck model
deck_model = genanki.Model(
    1607392319,
    'Simple Model',
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
    ])

# Create a new deck
deck = genanki.Deck(
    2059417507,
    deck_name)

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
        prefix, *front = front.split(" ")
        front = " ".join(front)
        da = DutchAudio(front)
        sound_url = da.get_audio_url()
        front_html = f'<span style="color: rgb(0, 0, 255);"><b>{prefix} {front}</b></span><br>\
        [sound:{front}.mp3]\
        '
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)
        r = requests.get(sound_url, headers=headers)
        with open(f'{audio_dir}/{front}.mp3', 'wb') as f:
            f.write(r.content)
    except Exception as e:
        print(f'skipped: {e}')
        continue
    note = genanki.Note(
        model=deck_model,
        fields=[
            front_html,
            back
            ])
    deck.add_note(note)

deck_package = genanki.Package(deck)

for root, dirs, files in os.walk(audio_dir):
    for file in files:
        if file.endswith(".mp3"):
            deck_package.media_files.append(os.path.join(root, file))

deck_package.write_to_file(f'{deck_name}.apkg')
