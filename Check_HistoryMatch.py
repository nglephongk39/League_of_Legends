
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import xlwings as xw

print('Finish importing package')

wb = xw.Book('D:\HowKTeam - Python\Learning Python\Project\Linkedin-profiles-scraping\output.csv')
sh1 = wb.sheets('output')

print('Open file finish')

start = 387
end = 400
names = sh1[f'A{start}:A{end}'].value

print('Finish gettinh the value')

URL = 'https://lmssplus.com/profile/'
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
print('Finish open the Chrome')
sleep(3)
for index in range(len(names)):
    driver.get(URL+names[index])
    sleep(2)
    try: 
        history = driver.find_element_by_xpath('//*[@id="profileSection2"]/div/div[2]/div[2]/div/div[1]/div[1]/div[5]')
        sh1[f'G{index + start}'].value = history.text
    except:
        sh1[f'G{index + start}'].value = 'Not Value'

print('Finish')
