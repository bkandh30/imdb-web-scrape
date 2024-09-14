import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.imdb.com/chart/top/"

driver.get(url)

time.sleep(5)

webpage = driver.page_source

soup = BeautifulSoup(webpage, 'html.parser')

driver.quit()

movies = soup.find_all('li', class_='ipc-metadata-list-summary-item')
data = []

for movie in movies:
    title = movie.find('h3', class_='ipc-title__text').text.strip()
    year = movie.find('span', class_='cli-title-metadata-item').text.strip()
    rating = movie.find('span', class_='ipc-rating-star').text.strip()
    rating = rating.split()[0]
    watched = ""
    data.append([title, year, rating, watched])

print(len(data))
df = pd.DataFrame(data, columns=['Title', 'Year', 'Rating', "Watched"])
df.to_excel('imdb_top250.xlsx')
print("Created the excel file containing the top 250 imdb movies")