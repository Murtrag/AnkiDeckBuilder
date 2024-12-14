import requests
from typing import List
from bs4 import BeautifulSoup
from .interface import BaseImage

class GoogleImages(BaseImage):
    def __init__(self, text: str):
        super().__init__(text)
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    def is_https(self, url: str) -> bool:
        pattern = r"^https://"
        return re.match(pattern, url) is not None

    def scrape_google_images(self, query: str, num_images: int = 10) -> List[str]:
        query = query.replace(' ', '+')
        url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            images = []
            for img in soup.find_all("img")[:num_images]:
                src = img.get("src", "")
                if self.is_https(src):
                    images.append(src)
            return images
        else:
            print(f"Error: {response.status_code}")
            return []

    def get_image_urls(self, num_images: int = 10) -> List[str]:
        return self.scrape_google_images(self._text, num_images=num_images)