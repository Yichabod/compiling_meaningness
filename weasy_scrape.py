from bs4 import BeautifulSoup
import requests as re
import sys
from weasyprint import HTML, CSS
import pdfkit

"""

"""

root_page = "https://meaningness.com/"
#have yet to try this for Vividness, Eggplant, B4V

intro_text = "Why meaningness?" 


def _find_intro_href_index(text, hrefs):
    """Finds the index of the first relevant page"""
    href_texts = [href.text for href in hrefs]
    return href_texts.index(text)

def write_links_to_file(links, root_page, filename="pictureless_meaningness.pdf"):
    """
    Given the relevant links, creates a large string that is then written to a pdf using weasy
    """
    container_string = ""
    for i, href in enumerate(links):
        url_suffix = href.attrs['href']
        url = root_page+url_suffix
        soup = BeautifulSoup(re.get(url).content, 'html.parser')
        for a in soup.findAll('a', href=True): #remove links which will not work
            del a['href']
        article = soup.find('article')
        big_html += str(article)

        if i % 20 == 0:
            print("{0} of {1} complete".format(i, len(hrefs)))
            time.sleep(5) #to prevent too many requests in short period

    HTML(string=big_html).write_pdf(filename)

if __name__ == "__main__":
    main_page = re.get(root_page)
    main_soup = BeautifulSoup(main_page.content, "html.parser")
    hrefs = main_soup.find_all(href=True)
    
    href_index = _find_intro_href_index(intro_text, hrefs)
    hrefs = hrefs[href_index:]

    big_html = ""
    for i, href in enumerate(hrefs):
        url_suffix = href.attrs['href']
        url = root_page+url_suffix
        try: #in case too many requests
            soup = BeautifulSoup(re.get(url).content, 'html.parser')
        except re.exceptions.ConnectionError:
            print("connection refused for", url)
            continue

        for a in soup.findAll('a', href=True): #remove links which will not work
            del a['href']

        article = soup.find('article')
        big_html += str(article)
        
        if i % 20 == 0:
            print("{0} of {1} complete".format(i, len(hrefs)))
            time.sleep(5) #to prevent too many requests in short period
            

    HTML(string=big_html).write_pdf('pictureless_meaningness.pdf')
# try this approach: https://github.com/chsasank/paul-graham-essays-ebook/blob/main/scrape.ipynb
