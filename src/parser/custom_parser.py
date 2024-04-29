import time
from termcolor import colored, cprint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

class QueryData:
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

query = QueryData("http://skelbiu.lt", "keychron")

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

accept = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept.click()

about = driver.find_element(By.ID, "searchKeyword")
about.send_keys(query.keyword)

search = driver.find_element(By.ID, "searchButton")
search.click()

time.sleep(1)

print('\nstart')

go = True
while(go == True):

    try:
        parentClassTag = "//a[@class='js-cfuser-link standard-list-item   ']"

        hrefLinks = driver.find_elements(By.XPATH, f"{parentClassTag}")
        hrefTitle = driver.find_elements(By.XPATH, f"{parentClassTag} //div[@class='title']")
        hrefContent = driver.find_elements(By.XPATH, f"{parentClassTag} //div[@class='first-dataline']")
        hrefPlace = driver.find_elements(By.XPATH, f"{parentClassTag} //div[@class='second-dataline']")
        hrefPrice = driver.find_elements(By.XPATH, f"{parentClassTag} //div[@class='price-line']")

        cprint(f"len: {len(hrefLinks)}\n", "blue", None, attrs=["bold"])

        for index, href in enumerate(hrefLinks):

            textHref = colored(f"href: {href.get_attribute('href')}", "red", attrs=["bold"])
            cprint(textHref)

            textTitle = colored(f"title: {hrefTitle[index].get_attribute('textContent')}", "blue", attrs=["bold"])
            cprint(textTitle)

            try:
                textContent = colored(f"content: {hrefContent[index].get_attribute('textContent')}", "magenta", attrs=["bold"])
                cprint(textContent)
            except:
                textContent = colored(f"no content", "magenta", attrs=["bold"])
                cprint(textContent)
            
            textPlace = colored(f"place: {hrefPlace[index].get_attribute('textContent')}", "blue", attrs=["bold"])
            cprint(textPlace)

            textPrice = colored(f"price: {hrefPrice[index].get_attribute('textContent')}", "blue", attrs=["bold"])
            cprint(textPrice)

            print()

            if (index == 1):
                break
        
        try:
            paginationTag = "//div[@id='pagination']"
            pagination = driver.find_element(By.XPATH, paginationTag)

            nextTag = "//a[@rel='next']"
            next = driver.find_element(By.XPATH, nextTag)
            next.click()

            print("#")

        except:
            print("nėra daugiau puslapių")
            go = False

    except:
        print('blogas šudas')

    time.sleep(1)