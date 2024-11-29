import requests

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

def download_audio(sound_url, file_name, audio_dir="audio", headers=headers):
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
    
    response = requests.get(sound_url, headers=headers)
    response.raise_for_status()

    file_path = os.path.join(audio_dir, f"{file_name}.mp3")
    with open(file_path, 'wb') as f:
        f.write(response.content)
    
    print(f"file saved in: {file_path}")