# from LxmlSoup import LxmlSoup
# import requests

# # html = requests.get('https://sunlight.net/catalog').text  # получаем html код сайта
# html = requests.get('https://www.skelbiu.lt/skelbimai/?autocompleted=1&keywords=keychron&cities=0&distance=0&mainCity=0&search=1&category_id=0&user_type=0&ad_since_min=0&ad_since_max=0&visited_page=1&orderBy=-1&detailsSearch=0').text  # получаем html код сайта
# soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

# print('textas')

# # print(html)

# # links = soup.find_all('a', class_='cl-item-link js-cl-item-link js-cl-item-root-link')  # получаем список ссылок и наименований
# links = soup.find_all('a', class_='js-cfuser-link standard-list-item   ')  # получаем список ссылок и наименований

# print(f"Linku: {len(links)}")

# limit = 2

# for index, link in enumerate(links):
#     url = link.get("href")  # получаем ссылку товара
#     name = link.text()  # извлекаем наименование из блока со ссылкой
#     price = soup.find_all("div", class_="cl-item-info-price-discount")[index].text()  # извлекаем цену
#     print(index)
#     print(f"Url - {url}")
#     print(f"Name - {name}")
#     print(f"Price - {price}\n")
#     if index == limit:
#         break
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

class QueryData:
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

query = QueryData("http://skelbiu.lt", "keycaps")

hide = 3
options = Options()

if (hide == 1):
    options.add_argument("--headless")
else:
    if (hide == 2):
        options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.set_window_rect(1500,0,1300,1000)

driver.get(query.url)

time.sleep(1)
print('delay 3')

accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept.click()

# time.sleep(1 )
# print('delay 1')

about = driver.find_element(By.ID, "searchKeyword")
about.send_keys(query.keyword)

# time.sleep(1)
print('delay 1')

search = driver.find_element(By.ID, "searchButton")
search.click()

time.sleep(1)

print('start')

# content = driver.page_source
# content_soup = BeautifulSoup(content, "html.parser")


go = True
while(go == True):

    try:
        # buttons = content_soup.find_all('a', class_="js-cfuser-link standard-list-item")
        # buttons = content_soup.find_all('a')
        # print(f"len: {len(buttons)}")

        # for href in buttons:
        #     print(href.getText())

        # hrefs = driver.find_elements(By.cssSelector("a[class='js-cfuser-link standard-list-item   ']"))

        parentClass = "//a[@class='js-cfuser-link standard-list-item   ']"

        hrefLinks = driver.find_elements(By.XPATH, f"{parentClass}")
        hrefTitle = driver.find_elements(By.XPATH, f"{parentClass} //div[@class='title']")
        hrefContent = driver.find_elements(By.XPATH, f"{parentClass} //div[@class='first-dataline']")

        print(f"len: {len(hrefLinks)}")

        for index, href in enumerate(hrefLinks):

            print(f"href: {href.get_attribute('href')}\ntitle: {hrefTitle[index].get_attribute('textContent')}\ncontent: {hrefContent[index].get_attribute('textContent')}")

            if (index == 3):
                break
        
        isPagination = False

        try:
            pagination = driver.find_element(By.ID, "pagination")

            isPagination = True

            print(pagination.text)

        except:
            print("nerastas pagination")
        
        if (len(hrefLinks) > 0):
            go = False

        # donate = driver.find_element(By.XPATH, "//a[contains(@class, 'donate-button')]")
        # print(donate.text)

        # span = driver.find_element(By.XPATH, "//span[contains(@class, 'icon-get-started')]")
        # print(span.get_attribute('InnerText'))
    except:
        print('blogas šudas')

    time.sleep(1)
    # if (data):
    #     print(data)
    #     go = False
    #     break




# print(f"len:{len(about)}")

# print(str(about.text))
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()