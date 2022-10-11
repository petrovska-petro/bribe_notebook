# NOTE: caps & budget may vary along the quarters modify accordingly
GAUGE_CAP = 0.02
MAX_BRIBE = 16_000


def get_bribe_info(total_vp, vebal_controlled, cost_per_vote_after_fee, badger_price):
    vlaura_req = total_vp / (vebal_controlled / GAUGE_CAP)
    cost_max_cap = vlaura_req * cost_per_vote_after_fee
    badger_to_bribe = cost_max_cap / badger_price

    return vlaura_req, cost_max_cap, badger_to_bribe
