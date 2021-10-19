import json
import html
import requests
import random


def main():
    url = 'https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand'
    response = json.loads(requests.get(url).text)
    response = random.choice(response)
    quote = html.unescape(response['content']['rendered'])
    quote = quote[3:-5]
    print(quote)

if __name__ == '__main__':
    main()
