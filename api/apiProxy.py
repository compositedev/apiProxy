from requests import get
from time import sleep

API = "https://api.ethplorer.io/getAddressInfo/0x0De845955E2bF089012F682fE9bC81dD5f11B372?apiKey=EK-gHm8Y-GuxFYSy-qoNj9"

while True:
    res = get(API)
    apiOut = res.text
    with open('apiOut.txt', 'w') as the_file:
        the_file.write(apiOut)

    print(res.content)
    sleep(5)
