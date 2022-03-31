import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Install selenium driver in case that doesn't exist
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Count fetched items
counter = 1

# page numbers you want to scrape
for page in range(1, 11):
    url = f'https://divar.ir/s/tehran/buy-apartment/parand?page={page}'
    driver.get(url)

    elements = driver.find_elements(By.CLASS_NAME, 'kt-post-card__body')
    urls = driver.find_elements(By.CLASS_NAME, 'kt-post-card')

    f = open('data.txt', 'a')

    for element, url in zip(elements, urls):
        f.write(f'{counter} --> {element.text}')
        f.write('\n')
        f.write(f'Link --> {url.get_attribute("href")}')
        counter += 1
    
    time.sleep(10)


f.close()
driver.quit()
