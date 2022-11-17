from datetime import datetime, timedelta

import pandas as pd

CVX_FEE = 0.17
ROUND_DAYS_DURATION = 14

# frax emission details
FXS_DAILY_EMISSIONS = 12_500


def cvx_mint_ratio(cvx, block_current_proposal):
    # https://docs.convexfinance.com/convexfinanceintegration/cvx-minting#mint-formula
    total_cliffs = cvx.totalCliffs()
    cliff_reduction = cvx.reductionPerCliff() / 1e18
    cvx_total_supply = cvx.totalSupply(block_identifier=block_current_proposal) / 1e18
    current_cliff = cvx_total_supply / cliff_reduction
    remaining_cliffs = total_cliffs - current_cliff
    cvx_mint_ratio = remaining_cliffs / total_cliffs
    return cvx_mint_ratio


def votium_round_emissions_after_fee(cvx_mint_ratio, crv_price, cvx_price):
    # borrow from: https://github.com/Badger-Finance/badger-ape/blob/convex_curve_wars/scripts/convex_curve_wars_votium.py#L29
    schedules = pd.read_csv("data/crv_schedules.csv")
    schedules["DateTime"] = pd.date_range("2020-08-13", periods=2190, freq="D")
    schedules = schedules.set_index("DateTime")
    ems_upcoming_round = schedules["Community"].loc[
        (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
    ]
    ems_today = schedules["Community"].loc[datetime.now().strftime("%Y-%m-%d")]
    # fee only taken from crv rev: https://docs.convexfinance.com/convexfinance/faq/fees#ed94
    round_emissions = (ems_upcoming_round - ems_today) * (1 - CVX_FEE)
    biweekly_emissions = (
        round_emissions * crv_price + round_emissions * cvx_mint_ratio * cvx_price
    )
    return biweekly_emissions


def fxs_emissions_usd(fxs_price, fxs_weight, treasury_capture):
    emissions_usd = FXS_DAILY_EMISSIONS * fxs_price * ROUND_DAYS_DURATION
    return emissions_usd * fxs_weight * treasury_capture
