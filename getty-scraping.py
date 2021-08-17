from bs4 import BeautifulSoup
import requests
from openpyxl import load_workbook

filesheet = "./web-scraping/getty-scraping/getty.xlsx"
wb = load_workbook(filesheet)
sheet = wb.active

print('Ingresa la URL')
url = input('>')
print('Ingresa una descripción')
human_description = input('>')
print('Es a color?(S/N):')
colorIn = input('>')
print(f'Procesando datos...')



def obtain_data():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')


    detalles = soup.find('section', class_='asset-details')
    editorial = detalles.find('span', class_='asset-detail__asset-id').text

    creation = detalles.find_all('div', class_='asset-detail asset-detail--collection')
    date = creation[1]
    creation_date = date.find('div', class_='asset-detail__value asset-detail__cell').text

    file_name = detalles.find('div', class_='asset-detail__value asset-detail__cell text--break').text
    
    description = soup.find('div', class_='asset-description__caption').text
    
    
    year = creation_date[-4:]
    link = url
    duration = ''
    file_type = file_name[-3:]
    name = str(f'GTTY_{editorial}_{human_description}_{year}')

    
    if colorIn == 'S':
        color = 'x'
        bn = ''
    else:
        bn = 'x'
        color = ''
    
    
    datos = [(f'{name}',f'{year}',f'{link}',f'{description}',f'{bn}',f'{color}',f'{duration}',f'{file_type}')]
    for row in datos:
        sheet.append(row)
    wb.save(filesheet)
    
    print(f'Nombre: {name}')
    print(f'Año: {year}')
    print(f'Link: {link}')
    print(f'Descripción: {description}')
    print(f'B&N: {bn}')
    print(f'Color: {color}')
    print(f'Duración: {duration}')
    print(f'Tipo: {file_type}')

if __name__ == '__main__':  
        obtain_data()
