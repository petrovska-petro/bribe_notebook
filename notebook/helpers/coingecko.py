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


def get_votium_prices():
    prices = CoinGeckoAPI().get_price(
        ["convex-finance", "curve-dao-token", "badger-dao", "frax-share"], "usd"
    )
    cvx_price = prices["convex-finance"]["usd"]
    crv_price = prices["curve-dao-token"]["usd"]
    badger_price = prices["badger-dao"]["usd"]
    fxs_price = prices["frax-share"]["usd"]

    return cvx_price, crv_price, badger_price, fxs_price


def get_coll_prices():
    prices = CoinGeckoAPI().get_price(["ethereum", "bitcoin"], "usd")
    eth_price = prices["ethereum"]["usd"]
    btc_price = prices["bitcoin"]["usd"]

    return eth_price, btc_price
