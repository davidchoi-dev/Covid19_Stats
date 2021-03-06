import requests 
import csv
from os import path 
from bs4 import BeautifulSoup as bs4


class CovidWorldInfo:
    def __init__(self):
        self.scrape_url = "https://www.worldometers.info/coronavirus/"
        self.datafile = f"Data/World/new_covid_dat.csv"
        
    def getData(self):
        page = requests.get(self.scrape_url)
        html = bs4(page.text, 'html.parser')
        table = html.find(id="main_table_countries")
        thead_all = table.thead.find_all('th')
        thead = [th.text for th in thead_all]
        
        tbody_all = table.find_all('tbody')
        tr_temp = [tr for tr in tbody_all[0].find_all('tr')]
        td_temp = [td.find_all('td') for td in tr_temp]
        tbody = [[j.text.strip() for j in i] for i in td_temp]
        
        return thead, tbody
        
    
    
    def inputData(self):
        thead, tbody = self.getData()
        if(path.isfile(self.datafile)==False):
            with open(self.datafile, 'w+') as file:
                cw = csv.writer(file)
                cw.writerow(thead)
                for i in tbody:
                    cw.writerow(i)
                file.close()
        else:
            with open(self.datafile, 'a') as file:
                cw = csv.writer(file)
                cw.writerow(tbody)
                file.close()
        
    # def showData(self):
    #     test = self.getData()
    #     print(test)
    
    