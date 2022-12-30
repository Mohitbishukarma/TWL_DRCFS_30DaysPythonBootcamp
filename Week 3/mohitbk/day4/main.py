import bs4
import requests

def send_request(web_url:str) -> str:
    return requests.get(web_url).text

def parse_str(unparsed_str: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(unparsed_str,'html.parser')

def main():
    url = ""



# .text -> unicode
# .content -> bytes