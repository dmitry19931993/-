from loader import bot
from states.contact_information import UserEnterData
from keyboards.reply.contact import request_contact
from telebot.types import Message
import requests
import json



@bot.message_handler(commands=["bestdeal"])
def bestdeal(message: Message) -> None:
    bot.set_state(message.from_user.id, UserEnterData.city, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет,{message.from_user.full_name}, введи город, в котором будем искать')

@bot.message_handler(state= UserEnterData.city)
def get_city(message: Message) -> None:
    url = "https://hotels4.p.rapidapi.com/locations/v3/search"
    querystring = {"q": UserEnterData.city}
    headers = {
        "X-RapidAPI-Key": "3734da3a94msh550e03913642a91p1b012djsna8d5f3b74cae",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring, timeout=10)
    data_ship = json.loads(response.text)

    url_2 = "https://hotels4.p.rapidapi.com/properties/v2/list"
    payload_2 = {
        "eapid": 1,
        "siteId": 300000001,
        "destination": {"regionId": 3000},
        "checkInDate": {
            "day": 10,
            "month": 5,
            "year": 2023
        },
        "checkOutDate": {
            "day": 15,
            "month": 5,
            "year": 2023
        },
        "rooms": [
            {
                "adults": 2
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": 200,
        "sort": "PRICE_LOW_TO_HIGH",
        "filters": {"price": {
            "max": 150,
            "min": 100
        }}
    }
    headers_2 = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "3734da3a94msh550e03913642a91p1b012djsna8d5f3b74cae",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response_2 = requests.request("POST", url_2, json=payload_2, headers=headers_2)

    bot.send_message(message.from_user.id, response_2.text)
    #print(data_ship['sr'][0]['gaiaId'])
    # print(data_ship)