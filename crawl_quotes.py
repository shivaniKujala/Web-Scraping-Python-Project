import requests
from bs4 import BeautifulSoup

#Fetch HTML content using url
url = "http://quotes.toscrape.com/"
request = requests.get(url)
html_content = request.content

#Parsing HTML content using BeautifulSoup which converts into Python objects

soup = BeautifulSoup(html_content,"html.parser") #Converting into Parsed HTML

#print(soup.prettify())

#Fetching anchor tags of quotes
tag_elements_in_html_content = soup.find_all("span", class_ = "tag-item")


data = []   #A list to store quotes

# Fetching quotes from next page for each_tag =>maximum pages for each_tag element having only two pages
# Here using while loop to to get the data from next page of each_tag
def scrape_page(link_url):
    max_pages = 2
    current_page = 1

    while current_page <= max_pages:
        current_url = f'{link_url}page/{current_page}/'
        #print(current_url)

        raw_html = requests.get(current_url)    #Fetching current HTML Content by using Get Method
        soup_raw_html = BeautifulSoup(raw_html.text,"html.parser")
        #print(soup_raw_html.prettify())

        for quotes in soup.find_all("div" , class_="quote"):
            summary_quote = quotes.span.text
            #print(summary_quote)

            author_name = quotes.select("small")
            #print(author_name)

            tags = quotes.find("div" , class_="tags")
            anchor_tags = tags.find_all("a")
            #for i in anchor_tags:
                #print(i.text)

        current_page += 1



#
def making_link_for_tag_elements(each_tag_element):
    link = each_tag_element.select_one('.tag-item a')["href"]
    string_link = each_tag_element.a.text
    link_url = "http://quotes.toscrape.com" + link # Fetching url for all tag elements to scrape data
    #print(link_url)
    scrape_page(link_url)



# Getting tag elements with their links to make url to fetch data in next pages => Iteration makes every tag element
# availble to make linke to extract data from HTML
for each_tag_element in tag_elements_in_html_content:
    making_link_for_tag_elements(each_tag_element)