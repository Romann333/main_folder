import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import csv

# headers = {"accept": "text/css,*/*;q=0.1", 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'

# }

# fund_links = {}
# people_id = []
# for page in range(0, 100, 10):    
#     gfs = requests.get(f'https://project-valentine-api.herokuapp.com/investors?page%5Blimit%5D=10&page%5Boffset%5D={page}',
#     headers=headers
#     )
   
#     s = gfs.json()
      
#     for i in s['data']:
#         temp = 'https://connect.visible.vc/investors/' + i['attributes']['slug']
#         name = i['attributes']['name']
#         fund_links[name] = temp
#         count_id = len(i['attributes']["person-ids"])
#         people_id.append(count_id)


# with open("all_links3.json", "w") as file:
#     json.dump(fund_links, file, indent=4, ensure_ascii=False)
        
with open("all_links.json") as file:
    all_links = json.load(file) 

with open('result.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow((
        'Name of investor',
        'Site',
        'Info card',
        'Stage',
        'Check size',
        'Focus',
        'Investment geography',
        'Maneger name',
        'Role',
        'Contact',
        'Maneger name', 'Role', 'Contact', 'Maneger name', 'Role', 'Contact', 'Maneger name', 'Role', 'Contact',
        'Maneger name', 'Role', 'Contact', 'Maneger name', 'Role', 'Contact', 'Maneger name', 'Role', 'Contact',
        'Maneger name', 'Role', 'Contact', 'Maneger name', 'Role', 'Contact', 'Maneger name', 'Role', 'Contact'       
        
    ))


def get_data_with_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        driver = webdriver.Chrome(
            executable_path="/home/roman/python_course/Selenium_Python/Chrome_ driver/chromedriver",
            options=options
         )
   
        for name_fond in all_links: 

            try:
                driver.get(url=all_links[name_fond])
                time.sleep(5)

                # with open('var.html', 'w') as file:
                #     file.write(driver.page_source)

                # with open('var.html') as file:
                #     src = file.read()

                soup = BeautifulSoup(driver.page_source, 'lxml')
                print(all_links[name_fond])
                m_n =[]
                m_r = []
                m_l = []

                link = soup.find(class_='mr-2 text-sm leading-tight text-orange-600 hover:underline').get('href').strip(' ')          
                stage = soup.find(string=re.compile('Stage')).find_next('span').text.replace('\n', '').replace(' ', '')
                check = soup.find(string=re.compile('Check size')).find_next('span').text.replace('\n', '').replace(' ', '')
                focus = soup.find(string=re.compile('Focus')).find_next('span').string.replace(' ', '').replace(',', ', ').strip('\n ')
                i_geo = soup.find(string=re.compile('Investment geography')).find_next('span').text.strip(' ').replace('\n', '')
                
                m_name = soup.find_all(class_='font-serif text-base text-black truncate')
                for i in m_name:
                    m_n.append(i.text.strip('\n '))
                
                m_role = soup.find_all(class_='text-xs text-gray-500 truncate')
                for i in m_role:
                    m_r.append(i.text.strip('\n ') if i.text.strip('\n ') != '' else 'No information')
                
                m_links = soup.find_all(class_='flex items-center px-2 py-3 text-sm bg-white border border-gray-300 max-w-sm')
                for i in m_links:
                    tmp = ''
                    for e in i.find_all('a'):
                        tmp += e.get('href') + '\n'
                    m_l.append(tmp.strip('\n') if tmp.strip('\n') != '' else 'No information')    

                add_row_to_csv = [ 
                    name_fond,
                    (link if link != '' else 'No information'),
                    all_links[name_fond],
                    (stage if stage != '' else 'No information'),
                    (check if check != '-' else 'No information'),
                    (focus if focus != '' else 'No information'),
                    (i_geo if i_geo != '' else 'No information')
                    ]

                for i in range(10):
                    try:
                        add_row_to_csv.append(m_n[i])
                        add_row_to_csv.append(m_r[i])
                        add_row_to_csv.append(m_l[i])
                    except: 
                        add_row_to_csv.append('No information')
                        add_row_to_csv.append('No information')
                        add_row_to_csv.append('No information')
              
                print(link)

                with open('result.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(add_row_to_csv)
          
        
                   
            except Exception as ex:
                print(ex)

        
    
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()

def main():
    get_data_with_selenium()


if __name__ == '__main__':
    main()