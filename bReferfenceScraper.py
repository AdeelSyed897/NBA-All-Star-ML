from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

#setting up the webdriver
driver = webdriver.Chrome()
print("Starting...")

#opening the website
driver.get("https://www.basketball-reference.com/leagues/NBA_2024_per_game.html")

#letting the elements load
time.sleep(3)

print("Loaded Website.")

#connecting to beauitful soup
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


table = soup.find("table",{"id":"per_game_stats"})


#all of the table rows
rows = table.find_all("tr")
print("Found rows")

def convRow(row):
    convRow = []
    for elem in row:
        convRow.append(elem.text.strip())
    return convRow


with open('stats.csv', 'w', newline='') as file:
    print("opened file")
    writer = csv.writer(file)
    for row in rows:
        row_content = row.find_all("td")
        try:
            row_content[0]
            print(convRow(row_content))
            writer.writerow(convRow(row_content))
            print("Wrote in row")
        except:
            print("Empty")



'''
for row in rows:
    print("In loop")
    row_content = row.find_all("td")
    print("Row content:")
    print()
    try:
        print(row_content[0].text.strip())
    except:
        print("This is row content", row_content)
    for elem in row_content:
        print(elem.text.strip())
    input()
'''

driver.quit()