#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111
"""
Selenium example

Yahoo!Japanのトップページを取得し
- body要素を標準出力する
- トップページのスクリーンショットを撮る

original code:
<https://qiita.com/tabimoba/items/4ea3404416142187e645>
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    """main"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1024,768")
    # options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(
        executable_path="/usr/lib/chromium-browser/chromedriver",
        chrome_options=options)
    driver.implicitly_wait(600)

    setup_url = "https://www.yahoo.co.jp/"
    driver.get(setup_url)
    print(driver.find_element_by_xpath("//body").text)

    driver.save_screenshot("./screenshot1.png")

    driver.close()


if __name__ == "__main__":
    main()
