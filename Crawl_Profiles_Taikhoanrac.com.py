
import requests
from bs4 import BeautifulSoup
import xlwings as xw
from time import sleep
import csv




class Account:
        ingame = ''
        Price = ''
        URL = ''
        Rank = ''
        Champ = ''
        Skin = ''
        History = ''


list_account = []
variableName = Account()

PAGEs = 159
for page in range(1,PAGEs+1):

        sleep(2)

        usr_agent = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/61.0.3163.100 Safari/537.36'}
        Website = f'https://taikhoanrac.com/?page={page}'

        r = requests.get(Website, headers=usr_agent)

        r.encoding = 'utf-8' #Chuyển đổi mã hóa mặc định 'ISO-8859-1' thành 'UTF - 8'

        soup = BeautifulSoup(r.text, 'html.parser')\

        questions= soup.find_all('div', {'class' : 'sl-prodli'})

        # questions_ranks_skin_champ = soup.find_all('div', {'class' : 'sl-prifbot'})


        for rank_skin_champ in questions:
                variableName = Account()
                variableName.Skin = rank_skin_champ.find('ul').text.strip('\n').split('\n')[2][12:] #Skin
                if int(variableName.Skin) > 130:
                        variableName.Price = rank_skin_champ.find('span', {'class' : 'sl-prpri sl-prpri2'}).text[:len(variableName.Price)-1] #Price
                        if int(variableName.Price[:len(variableName.Price)-4]) <= 18:
                                variableName.ingame = rank_skin_champ.find('span' , {'class' : 'sl-lpcode'}).text[9:] #Ingame
                                variableName.Rank = rank_skin_champ.find('ul').text.strip('\n').split('\n')[0][6:] #Rank
                                variableName.Champ = rank_skin_champ.find('ul').text.strip('\n').split('\n')[1][7:] #Champ
                                variableName.URL = 'https://taikhoanrac.com/'+ rank_skin_champ.find('a', {'class' : 'sl-prlinks'})['href'] #URL

                                list_account.append(variableName)


        with open('output.csv', mode ='w', encoding='utf-8-sig', newline = '') as file_output:
                headers = ['Ingame', 'Price', 'Rank', 'Champ', 'Skin', 'URL']
                writer = csv.DictWriter(file_output, fieldnames=headers)
                writer.writeheader()
                for i in list_account:
                        writer.writerow({headers[0]:i.ingame, headers[1]:i.Price, headers[2]:i.Rank, headers[3]:i.Champ, headers[4]:i.Skin, headers[5]:i.URL})

        print(f'Finish page {page}')





        












