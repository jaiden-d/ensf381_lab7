import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"

print("\n\n____\n")

headers = {
    "User-Agent": "lab07-web-analyzer"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser') 
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

print("\n")


all_headings = soup.find_all(['h1','h2','h3','h4','h5','h6'])
heading_count = len(all_headings)
print(f"Number of headings in the HTML content: {heading_count}\n")

links_count = len(soup.find_all('a'))
print(f"Number of links in the HTML content: {links_count}\n")

p_count = len(soup.find_all('p'))
print(f"Number of paragraphs in the HTML content: {p_count}\n")


text_content = soup.get_text()
text_content = text_content.lower()
import re
words = re.findall(r'\b\w+\b', text_content)
from collections import Counter
word_counts = Counter(words)
most_common_words = word_counts.most_common(5)
print("Most common words in the HTML content and their counts: \n")
for word, count in most_common_words:
    print(f"{word}: {count}")
print("\n")


word = input("Enter a word to search for: ").lower()
count = word_counts.get(word)
print(f"The word '{word}' appears {count} times in the HTML content.\n")


paragraphs_text = []
for p in soup.find_all('p'):
    text = p.get_text().strip()
    if 5 <= len(text):
        paragraphs_text.append(p.get_text())
longest_paragraph = max(paragraphs_text, key=len)
print(f"The longest paragraph has length: {len(longest_paragraph)}")
print(f"Longest paragraph: {longest_paragraph}\n")


import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [heading_count, links_count, p_count]
plt.bar(labels, values)
plt.title('Group#17')
plt.ylabel('Count')
plt.show()