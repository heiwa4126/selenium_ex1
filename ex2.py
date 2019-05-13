#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111
"""
Selenium example

Yahoo!Japanのトップページから"selenium"を検索し
スクリーンショットを撮る。
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    """main"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1024,768")
    # options.add_argument("--ignore-certificate-errors")

    driver = webdriver.Chrome(
        executable_path="/usr/lib/chromium-browser/chromedriver",
        chrome_options=options)
    driver.implicitly_wait(60)

    driver.get("https://www.yahoo.co.jp/")

    driver.find_element_by_css_selector("#srchtxt").send_keys("selenium")
    driver.find_element_by_css_selector("#srchbtn").click()

    driver.save_screenshot("./screenshot2.png")
    driver.close()


if __name__ == "__main__":
    main()
