#  Go to dara site for a specific product
# fetch it's current price
# write that price to a file every 60 s

# reuest the dara product page using reuests module
# parse the html string using bs4
# find the element that contains the price
# convert the price into integer
# write the price in a file


# importing reuired modules
import requests
import bs4
import datetime

def send_request(web_url:str) -> str:
    return requests.get(web_url).text

def parse_html_string(html_str: str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(html_str, 'html.parser')
    return soup

# def fetch_data(parsed_html:bs4.BeautifulSoup) -> str:
#     ...

#     output = (product_name, price)
#     return output

def get_price_from_string(soup: bs4.BeautifulSoup) -> float:
    price_element = soup.find('span', class_ = "price-wrapper")
    nepali_price = price_element.span.string

    return nepali_price

def write_price_to_file(price: float, filename):
    with open(filename, mode='w', encoding="utf-8") as file:
        file.write(price)

def main():
    web_url = "https://www.sastodeal.com/baltra-sensible-plus-electric-2-burner-infrared-cooker-bic-126-supply-baltra-09.html"
    file_path = "price_list.txt"

    html_str = send_request(web_url)
    soup = parse_html_string(html_str)

    price = get_price_from_string(soup)
    write_price_to_file(price, file_path)



if __name__ == "__main__":
    main()



    # datetime.now()  -> Current time
    # datetime.strftime('%Y)  -> convets time to str