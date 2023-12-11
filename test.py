from bs4 import BeautifulSoup as BS
with open('test.html', encoding='utf-8') as file:
    html = file.read()

soup = BS(html, 'html.parser')   

container = soup.find('div',class_='container')

navigation = container.find('div',class_='navigation')
list =navigation.find ('ul' ,class_='list')
li = list.find_all ('ul')

content = container.find('div',class_='content  ')
post = container.find('div',class_= 'post')
h2 = post.find_all('h2', class_='title')
for item in h2:
    print(item.text.strip())

# content= container.find('div', class_ ='content')
# title = container.find('h2',class_= 'title')
# image = container.find('img',class_='img')