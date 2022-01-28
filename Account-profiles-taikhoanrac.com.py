
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import csv



class account:
    ingame = ''
    Price = ''
    URL = ''
    Rank = ''
    Champ = ''
    Skin = ''
    History = ''


# Page URL
def URL_Page():
    URLs = "https://taikhoanrac.com/?page="
    list_URL = []
    for URL in range(12,13):
        URL = URLs + str(URL)
        list_URL.append(URL)
    return list_URL
print('- Finish URL for Page')

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
sleep(2)

list_account = []

for page in URL_Page():
    driver.get(page)
    sleep(2)
    page_source = BeautifulSoup(driver.page_source,"html.parser") #Download toàn bộ page_source của trang web
    profiles = page_source.find_all('div',class_="sl-prodli") #Tìm class trong HTML có chứa ingame
        

    for profile in profiles: #Lọc từng class và lấy ra tên ingame bằng hàm get_text()
        
        variableName = account()

        all_ = profile.find('div', class_="sl-priftop")
            #Thông tin cần tìm nằm trong <ul><ul> nên cần find 1 lần nữa đề lấy được giá trị
            #Giá trị ở đây gồm có Rank, Tướng, Trang Phục
        all_RankTuongTrangPhuc = all_.find('ul').get_text()

        
        if int(all_RankTuongTrangPhuc.strip('\n').split('\n')[2][12:]) > 130:
            variableName.Rank = all_RankTuongTrangPhuc.strip('\n').split('\n')[0][6:]
            variableName.Champ = all_RankTuongTrangPhuc.strip('\n').split('\n')[1][7:]
            variableName.Skin = all_RankTuongTrangPhuc.strip('\n').split('\n')[2][12:]

            ### Giá Bán
            gia_ban = profile.find('span', class_="sl-prpri sl-prpri2").get_text()
             
            if int(gia_ban[:len(gia_ban)-5]) <= 18:
                variableName.Price = gia_ban[:len(gia_ban)-1]

                ### Ingame

                ingame = profile.find('span', class_="sl-lpcode").get_text()
                ingame = ingame[9:]
                variableName.ingame = ingame

                ### URL
                URL = profile.find('a', class_="sl-prlinks").get('href')
                URL = 'https://taikhoanrac.com' + URL
                variableName.URL = URL

                list_account.append(variableName)

                print(list_account)
        # with open('output.csv', mode ='w', encoding='utf-8-sig', newline = '') as file_output:
        #     headers = ['Ingame', 'Price', 'Rank', 'Champ', 'Skin', 'URL']
        #     writer = csv.DictWriter(file_output, fieldnames=headers)
        #     writer.writeheader()
        #     for i in list_account:
        #         writer.writerow({headers[0]:i.ingame, headers[1]:i.Price, headers[2]:i.Rank, headers[3]:i.Champ, headers[4]:i.Skin, headers[5]:i.URL})


driver.quit()

print('Finish !!!')


