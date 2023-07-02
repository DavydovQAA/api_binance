import requests

BASE_URL = 'https://api.binance.com/api/v3'


class BinanceAPI:

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url

    def get_crypto_price(self, crypto_name: str) -> float:
        """
        Получаем последнюю цену на криптовалюту
        """
        url = f"{self.base_url}/ticker/price?symbol={crypto_name}USDT"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return float(data['price'])
        else:
            raise Exception(f"Ошибка при получении цены для {crypto_name}. Код ошибки: {response.status_code}")