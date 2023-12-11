# from bs4 import BeautifulSoup as BS
# import requests

# def get_html(url):
#     response = requests.get(url)
#     if requests.status_code== 200:
#         return requests.text
#     return None




# def get_data(html):
#     soup = BS(html, 'html.parser')
#     print(soup)

# def main():
#     URL = 'https://www.house.kg/kupit-uchastok?region=1&town=2&sort_by=upped_at+desc'
#     html = get_html(URL)


# if __name__ =='__name__':
#     main()  
from bs4 import BeautifulSoup as  BS
import requests


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None


def get_data(html):
    soup = BS(html, 'html.parser')
    container = soup.find('div', class_= 'container body-container')
    main = container.find('div', class_ = 'main-content')
    wrapper = main.find('div', class_ = 'listings-wrapper')
    post = wrapper.find_all('div',class_ = 'listing')
    for i in post:
        left_side = i.find('div', class_ = 'left-side')
        title = left_side.find('p', class_ = 'title')
        address = left_side.find('div', class_ = 'address')
        link = left_side.find('a').get('href')
        full_link = f'https://www.house.kg{link}'
        right_side = i.find('div', class_ = 'right-side')
        span = i.find('span', class_='dealer-name') 
        desc = i.find('div',class_='description')
        info = i.find('div',class_='additional-info').find('div')
        view = info.find('span',{"data-placement":"top"}).text.strip()
        sorted_view = sorted(view)
        print(sorted_view)
        print(f'Просмотры:{view}')
        # print(view.text)
        # print(info.text.strip())
        # print(desc)
        # print(full_link)
        # print(title.text.strip())
        # print(address.text.strip())

def main():
    URL = 'https://www.house.kg/kupit-uchastok?region=1&town=2&sort_by=upped_at+desc'
    html = get_html(URL)
    get_data(html)
    
    
if __name__ == '__main__':
    main()


