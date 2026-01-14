from bs4 import BeautifulSoup
import urllib.request

WPM = 260  # average adult reading speed

def get_word_count(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for tag in soup(["script", "style", "noscript", "header", "footer", "aside"]):
        tag.decompose()

    text = soup.get_text()
    words = text.split()
    return len(words)

def calculate_reading_time(url):
    return get_word_count(url) / WPM

url = ("https://www.diggitmagazine.com/articles/pastafarianism-true-religion-or-bunch-satirical-noodles")

word_count = get_word_count(url)
reading_time = calculate_reading_time(url)

print(f"Word count: {word_count}")
print(f"estimated reading time: {reading_time:.2f} minutes")
