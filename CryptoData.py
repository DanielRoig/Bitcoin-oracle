import json
import urllib.request as request


class CryptoData:
    def __init__(self):
        self.apiKey = "8e5b48cac520f4260f6b023024436b5cefd36933f7acb350cdfd48bcd8930adf"

    def average_data(self, currency_):
        currency_list = {}
        currency_list_file = open('/assets/currency_list.txt', "r")

        # Fill up the dictionary with the crypto abrevation ("bitcoin" : "BTC")
        for line in currency_list_file:
            line = line.split('')
            currency_list[line[0]] = line[1]

        # If currency input is not in the dictionary
        if currency_ not in currency_list:
            data = {
                'state': 'WRONG'
            }
            return data

        # Retrieve currency information from the API
        url = "https://min-api.cryptocompare.com/data/generateAvg?fsym=" + currency_list[currency_] \
              + "&tsym=USD&e=Kraken"
        response = request.urlopen(url + "&api_key=" + self.apiKey)
        data = json.loads(response.read())
        data['state'] = 'OK'
        return data



# Web api -> https://www.cryptocompare.com
# User -> carlos.matos.from.new.york@gmail.com
# Pw -> Bitconnect0
