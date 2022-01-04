from openpyxl import Workbook as wb
import requests
from bs4 import BeautifulSoup as bs


excel = wb()
sheet = excel.active
sheet.title = 'WAY UP INTERNSHIPS ECON'
column_names = sheet.append(['Company', 'Location', 'Position', 'Link'])

web = requests.get('https://www.wayup.com/s/internships/economics/new-york-ny/').text
soup = bs(web, 'lxml')
for x in soup.find_all('div', class_ ='sc-iCoHVE RjEGt'):
    name = x.find('div', class_ ='sc-gtssRu dWMURV').text.upper() 
    location = x.find('div', class_ ='sc-gtssRu dfQMYO').text
    position = x.find('h3', class_ ='sc-fujyUd iohUvv').text.replace('','')
    links = soup.find('div', class_ ='sc-iCoHVE RjEGt').a['href'] # The "a" is in the 'div' link that's why we use "soup" not "x"
    print(f"Name: {name}")
    print(f'Location: {location}')
    print(f"Position: {position}")
    print(f"Link: {links.strip()} \n")
    sheet.append([name, location, position, links.strip()])
excel.save('WAY UP.xlsx')


    

    