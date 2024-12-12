import requests
from bs4 import BeautifulSoup
import base64
from .interface import BaseAudio

class DutchAudio(BaseAudio):
    def __init__(self, text: str):
        super().__init__(text)
        self._voice = 'Femke22k'
        self._speed = '80'
        self.headers = {
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

    def get_audio_url(self):
        base_url = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream"
        encoded_text = base64.b64encode(self._text.encode("utf-8")).decode("utf-8")
        url = f"{base_url}/voiceName={self._voice}?voiceSpeed={self._speed}&inputText={encoded_text}"
        return url
    
    
class DutchPodAudio(BaseAudio):
    def __init__(self, text: str):
        super().__init__(text)
        self._url = "https://www.dutchpod101.com/learningcenter/reference/dictionary_post"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Priority": "u=0"
        }
        self._referrer = "https://www.dutchpod101.com/dutch-dictionary/"

    def get_audio_url(self) -> str:
        payload = {
            "post": "dictionary_reference",
            "search_query": self._text
        }
        response = requests.post(
            self._url, 
            data=payload, 
            headers={**self.headers, "Referer": self._referrer}
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data: {response.status_code}")
        
        soup = BeautifulSoup(response.text, "html.parser")
        source_tag = soup.select_one("audio source")
        
        if not source_tag or not source_tag.get("src"):
            print(response.text)
            raise Exception("Audio URL not found in the response.")
        
        return source_tag["src"]