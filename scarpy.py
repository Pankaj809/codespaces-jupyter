"""
This module provides a set of utility functions for working with strings.

Functions:
- count_chars(s: str) -> int: Returns the number of characters in a string.
- capitalize_first_letter(s: str) -> str: Capitalizes the first letter of a string.
- ...
"""
import requests
from bs4 import BeautifulSoup
URL = "https://www.nytimes.com/"
Response = requests.get(URL, timeout=10)
Soup = BeautifulSoup(Response.content, "html.parser")

titles = []
for article in Soup.find_all("article"):
    title = article.find("h2", {"class": "css-1j9dxys e1voiwgp0"}).get_text().strip()
    titles.append(title)

print(titles)
print("Completed")
