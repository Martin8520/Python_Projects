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
        headline = item.get_text(strip=True)
        link = item.find_parent('a')['href']
        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link
        headlines.append((headline, link))

    return headlines


def filter_headlines(headlines, keyword):
    if keyword:
        keyword = keyword.lower()
        filtered_headlines = [headline for headline in headlines if keyword in headline[0].lower()]
        return filtered_headlines
    return headlines


def display_headlines(headlines):
    if not headlines:
        print("No headlines found.")
        return

    print("Filtered News Headlines:")
    for i, (headline, link) in enumerate(headlines, 1):
        print(f"{i}. {headline}")
        print(f"   Link: {link}")


def main():
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)

    keyword = input("Enter a word or words to filter headlines (leave empty to show all): ").strip()

    filtered_headlines = filter_headlines(headlines, keyword)
    display_headlines(filtered_headlines)


if __name__ == "__main__":
    main()
