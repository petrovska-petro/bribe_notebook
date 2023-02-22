import pandas as pd
import altair as alt


# Gauges/Pools labels
VISUAL_LABELS = ["80badger/20wbtc", "50badger/50reth"]

def incentive_visuals(gauges, amounts):
    df = pd.DataFrame(
        {
            "Gauges": gauges,
            "Badger Incentive Amount": amounts,
        }
    )
    bars = alt.Chart(df).mark_bar().encode(x="Badger Incentive Amount:Q", y="Gauges:O")

    text = bars.mark_text(
        align="left",
        baseline="middle",
        dx=3,  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(text="Badger Incentive Amount:Q")

    return bars + text


def pool_capture_visuals(pools, captures):
    df_incentives_split = pd.DataFrame(
        {
            "Pool": pools,
            "Capture": captures,
        }
    )

    bars = (
        alt.Chart(df_incentives_split)
        .mark_bar()
        .encode(x=alt.X("Capture:Q", axis=alt.Axis(format=".0%")), y="Pool:O")
    )

    text = bars.mark_text(
        align="left",
        baseline="middle",
        dx=3,  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(text=alt.Text("Capture:Q", format=".0%"))

    return bars + text


def pnl_visuals(gauges, costs, revenues):
    df = pd.DataFrame(
        {
            "Gauges": gauges,
            "Cost": costs,
            "Revenue": revenues,
        }
    )

    grouped_bars = (
        alt.Chart(df)
        .mark_bar()
        .encode(x="$:Q", y="P&L:N", color="P&L:N", row=alt.Row("Gauges"))
        .transform_fold(as_=["P&L", "$"], fold=["Cost", "Revenue"])
    )

    return grouped_bars
