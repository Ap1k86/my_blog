import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


# Получаю исходный код страницы.
def get_source_html(url):
    driver = webdriver.Chrome(
        executable_path='/home/vitalik/all_django_project/my_blog/chromedriver/chromedriver'
    )
    driver.maximize_window()

    try:
        driver.get(url=url)
        time.sleep(3)
    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


# Функция в которой буду вызывать функции.
def main():
    get_source_html(url='https://bestfish.by/product-category/akva-obitateli/akvariumnye-rybki/ ')


if main() == '__main__':
    main()


