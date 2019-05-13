# 概要

Ubuntu 18.04LTS(Xなし)上で、
headless Chromium + Selenium で
スクリーンショットを撮るサンプル。

# Selenuim の導入 

```
sudo apt install \
 chromium-browser chromium-chromedriver \
 python3-selenium fonts-noto-cjk
```

これでサンプルプログラムを実行して
日本語が化ける場合は

```
wget --content-disposition IPAfont00303.zip http://ipafont.ipa.go.jp/old/ipafont/IPAfont00303.php
sudo unzip IPAfont00303.zip -d /usr/share/fonts/
rm IPAfont00303.zip
sudo fc-cache -fv
```

などでフォントを追加してみる。

# 注意点

python 3なのでshebangは `#!/usr/bin/env python3`

# リンク

## 参考にしたもの
- [Ubuntu 18.04LTSとchromium-browser(Headless)とpython3でSeleniumする - Qiita](https://qiita.com/tabimoba/items/4ea3404416142187e645)
- [EC2 UbuntuでGoogle Chromeをヘッドレス実行してスクリーンショットを採取する手順 - Qiita](https://qiita.com/shinsaka/items/37436e256c813d277d6d)
- [ゼロからはじめるPython(49) Pythonでブラウザ自動操縦してカード明細を自動でダウンロードしよう(その1) | マイナビニュース](https://news.mynavi.jp/article/zeropython-49/)
- [java - Headless chrome + ignore-certificate-errors - Stack Overflow](https://stackoverflow.com/questions/45510973/headless-chrome-ignore-certificate-errors)

## 公式など
- [7. WebDriver API — Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains)

