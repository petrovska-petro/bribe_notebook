import requests

# endpoints
BALANCER_SUBGRAPH = "https://api.thegraph.com/subgraphs/name/balancer-labs/balancer-v2"
SNAPSHOT_SUBGRAPH = "https://hub.snapshot.org/graphql?"
LLAMA_DASHBOARD_URL = "https://api.llama.airforce//dashboard"

POOL_ID_BADGER = "0xb460daa847c45f1c4a41cb05bfb3b51c92e41b36000200000000000000000194"
POOL_ID_DIGG = "0x8eb6c82c3081bbbd45dcac5afa631aac53478b7c000100000000000000000270"

PROPOSAL_INFO_QUERY = """
        query($proposal_id: String) {
          proposal(id: $proposal_id) {
            scores_total
            snapshot
            choices
            scores
          }
        }
        """


TVL_QUERY = """
        query($pool_id: String) {
          pool(id: $pool_id) {
            totalLiquidity
          }
        }
        """

# methods to hit endpoints
def get_cost_per_vote_after_fee():
    LLAMA_DASHBOARD_URL = "https://api.llama.airforce//dashboard"
    aura_dash = requests.post(
        LLAMA_DASHBOARD_URL, json={"id": "bribes-overview-aura"}
    ).json()
    cost_per_vote_last_round = aura_dash["dashboard"]["epochs"][-1]["dollarPerVlAsset"]
    cost_per_vote_after_fee = cost_per_vote_last_round * (1.04)
    return cost_per_vote_after_fee


def get_proposal_info(proposal_id):
    response_proposal = requests.post(
        SNAPSHOT_SUBGRAPH,
        json={"query": PROPOSAL_INFO_QUERY, "variables": {"proposal_id": proposal_id}},
    ).json()["data"]["proposal"]

    return response_proposal


def get_tvl_balancer_badger_pool():
    response_tvl_badger = requests.post(
        BALANCER_SUBGRAPH,
        json={"query": TVL_QUERY, "variables": {"pool_id": POOL_ID_BADGER}},
    ).json()
    tvl_badger = float(response_tvl_badger["data"]["pool"]["totalLiquidity"])
    return tvl_badger


def get_tvl_balancer_digg_pool():
    response_tvl_badger = requests.post(
        BALANCER_SUBGRAPH,
        json={"query": TVL_QUERY, "variables": {"pool_id": POOL_ID_DIGG}},
    ).json()
    tvl_badger = float(response_tvl_badger["data"]["pool"]["totalLiquidity"])
    return tvl_badger
