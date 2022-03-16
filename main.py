from copyreg import dispatch_table
from telegram.ext import *
import os
import responses as R
import time
import requests


API_KEY = "5128155257:AAEfJRbYP834iU-napV9jzonJ6HGHfw-ozo"
print("Bot started")

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
  
def alerts_start(update, context):
    last_above = -1
    last_below = -1
  #Create an infinite loop to continuously show the price
    while True:
        price = get_price()
        print(price)
        price_R = round(float(price), -2)

        if float(price) < price_R and price_R != last_below:
            print("----------------------")
            print(price)
            print("----------------------")
            update.message.reply_text(f"Price below: {price_R}$")
            last_below = price_R
            last_above = last_below - 100
        elif float(price) > price_R and price_R != last_above:
            print("----------------------")
            print(price)
            print("----------------------")
            update.message.reply_text(f"Price above: {price_R}$")
            last_above = price_R
            last_below = last_above + 100

        time.sleep(1) #Suspend execution for 3 seconds. ""


def help_command(update, context):
    update.message.reply_text("You will be alerted when the BTC price goes above or below the programmed prices.")
    update.message.reply_text("Programmed prices for now:\nBTC price rounded up by four decimal points. ")
    update.message.reply_text("Example: If price is $43,060.23, rounded price is 43,100.00 so you will be alerted if its above or below the rounded price.")

def handle_messages(update, context):
    text = str(update.message.text).lower()
    response = R.start_bot(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", alerts_start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_messages))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()