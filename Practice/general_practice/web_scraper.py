import requests
from bs4 import BeautifulSoup


def fetch_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []
    for item in soup.find_all('h2', {'data-testid': 'card-headline'}):
        headlines.append(item.get_text(strip=True))

    return headlines


def display_headlines(headlines):
    if not headlines:
        print("No headlines found.")
        return

    print("Latest News Headlines:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")


def main():
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)
    display_headlines(headlines)


if __name__ == "__main__":
    main()
