import requests
from bs4 import BeautifulSoup

def get_ladder_ads(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    ladder_ads = []

    for ad in soup.find_all("div"):
        if ad.find(string=lambda x: x and "نردبان" in x):
            text = ad.get_text(strip=True)
            if text:
                ladder_ads.append(text)

    return ladder_ads


if __name__ == "__main__":
    url = "https://divar.ir/s/tehran"
    results = get_ladder_ads(url)

    print("Ladder Ads:\n")
    for i, ad in enumerate(results, 1):
        print(f"{i}. {ad}")