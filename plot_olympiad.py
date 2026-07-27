import argparse
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

# Data dictionary for all Olympiads
olympiad_data = {
    "IMO": {
        "data": [
            (1974, 2, 18),
            (1975, 3, 17),
            (1976, 3, 18),
            (1977, 1, 21),
            (1978, 2, 22),
            (1979, 5, 23),
            (1981, 1, 27),
            (1982, 3, 30),
            (1983, 2, 32),
            (1984, 4, 34),
            (1985, 2, 38),
            (1986, 1, 37),
            (1987, 5, 42),
            (1988, 6, 49),
            (1989, 15, 50),
            (1990, 3, 54),
            (1991, 5, 56),
            (1992, 2, 56),
            (1993, 7, 73),
            (1994, 1, 69),
            (1995, 11, 73),
            (1996, 2, 75),
            (1997, 3, 82),
            (1998, 3, 76),
            (1999, 3, 81),
            (2000, 3, 82),
            (2001, 2, 83),
            (2002, 2, 84),
            (2003, 2, 82),
            (2004, 2, 85),
            (2005, 3, 91),
            (2006, 2, 90),
            (2007, 3, 93),
            (2008, 3, 97),
            (2009, 2, 104),
            (2010, 3, 96),
            (2011, 2, 101),
            (2012, 3, 100),
            (2013, 3, 97),
            (2014, 2, 101),
            (2015, 1, 104),
            (2016, 1, 109),
            (2017, 4, 111),
            (2018, 1, 107),
            (2019, 1, 112),
            (2021, 4, 107),
            (2022, 3, 104),
            (2023, 2, 112),
            (2024, 1, 108),
            (2025, 2, 115),
            (2026, 2, 117),
        ],
        "top_milestone_threshold": 0.05,
        "peaks": [2024],
        "title_years": "1974-2026",
    },
    "IBO": {
        "data": [
            (2003, 8, 45),
            (2004, 3, 48),
            (2005, 5, 50),
            (2006, 4, 55),
            (2007, 2, 49),
            (2008, 2, 55),
            (2009, 3, 56),
            (2010, 5, 60),
            (2011, 1, 58),
            (2012, 2, 59),
            (2013, 1, 62),
            (2014, 3, 61),
            (2015, 1, 61),
            (2016, 2, 68),
            (2017, 1, 64),
            (2018, 4, 68),
            (2019, 3, 73),
            (2021, 4, 76),
            (2022, 5, 65),
            (2023, 3, 76),
            (2024, 5, 73),
            (2025, 4, 75),
        ],
        "top_milestone_threshold": 0.05,
        "peaks": [2011],
        "title_years": "2003-2025",
    },
    "IChO": {
        "data": [
            (1984, 3, 18),
            (1985, 2, 22),
            (1986, 2, 24),
            (1987, 3, 26),
            (1988, 2, 28),
            (1989, 3, 30),
            (1990, 2, 30),
            (1991, 2, 33),
            (1992, 5, 34),
            (1993, 4, 38),
            (1994, 3, 40),
            (1995, 3, 43),
            (1996, 2, 46),
            (1997, 2, 48),
            (1998, 3, 50),
            (1999, 2, 51),
            (2000, 2, 53),
            (2001, 1, 54),
            (2002, 3, 57),
            (2003, 3, 59),
            (2004, 2, 61),
            (2005, 3, 59),
            (2006, 2, 67),
            (2007, 1, 68),
            (2008, 2, 66),
            (2009, 2, 64),
            (2010, 2, 68),
            (2011, 3, 70),
            (2012, 3, 72),
            (2013, 4, 73),
            (2014, 3, 75),
            (2015, 2, 75),
            (2016, 3, 75),
            (2017, 1, 76),
            (2018, 2, 76),
            (2019, 2, 80),
            (2020, 1, 60),
            (2021, 2, 85),
            (2022, 5, 84),
            (2023, 4, 89),
            (2024, 2, 90),
            (2025, 1, 90),
            (2026, 2, 93),
        ],
        "top_milestone_threshold": 0.05,
        "peaks": [2001],
        "title_years": "1984-2026",
        "has_2020": True,
    },
    "IOAA": {
        "data": [
            (2013, 11, 35),
            (2014, 8, 37),
            (2015, 7, 39),
            (2016, 6, 41),
            (2017, 5, 46),
            (2018, 4, 37),
            (2019, 3, 47),
            (2021, 2, 47),
            (2022, 1, 44),
            (2023, 3, 50),
            (2024, 1, 52),
            (2025, 1, 64),
        ],
        "top_milestone_threshold": 0.05,
        "peaks": [2022, 2025],
        "title_years": "2013-2025",
    },
    "IOI": {
        "data": [
            (1992, 1, 51),
            (1993, 2, 48),
            (1994, 1, 51),
            (1995, 1, 56),
            (1996, 2, 56),
            (1997, 2, 57),
            (1998, 2, 62),
            (1999, 1, 65),
            (2000, 2, 68),
            (2001, 2, 75),
            (2002, 4, 77),
            (2003, 3, 75),
            (2004, 2, 81),
            (2005, 3, 72),
            (2006, 1, 74),
            (2007, 4, 76),
            (2008, 2, 78),
            (2009, 3, 78),
            (2010, 2, 80),
            (2011, 1, 78),
            (2012, 1, 81),
            (2013, 3, 77),
            (2014, 1, 81),
            (2015, 2, 83),
            (2016, 2, 80),
            (2017, 3, 83),
            (2018, 1, 87),
            (2019, 3, 87),
            (2020, 1, 87),
            (2021, 2, 88),
            (2022, 3, 89),
            (2023, 2, 87),
            (2024, 2, 91),
            (2025, 2, 90),
            (2026, 1, 92),
        ],
        "top_milestone_threshold": 0.05,
        "peaks": [2026],
        "title_years": "1992-2026",
        "has_2020": True,
    },
    "IPhO": {
        "data": [
            (1986, 5, 19),
            (1987, 5, 20),
            (1988, 3, 25),
            (1989, 4, 28),
            (1990, 3, 32),
            (1991, 3, 35),
            (1992, 3, 37),
            (1993, 3, 41),
            (1994, 3, 46),
            (1995, 1, 48),
            (1996, 1, 56),
            (1997, 5, 56),
            (1998, 2, 56),
            (1999, 5, 62),
            (2000, 2, 63),
            (2001, 3, 65),
            (2002, 2, 66),
            (2003, 3, 54),
            (2004, 3, 71),
            (2005, 2, 73),
            (2006, 1, 86),
            (2007, 3, 69),
            (2008, 3, 82),
            (2009, 5, 68),
            (2010, 4, 79),
            (2011, 2, 84),
            (2012, 1, 81),
            (2013, 5, 83),
            (2014, 2, 85),
            (2015, 4, 82),
            (2016, 3, 84),
            (2017, 2, 88),
            (2018, 6, 86),
            (2019, 4, 78),
            (2021, 3, 76),
            (2022, 3, 75),
            (2023, 3, 80),
            (2024, 2, 43),
            (2025, 1, 87),
        ],
        "top_milestone_threshold": 0.05,
        "peaks": [2025],
        "title_years": "1986-2025",
    },
}


def plot_olympiad(name):
    if name not in olympiad_data:
        print(
            f"Error: {name} is not a valid Olympiad. Choose from {list(olympiad_data.keys())}"
        )
        sys.exit(1)

    config = olympiad_data[name]
    data = config["data"]

    # Create DataFrame
    df = pd.DataFrame(data, columns=["Year", "Rank", "Total_Countries"])

    # Calculate the competitive percentile (Higher is better, 100% = 1st place)
    df["Percentile"] = (1 - (df["Rank"] - 1) / df["Total_Countries"]) * 100

    # Initialize the plot
    plt.figure(figsize=(18, 10))

    # Plot the primary percentile path
    plt.plot(
        df["Year"],
        df["Percentile"],
        marker="o",
        linestyle="-",
        color="#2c3e50",
        linewidth=2,
        markersize=5,
        alpha=0.8,
        label="USA's Performance Percentile",
    )

    # Annotate every individual data point with its Rank / Total Countries string
    prepct = 0
    minpct = 101
    for i, row in df.iterrows():
        year = int(row["Year"])
        rank = int(row["Rank"])
        total = int(row["Total_Countries"])
        pct = row["Percentile"]

        # Toggle text positions slightly to avoid visual overlap
        if pct > prepct:
            yano = 8
        else:
            yano = -14
        xy_text_offset = (0, yano)

        plt.annotate(
            f"{pct:.0f}%ile ({rank}/{total})",
            xy=(year, pct),
            xytext=xy_text_offset,
            textcoords="offset points",
            ha="center",
            fontsize=8,
            color="#34495e",
            weight="semibold",
        )
        prepct = pct
        minpct = min(minpct, pct)

    # Highlight standout historic peaks
    top_milestones = df[
        df["Rank"] / df["Total_Countries"] <= config["top_milestone_threshold"]
    ]
    plt.scatter(
        top_milestones["Year"],
        top_milestones["Percentile"],
        color="#e74c3c",
        s=120,
        zorder=5,
        label="Top 5% Finishes",
    )

    # Specifically label the all-time high water mark(s)
    peaks = config["peaks"]
    if len(peaks) == 1:
        best_year = peaks[0]
        best_data = df[df["Year"] == best_year].iloc[0]
        fmt_pct = (
            f"{best_data['Percentile']:.1f}"
            if name in ["IMO", "IBO", "IOI"]
            else f"{best_data['Percentile']:.0f}"
        )

        # Offset adjustment based on Olympiad to match original visuals
        xytext_offset = 5
        if name == "IMO":
            xytext_offset = 5
        elif name == "IBO":
            xytext_offset = 5
        elif name == "IChO":
            xytext_offset = 5
        elif name == "IOI":
            xytext_offset = 5

        plt.annotate(
            f"\U0001f3c6 Historic Peak!\nRank {int(best_data['Rank'])} of {int(best_data['Total_Countries'])}\n({fmt_pct}th Percentile)",
            xy=(best_year, best_data["Percentile"]),
            xytext=(
                best_year - xytext_offset,
                best_data["Percentile"] - (6 if name != "IOI" else 2),
            ),
            arrowprops=dict(
                facecolor="#e74c3c", arrowstyle="->", connectionstyle="arc3,rad=-0.1"
            ),
            fontsize=11,
            fontweight="bold",
            color="#e74c3c",
            ha="center",
            fontname="Segoe UI Emoji",
        )
    elif len(peaks) == 2:
        best_1 = df[df["Year"] == peaks[0]].iloc[0]
        best_2 = df[df["Year"] == peaks[1]].iloc[0]

        text_x = (peaks[0] + peaks[1]) // 2
        text_y = best_1["Percentile"] + (1 if name == "IOAA" else 2)
        fmt_pct = f"{best_1['Percentile']:.0f}"

        # Main Annotation (Contains the Text + Arrow pointing to first peak)
        plt.annotate(
            f"\U0001f3c6 Historic Peak!\nRank {int(best_1['Rank'])} of {int(best_1['Total_Countries'])}\n({fmt_pct}th Percentile)",
            xy=(peaks[0], best_1["Percentile"]),
            xytext=(text_x, text_y),
            arrowprops=dict(
                color="#e74c3c", arrowstyle="->", connectionstyle="arc3,rad=-0.1"
            ),
            fontsize=11,
            fontweight="bold",
            color="#e74c3c",
            ha="center",
            fontname="Segoe UI Emoji",
        )
        # Ghost Annotation (Empty Text + Arrow pointing to second peak)
        plt.annotate(
            "",
            xy=(peaks[1], best_2["Percentile"]),
            xytext=(text_x + 1, text_y),
            arrowprops=dict(
                color="#e74c3c",
                arrowstyle="->",
                connectionstyle="arc3,rad=0.1",
            ),
        )

    # Plot customization
    plt.title(
        f"USA's {name} Performance Percentile ({config['title_years']})\nRelative Positioning to Overall Pool Size",
        fontsize=16,
        fontweight="bold",
        pad=15,
    )
    plt.xlabel("Year", fontsize=12, labelpad=10)
    plt.ylabel(
        "Competitive Percentile (%) \u2014 Higher is Better", fontsize=12, labelpad=10
    )

    plt.xlim(data[0][0] - 1, data[-1][0] + 1)
    plt.ylim(minpct - 6, 103)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="lower left", fontsize=11)

    # Informative visual anchor for the 2020 gap
    if not config.get("has_2020"):
        plt.axvspan(2019.5, 2020.5, color="#ecf0f1", alpha=0.7, zorder=1)
        plt.text(
            2020,
            55,
            "2020\nCancelled",
            color="#7f8c8d",
            fontsize=9,
            ha="center",
            fontweight="bold",
        )

    plt.tight_layout()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "assets")
    os.makedirs(assets_dir, exist_ok=True)
    plt.savefig(os.path.join(assets_dir, f"usa_{name.lower()}_percentile.png"))
    print(f"Generated plot for {name} at assets/usa_{name.lower()}_percentile.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Olympiad Performance Plots")
    parser.add_argument(
        "olympiad",
        type=str.upper,
        nargs="?",
        choices=list(olympiad_data.keys()) + ["ALL"],
        default="ALL",
        help="Specify the Olympiad to plot (IMO, IBO, IChO, IOAA, IOI, IPhO, or ALL)",
    )
    args = parser.parse_args()

    if args.olympiad == "ALL":
        for olym in olympiad_data.keys():
            plot_olympiad(olym)
    else:
        plot_olympiad(args.olympiad)
