from binance_api import BinanceAPI
from crypto_currency import CryptoCurrency
from common import write_file

CRYPTO_CURRENCIES = ['BTC', 'ETH', 'XRP', 'LTC', 'EOS']

binance_api = BinanceAPI()
crypto_checker = CryptoCurrency(binance_api)
crypto_prices = crypto_checker.get_crypto_prices(CRYPTO_CURRENCIES)

# Записываем крипту и соответствующую последнюю цену
write_file(crypto_prices, 'crypto_prices.txt')

# Отображаем список валют, которые имеют стоимость ниже BTC
print("Список валют, которые имеют стоимость ниже BTC:", crypto_checker.compare_with_btc(crypto_prices), sep='\n')

# Отображаем список всех валют и их стоимость
print("Список всех валют и их стоимость", crypto_prices, sep='\n')