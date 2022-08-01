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


quotes_data = []
authors_data = []  #list of authors information

#Fetching authors information from each_pages in HTML
def making_authors_information_from_html_page(link_url):
    max_page = 2
    current_page = 1

    while current_page <= max_page:
        request_link_url = requests.get(link_url)
        soup_link_url = BeautifulSoup(request_link_url.content , "html.parser")
        #print(soup_link_url.prettify())

        author = {}
        finding_parent_element = soup.find("div" , class_="quote")
        author_row = finding_parent_element.find("span")
        author_link = finding_parent_element.find("a")['href']
        author_link_to_get_html = "http://quotes.toscrape.com" + author_link + "/"
        #print(author_link_to_get_html)

        #Fetching author information from author_link

        get_author_information = requests.get(author_link_to_get_html)
        soup_author_information = BeautifulSoup(get_author_information.content , "html.parser")
        #print(soup_author_information.prettify())


        #Finding Author Details in Author_description_link
        table_author = soup.find("div", class_="author_details")
        #print(table_author)

        current_page += 1

# Fetching quotes from next page for each_tag =>maximum pages for each_tag element having only two pages
# Here using while loop to to get the data from next page of


def scrape_page(link_url, quotes_data):

    max_pages = 2
    current_page = 1




    while current_page <= max_pages:
        current_url = f'{link_url}page/{current_page}/'
        #print(current_url)


        raw_html = requests.get(current_url)    #Fetching current HTML Content by using Get Method
        soup_raw_html = BeautifulSoup(raw_html.text,"html.parser")
        #print(soup_raw_html.prettify())



        for quotes in soup_raw_html.find_all("div" , class_="quote"):
            each_quote = dict()
            summary_quote = quotes.span.text
            #print(summary_quote)
            each_quote["quote"] = summary_quote

            author_name = quotes.select_one("small")
            #print(author_name.string)
            each_quote["author"] = str(author_name.string)


            tags = quotes.find("div" , class_="tags")
            tags_list = []
            anchor_tags = tags.find_all("a")
            for i in anchor_tags:
                tags_list.append(i.text)
            #print(tags_list)
            each_quote["tags"] = tags_list
            quotes_data.append(each_quote)
        current_page += 1




#links_url_list = []

def making_link_for_tag_elements(each_tag_element):

    link = each_tag_element.select_one('.tag-item a')["href"]
    string_link = each_tag_element.a.text
    link_url = "http://quotes.toscrape.com" + link # Fetching url for all tag elements to scrape data
    making_authors_information_from_html_page(link_url)
    scrape_page(link_url,quotes_data)



# Getting tag elements with their links to make url to fetch data in next pages => Iteration makes every tag element
# availble to make linke to extract data from HTML
for each_tag_element in tag_elements_in_html_content:
    making_link_for_tag_elements(each_tag_element)

print(quotes_data)