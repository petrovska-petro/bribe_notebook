BADGER_DELEGATE = "0x14f83ff95d4ec5e8812ddf42da1232b0ba1015e6"
VOTER_MSIG = "0xA9ed98B5Fb8428d68664f3C5027c62A10d45826b"

def get_council_vp_fee(vlAURA, block_current_proposal):
    strat_votes = (
        vlAURA.getVotes(BADGER_DELEGATE, block_identifier=block_current_proposal) / 1e18
    )
    # 10% fee
    council_fee = strat_votes * 0.1
    return council_fee

def get_voter_vp(vlAURA, block_current_proposal):
    return vlAURA.getVotes(VOTER_MSIG, block_identifier=block_current_proposal) /1e18