# emissions ecosystem
BALANCER_EMISSIONS = 121_930
AURA_FEE = 0.25

DIGG_POOL_ID = "0x8EB6C82C3081BBBD45DCAC5AFA631AAC53478B7C000100000000000000000270"


def aura_mint_ratio(aura, block_current_proposal):
    total_cliffs = aura.totalCliffs()
    cliff_reduction = aura.reductionPerCliff() / 1e18
    aura_total_supply = aura.totalSupply(block_identifier=block_current_proposal) / 1e18
    init_mint_amount = aura.INIT_MINT_AMOUNT() / 1e18
    aura_mint_ratio = (
        (total_cliffs - (aura_total_supply - init_mint_amount) / cliff_reduction) * 2.5
        + 700
    ) / total_cliffs
    return aura_mint_ratio


def weekly_emissions_after_fee(aura_mint_ratio, bal_price, aura_price):
    weekly_emissions = (
        BALANCER_EMISSIONS * bal_price
        + BALANCER_EMISSIONS * aura_mint_ratio * aura_price
    )
    weekly_emissions_after_fee = weekly_emissions * (1 - AURA_FEE)
    return weekly_emissions_after_fee


def get_gravi_in_balancer_pool(balancer_vault, block_current_proposal):
    # digg pool id
    digg_pool_info = balancer_vault.getPoolTokens(
        DIGG_POOL_ID,
        block_identifier=block_current_proposal,
    )
    gravi_in_digg_pool = digg_pool_info[1][2] / 1e18
    return gravi_in_digg_pool
