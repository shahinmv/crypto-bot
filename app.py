import time
import requests
def get_price():
    test = requests.get("https://api.nomics.com/v1/currencies/ticker?key=d3819573b287c9d72d7525619619338b2a2ecf92&ids=BTC,ETH,XRP&interval=1d,30d&convert=USD&per-page=100&page=1")

    data = test.json()

    result = [x for x in data if x["id"]=="BTC"]

    data = str(result).split()

    final_price = data[13]

    disallowed_Characters = "',"
    for character in disallowed_Characters:
        final_price = final_price.replace(character, "")

    #final = before[0].replace(",", "")

    return final_price


if __name__ == "__main__":
    last_price = -1
    
    last_above = -1
    last_below = -1
  #Create an infinite loop to continuously show the price
    while True:
        price = get_price()
        #price = input()
        price_R = round(float(price), -2)

        if float(price) < price_R and price_R != last_below:
            print(f"Below {price_R}")
            last_below = price_R
            last_above = last_below - 100
        elif float(price) > price_R and price_R != last_above:
            print(f"Above {price_R}")
            last_above = price_R
            last_below = last_above + 100

        time.sleep(1) #Suspend execution for 3 seconds. """
    




