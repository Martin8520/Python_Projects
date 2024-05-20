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


def filter_headlines(headlines, keyword):
    if keyword:
        keyword = keyword.lower()
        filtered_headlines = [headline for headline in headlines if keyword in headline.lower()]
        return filtered_headlines
    return headlines


def display_headlines(headlines):
    if not headlines:
        print("No headlines found.")
        return

    print("Filtered News Headlines:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")


def main():
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)

    keyword = input("Enter a word or words to filter headlines (leave empty to show all): ").strip()

    filtered_headlines = filter_headlines(headlines, keyword)
    display_headlines(filtered_headlines)


if __name__ == "__main__":
    main()
