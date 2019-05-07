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
