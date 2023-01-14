# IMPORT SECTION
import time
from bs4 import BeautifulSoup
import requests

class Reddit():
    def __init__(self,url):
        self.url = url

    def make_request(self) -> str:
        """
        Makes request to the URL and returns the response.
        
        Args:
            None
        Return:
            unparsed_html (str) -> the response returned by request.get()
        """

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }                                                                   
        unparsed_html = requests.get(self.url,headers=headers)
        time.sleep(7)
        return unparsed_html.content
    

    def parse_text(self, unparsed_html: str) -> 'BeautifulSoup':
        """
        Parse the html content to BeautifulSoup object.
        
        Args:
            unparsed_html (str) -> unparsed html content
        Return:
            soup (bs4.BeautifulSoup) -> parsed html content to bs4 object
        """
        soup = BeautifulSoup(unparsed_html, "html.parser")
        return soup
    
    def store_data(self, content:str) -> None:
        """
        Opens the redditgahana.csv file and writes the content in append mode.
        
        Args:
            content (str) -> the content to be stored in file
        Return:
            None
        """

        with open("redditgahana.csv", mode="a", encoding="utf-8") as data_file:
            data_file.write(str(content))
        
    def extract_data(self, parsed_html:'BeautifulSoup') -> str:
        """
        Extracts the data from the html content and returns the required data.
        
        Args:
            parsed_html (bs4.BeautifulSoup) -> parsed html content to bs4 object.
        Return:
            data (str) -> extreacted data
        """
        thread_name = parsed_html.find('span', class_='_2wzi-W7JiZ7A6U6aFvfvSR').text
        title = parsed_html.find('h1', class_='_eYtD2XCVieq6emjKBH3m').text
        number_of_upvotes = parsed_html.find('div', class_='_23h0-EcaBUorIHC-JZyh6J').text
        comment_elem = parsed_html.find('span', class_='FHCV02u6Cp2zYL0fhQPsO')
        if comment_elem:
            number_of_comments = comment_elem.text.split(' ')[0]
        img_elem = parsed_html.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax')
        img_url = None
        if img_elem:
            img_url = img_elem['src']
        
        data = f"{thread_name},{title},{number_of_upvotes},{number_of_comments},{img_url}\n"
        return data

    def run(self):
        """
        Bot runner function.
    
        """
        unparsed_html = self.make_request()
        parsed_html = self.parse_text(unparsed_html)
        content = self.extract_data(parsed_html)
        self.store_data(content)


if __name__ == "__main__":
    myReddit = Reddit("https://www.reddit.com/r/technology/comments/10azbsj/tesla_slashes_prices_up_to_20_in_broad_bid_to/")
    myReddit.run()

