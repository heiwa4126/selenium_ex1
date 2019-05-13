
Ubuntu 18.04LTS

sudo apt install \
 chromium-browser chromium-chromedriver \
 python3-selenium fonts-noto-cjk

これでサンプルプログラムを実行して
日本語が化ける場合は

wget --content-disposition IPAfont00303.zip http://ipafont.ipa.go.jp/old/ipafont/IPAfont00303.php
sudo unzip IPAfont00303.zip -d /usr/share/fonts/
rm IPAfont00303.zip
sudo fc-cache -fv

などでフォントを追加してみる


注意点:

python 3


<https://qiita.com/tabimoba/items/4ea3404416142187e645>
<https://qiita.com/shinsaka/items/37436e256c813d277d6d>
<https://stackoverflow.com/questions/45510973/headless-chrome-ignore-certificate-errors>
