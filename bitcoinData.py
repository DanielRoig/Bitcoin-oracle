import urllib, json

class BitcoinData():
	def __init__(self):
		self.apiKey = "8e5b48cac520f4260f6b023024436b5cefd36933f7acb350cdfd48bcd8930adf"

	def averageData(self):
		url = "https://min-api.cryptocompare.com/data/generateAvg?fsym=BTC&tsym=USD&e=Kraken"
		response = urllib.urlopen(url+"&api_key="+self.apiKey)
		data = json.loads(response.read())
		return data


#Web api -> https://www.cryptocompare.com
#User -> carlos.matos.from.new.york@gmail.com
#Pw -> Bitconnect0