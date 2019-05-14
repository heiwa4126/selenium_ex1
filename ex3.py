#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111
"""
Selenium example
Accept-Languageヘッダを変更するテスト。

最近は
option.add_experimental_option()ではなく
option.add_option("--lang=ja")で指定できる。
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main(lang):
    """main"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1024,768")
    # options.add_argument("--ignore-certificate-errors")
    # 古い: options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    options.add_argument("--lang={}".format(lang))

    driver = webdriver.Chrome(
        executable_path="/usr/lib/chromium-browser/chromedriver",
        chrome_options=options)
    driver.implicitly_wait(60)

    setup_url = "https://www.cylog.org/headers/"
    driver.get(setup_url)

    driver.save_screenshot("./screenshot3_{}.png".format(lang))

    driver.close()


if __name__ == "__main__":
    main("en")
    main("ja")
