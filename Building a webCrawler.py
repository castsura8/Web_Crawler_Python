import requests


from bs4 import BeautifulSoup


#a webcrawel is a package that allows you to grab links and other web stuff to your application


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xcars.TRS0&_nkw=cars&_sacat=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
       #err =  BeautifulSoup('features="html.parser"')


        for link in soup.findAll('a', {'class': 's-item__link'}):

            title = link.string
            href = "https://www.ebay.com" + link.get('href')
            print(href)
            print(title)

        #get_single_item_data(href)


page =+1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'notranslate'}):
        print (item_name.string)
    for link in soup.findall('a'):
        href = "https://www.ebay.com" + link.get('href')
        print(href)







trade_spider(3)

