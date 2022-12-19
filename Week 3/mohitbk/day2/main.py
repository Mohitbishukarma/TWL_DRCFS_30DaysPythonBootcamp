import bs4
import requests

def send_request(website_url:str)-> str:
    # try:
    #     content = requests.get(website_url)
    # except:
    #     print(f"Error while requesting to {website_url}")
    
    return requests.get(website_url).text
def parse_html_string(html_str:str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(html_str,'html.parser')
    return soup

def fetch_current_temperature(parsed_html: bs4.BeautifulSoup)-> float:
    top_element = parsed_html.find(id="top")
    current_date = top_element.find('div',class_ = "date").span.string.removeprefix('\n')
    return current_date

def main():
    web_url = "https://www.hamropatro.com/"
    html_str = send_request(web_url)
    parsed_html = parse_html_string(html_str)
    current_temp = fetch_current_temperature(parsed_html)

    print(f"The current temp is {current_temp} for today.")
    

main()

"shf".strip()