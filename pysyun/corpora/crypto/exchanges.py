import requests
import json

class CoinAPICurrencyAbbreviations:

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def process(self):
        
        results = []
        
        headers = {
            'X-CoinAPI-Key':  self.apiKey
        }
        response = requests.get('https://rest.coinapi.io/v1/exchangerate/ETC', headers=headers)
        response = json.loads(response.text)
        
        for rate in response['rates']:
            results.append(rate['asset_id_quote'])
        
        results = set(results)    
        results = list(results)        
        return results

class CoinMarketCapCurrencyAbbreviations:

    def __init__(self, apiKey):
        self.apiKey = apiKey

    def process(self):
        
        results = []
        
        headers = {
            'X-CMC_PRO_API_KEY':  self.apiKey
        }
        response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', headers=headers)
        response = json.loads(response.text)
        
        for item in response['data']:
            results.append(item['symbol'])
        
        results = set(results)    
        results = list(results)        
        return results

class PoloniexCurrencyAbbreviations:

    def process(self):
        
        results = []
        
        response = requests.get('https://poloniex.com/public?command=returnCurrencies')
        response = json.loads(response.text)
        
        for key in response:
            results.append(key)
        
        results = set(results)    
        results = list(results)        
        return results
    
 class EXMOCurrencyAbbreviations:

    def process(self):
        
        results = []
        
        response = requests.get('https://api.exmo.com/v1/currency/')
        response = json.loads(response.text)
        

        
        for key in response:
            results.append(key)
        
        results = set(results)    
        results = list(results)        
        return results
    
class CEXCurrencyAbbreviations:

    def process(self):
        
        results = []
        
        response = requests.get('https://cex.io/api/currency_limits')
        response = json.loads(response.text)
        
        for pair in response['data']['pairs']:
            results.append(pair['symbol1'])
        
        results = set(results)    
        results = list(results)        
        return results
