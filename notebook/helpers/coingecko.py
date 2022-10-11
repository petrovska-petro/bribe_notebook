from pycoingecko import CoinGeckoAPI


def get_prices():
    prices = CoinGeckoAPI().get_price(["aura-finance", "balancer", "badger-dao"], "usd")
    bal_price = prices["balancer"]["usd"]
    aura_price = prices["aura-finance"]["usd"]
    badger_price = prices["badger-dao"]["usd"]

    return bal_price, aura_price, badger_price
