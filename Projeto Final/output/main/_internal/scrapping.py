import requests
from lib_classes import Slip

import json

url = "https://api.adviceslip.com/advice"

def scrapping_func(numb_quotes = 1):

    slips = []


    for i in range(numb_quotes):
       res = requests.get(url)
       print(f"{i} scrapping '{url}'")
       slip_data = res.text.replace('{"slip": { ','').replace('}}','')
       slip_dict = json.loads("{"+slip_data+"}")

       slip_id = slip_dict["id"]
       slip_advice = slip_dict["advice"]

       slip = Slip(slip_id,slip_advice)
       slips.append(slip)
       
    return slips
    # print(slips)


if __name__ == "__main__":
    test = scrapping_func(2)
    print(test)
    print(type(test))
    print(type(test[0]))

