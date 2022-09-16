# cyber talents 
# chellenge url : https://cybertalents.com/challenges/web/sonic-go-brrr
# Level:easy
import requests
import base64
import urllib
import re
url = "http://wcamxwl32pue3e6m5l3n94wbq36omdvww87yc1v5-web.cybertalentslabs.com/index.php"

r = requests.Session()
r.get(url)
cookies = base64.b64decode(urllib.parse.unquote(r.cookies['secret'])).decode("ascii")
data = {"Q": cookies}
flag = r.post(url, data=data)
print("".join(re.findall('<span filter-content="S">(.*?)</span>',flag.text)))
r.close()