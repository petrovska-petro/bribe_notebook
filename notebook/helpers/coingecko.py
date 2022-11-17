from pycoingecko import CoinGeckoAPI


def get_prices():
    prices = CoinGeckoAPI().get_price(
        ["aura-finance", "balancer", "badger-dao", "rocket-pool"], "usd"
    )
    bal_price = prices["balancer"]["usd"]
    aura_price = prices["aura-finance"]["usd"]
    badger_price = prices["badger-dao"]["usd"]
    rpl_price = prices["rocket-pool"]["usd"]

    return bal_price, aura_price, badger_price, rpl_price
