import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates


# Plot all 3 datasets in 1 graph and store the figure
def plot_data(data, script_dir):
    cfont = {"fontname": "Calibri"}

    sns.set_style("ticks")
    fig, ax = plt.subplots(figsize=(14, 7))

    # Plot lines for each dataset
    sns.lineplot(
        ax=ax,
        x="date",
        y="Apple_driving_rolling",
        label="Apple - requests for travel indications by car",
        data=data,
        color="k",
        linestyle="--",
    )
    sns.lineplot(
        ax=ax,
        x="date",
        y="Facebook_movement_change_rolling",
        label="Facebook - general movements",
        data=data,
        color="#b1b2b7",
        linestyle="-",
    )
    sns.lineplot(
        ax=ax,
        x="date",
        y="Google_shopping_rolling",
        label="Google - shopping and entertainment venues attendances",
        data=data,
        color="#73747e",
        linestyle="-.",
    )
    sns.lineplot(
        ax=ax,
        x="date",
        y="Google_offices_rolling",
        label="Google - office attendances",
        data=data,
        color="#464646",
        linestyle="-",
    )

    # Set plot title and labels
    ax.set_title(
        "Percentage change of mobility in the Piedmont region \ncompared to the baseline - (7 days moving average)",
        size=18,
        weight="bold",
        y=1.05,
        **cfont
    )
    ax.set_xlabel("Month", size=14, **cfont)
    ax.set_ylabel("7 days moving average (% change)", size=14, **cfont)

    # add vertical lines for all phases of the pandemic
    for phase in ["2020-03-10", "2020-05-04", "2020-06-15"]:
        ax.axvline(x=pd.to_datetime(phase), color="gray", linestyle=":")
    for red_zone in [
        "2020-11-06",
        "2020-12-24",
        "2020-12-31",
        "2021-01-05",
        "2021-03-15",
    ]:
        ax.axvline(x=pd.to_datetime(red_zone), color="crimson", linestyle=":")
    for orange_zone in ["2020-11-29", "2021-01-17", "2021-03-01", "2021-04-12"]:
        ax.axvline(x=pd.to_datetime(orange_zone), color="orange", linestyle=":")
    for yellow_zone in ["2020-12-13", "2021-01-11", "2021-02-01", "2021-04-26"]:
        ax.axvline(x=pd.to_datetime(yellow_zone), color="yellow", linestyle=":")

    # annotate phases with a vertically positioned text
    annot1 = pd.DataFrame(
        {
            "x": [
                pd.to_datetime("2020-03-10"),
                pd.to_datetime("2020-05-04"),
                pd.to_datetime("2020-06-15"),
            ],
            "y": [55, 54, 58],
        },
        index=[
            "Phase 1 (national\nlockdown)",
            "Phase 2 (reducing\nthe measures)",
            'Phase 3 ("living"\nwith COVID-19)',
        ],
    )
    for t, p in annot1.iterrows():
        ax.annotate(
            text=t,
            xy=p,
            xytext=(13, 0),
            textcoords="offset points",
            rotation=90,
            fontsize=12,
            ha="right",
            **cfont
        )

    # annotate zones with a vertically positioned text
    annot2 = pd.DataFrame(
        {
            "x": [
                pd.to_datetime("2020-11-06"),
                pd.to_datetime("2020-11-29"),
                pd.to_datetime("2020-12-13"),
                pd.to_datetime("2020-12-24"),
                pd.to_datetime("2020-12-31"),
                pd.to_datetime("2021-01-05"),
                pd.to_datetime("2021-01-11"),
                pd.to_datetime("2021-01-17"),
                pd.to_datetime("2021-02-01"),
                pd.to_datetime("2021-03-01"),
                pd.to_datetime("2021-03-15"),
                pd.to_datetime("2021-04-12"),
                pd.to_datetime("2021-04-26"),
            ],
            "y": [69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69],
        },
        index=[
            "06/11/2020",
            "29/11/2020",
            "13/12/2020",
            "24/12/2020",
            "31/12/2020",
            "05/01/2021",
            "11/01/2021",
            "17/01/2021",
            "01/02/2021",
            "01/03/2021",
            "15/03/2021",
            "12/04/2021",
            "26/04/2021",
        ],
    )
    for t, p in annot2.iterrows():
        ax.annotate(
            text=t,
            xy=p,
            xytext=(1, 3),
            textcoords="offset points",
            rotation=90,
            fontsize=12,
            ha="right",
            **cfont
        )

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.axhline(y=0, color="#28282c", linestyle="--", linewidth=0.5)
    ax.annotate(
        text="Baseline",
        xy=(pd.to_datetime("2021-07-01"), 0),
        xytext=(-1, 3),
        textcoords="offset points",
        rotation=0,
        fontsize=12,
        **cfont
    )

    bbox_props = dict(boxstyle="round4, pad=0.15", fc="w", ec="k", lw=0.72)
    kw = dict(
        xycoords="data",
        textcoords="offset points",
        fontsize=12,
        fontweight="bold",
        bbox=bbox_props,
        ha="right",
        va="top",
    )

    # annotate Apple data minimum and maximum
    ax.annotate(
        "{:,d}%".format(np.round(data["Apple_driving_rolling"].min()).astype(int)),
        xy=(
            data[
                data["Apple_driving_rolling"] == data["Apple_driving_rolling"].min()
            ].date.iloc[0],
            data["Apple_driving_rolling"].min(),
        ),
        xytext=(15, -5),
        **cfont,
        **kw
    )

    ax.annotate(
        "{:,d}%".format(
            np.round(data[data.date.dt.month == 7].Apple_driving_rolling.max()).astype(
                int
            )
        ),
        xy=(
            data[
                data["Apple_driving_rolling"]
                == data[data.date.dt.month == 8].Apple_driving_rolling.max()
            ].date.iloc[0],
            data[data.date.dt.month == 8].Apple_driving_rolling.max(),
        ),
        xytext=(5, 20),
        **cfont,
        **kw
    )

    ax.annotate(
        "{:,d}%".format(
            np.round(data[data.date.dt.month == 12].Apple_driving_rolling.min()).astype(
                int
            )
        ),
        xy=(
            data[
                data["Apple_driving_rolling"]
                == data[data.date.dt.month == 12].Apple_driving_rolling.min()
            ].date.iloc[0],
            data[data.date.dt.month == 12].Apple_driving_rolling.min(),
        ),
        xytext=(25, -13),
        **cfont,
        **kw
    )

    ax.annotate(
        "{:,d}%".format(
            np.round(
                data[data["date"] == "2021-06-30"].Apple_driving_rolling.iloc[0]
            ).astype(int)
        ),
        xy=(
            pd.to_datetime("2021-06-30"),
            data[data["date"] == "2021-06-30"].Apple_driving_rolling.iloc[0],
        ),
        xytext=(27, 10),
        **cfont,
        **kw
    )

    # annotate Facebook data minimum and maximum
    # ax.annotate('{:,d}%'.format(np.round(data[data.date.dt.month == 11].Facebook_movement_change_rolling.max()).astype(int)),
    #            xy=(data[data['Facebook_movement_change_rolling'] == data[data.date.dt.month == 11].Facebook_movement_change_rolling.max()].date.iloc[0],
    #                data[data.date.dt.month == 11].Facebook_movement_change_rolling.max()),
    #            xytext=(35, 10), **cfont, **kw)

    # ax.annotate('{:,d}%'.format(np.round(data[data.date.dt.month == 12].Facebook_movement_change_rolling.max()).astype(int)),
    #            xy=(data[data['Facebook_movement_change_rolling'] == data[data.date.dt.month == 12].Facebook_movement_change_rolling.max()].date.iloc[0],
    #                data[data.date.dt.month == 12].Facebook_movement_change_rolling.max()),
    #            xytext=(15, 15), **cfont, **kw)

    # ax.annotate('{:,d}%'.format(np.round(data[data['date'] == '2021-06-30'].Facebook_movement_change_rolling.iloc[0]).astype(int)),
    #            xy=(pd.to_datetime('2021-06-30'), data[data['date'] == '2021-06-30'].Facebook_movement_change_rolling.iloc[0]),
    #            xytext=(25, 0), **cfont, **kw)

    # annotate Google data minimum and maximum
    ax.annotate(
        "{:,d}%".format(
            np.round(data[data.date.dt.month == 8].Google_offices_rolling.min()).astype(
                int
            )
        ),
        xy=(
            data[
                data["Google_offices_rolling"]
                == data[data.date.dt.month == 8].Google_offices_rolling.min()
            ].date.iloc[0],
            data[data.date.dt.month == 8].Google_offices_rolling.min(),
        ),
        xytext=(11, -5),
        **cfont,
        **kw
    )

    # ax.annotate('{:,d}%'.format(np.round(data[data.date.dt.month == 1].Google_shopping_rolling.min()).astype(int)),
    #            xy=(data[data['Google_shopping_rolling'] == data[data.date.dt.month == 1].Google_shopping_rolling.min()].date.iloc[0],
    #                data[data.date.dt.month == 1].Google_shopping_rolling.min()),
    #            xytext=(11, -5), **cfont, **kw)

    ax.annotate(
        "{:,d}%".format(
            np.round(
                data[data["date"] == "2021-06-30"].Google_offices_rolling.iloc[0]
            ).astype(int)
        ),
        xy=(
            pd.to_datetime("2021-06-30"),
            data[data["date"] == "2021-06-30"].Google_offices_rolling.iloc[0],
        ),
        xytext=(28, -2),
        **cfont,
        **kw
    )

    ax.annotate(
        "{:,d}%".format(
            np.round(
                data[data["date"] == "2021-06-30"].Google_shopping_rolling.iloc[0]
            ).astype(int)
        ),
        xy=(
            pd.to_datetime("2021-06-30"),
            data[data["date"] == "2021-06-30"].Google_shopping_rolling.iloc[0],
        ),
        xytext=(28, 5),
        **cfont,
        **kw
    )

    # prepate figure for plotting
    ax.set_ylim(-100, 100)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.xticks(rotation=10)

    plt.legend(loc=(-0.035, 1.02))
    fig.tight_layout()

    # Save the plot
    visualization_dir = os.path.abspath(os.path.join(script_dir, "reports", "figures"))
    figure_path = os.path.join(visualization_dir, "Post-Covid_Mobility_Piedmont.png")
    plt.savefig(figure_path, format="png", dpi=300, facecolor="white")

    return figure_path
