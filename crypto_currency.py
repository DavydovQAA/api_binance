from binance_api import BinanceAPI

PRICES_FILE = 'crypto_prices.txt'


class CryptoCurrency:
    def __init__(self, binance_api: BinanceAPI):
        self.binance_api = binance_api

    def get_crypto_prices(self, cryptocurrencies: list or tuple) -> dict:
        """
        Получение цены криптовалюты
        """
        prices = {}
        for currency in cryptocurrencies:
            try:
                price = self.binance_api.get_crypto_price(currency)
                prices[currency] = price
            except Exception as exc:
                print(f"Ошибка {exc} при попытке получить цену для криптовалюты: {currency}")
        return prices

    @staticmethod
    def compare_with_btc(prices: dict) -> list:
        """
        Сравнение значения каждой криптовалюты со значением Биткоина (BTC)
        """
        btc_price = prices.pop('BTC')
        lower_than_btc = [currency for currency, price in prices.items() if price < btc_price]
        return lower_than_btc