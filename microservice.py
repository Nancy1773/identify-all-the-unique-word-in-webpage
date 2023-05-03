import requests
from bs4 import BeautifulSoup
import re
import json

def count_words(url):
    # Step 1: Make an HTTP GET request
    response = requests.get(url)
    
    # Step 2: Extract the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    
    # Step 3: Clean the text
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    
    # Step 4: Convert the text to lowercase
    cleaned_text_lower = cleaned_text.lower()
    
    # Step 5: Tokenize the text into individual words
    words = cleaned_text_lower.split()
    
    # Step 6: Count the frequency of each word using a dictionary
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Step 7: Convert the dictionary to JSON format and return it
    return json.dumps(word_counts)

# If you want to print the word count on console use this.

if __name__ == '__main__':
    # replace with your desired URL
    url = 'https://www.example.com'
    word_counts = count_words(url)
    print(word_counts)

#  If you want to write the JSON output to a file instead of printing it to the console. use this.
if __name__ == '__main__':
    url = 'https://www.example.com'  # replace with your desired URL
    word_counts = count_words(url)
    with open('output.json', 'w') as f:
        f.write(word_counts)
