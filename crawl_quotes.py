import requests
from bs4 import BeautifulSoup

#Fetch HTML content using url
url = "http://quotes.toscrape.com/"
request = requests.get(url)
html_content = request.content

#Parsing HTML content using BeautifulSoup which converts into Python objects

soup = BeautifulSoup(html_content,"html.parser") #Converting into Parsed HTML

#print(soup.prettify())
quote_elements = soup.find_all("span", class_ = "tag-item")
#print(quote_elements)

data = []   #A list to store quotes

# Pagingation: Fetching quotes from next page also
def scrape_page(link_url):
    max_pages = 2
    current_page = 1

    while current_page <= max_pages:
        current_url = f'{link_url}page/{current_page}/'
        #print(current_url)

        raw_html = requests.get(current_url)    #Fetching current HTML Content by using Get Method
        soup_raw_html = BeautifulSoup(raw_html.text,"html.parser")
        #print(soup_raw_html.prettify())

        quotes = soup.find("div" , class_="quote")
        summary_quote = quotes.span.text
        author_name = quotes.select("small")
        tags = quotes.find("div",class_="tags")
        tag = tags.find_all('a')

        for each_tag in tag:
            print(each_tag.text)




        current_page += 1




def get_quotes_each_element(each_element):
    link = each_element.select_one('.tag-item a')["href"]
    string_link = each_element.a.text
    link_url = "http://quotes.toscrape.com" + link
    #print(link_url)
    scrape_page(link_url)




for each_element in quote_elements:
    get_quotes_each_element(each_element)