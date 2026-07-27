import matplotlib.pyplot as plt
import pandas as pd

# Historical IMO Data for USA (1974 - 2026)
# Format: (Year, USA's Rank, Total Participating Countries)
# Note: IMO was not held in 1980.
imo_data = [
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
]

# Create DataFrame
df = pd.DataFrame(imo_data, columns=["Year", "Rank", "Total_Countries"])

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
    xy_text_offset = (0, yano)  # if rank % 2 == 0 else (0, -14)

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

# Highlight standout historic peaks (Top-10 finishes)
top_milestones = df[df["Rank"] / df["Total_Countries"] <= 0.05]
plt.scatter(
    top_milestones["Year"],
    top_milestones["Percentile"],
    color="#e74c3c",
    s=120,
    zorder=5,
    label="Top 5% Finishes",
)

# Specifically label the all-time high water mark
best_year = df.loc[df["Percentile"].idxmax()]
plt.annotate(
    f"\U0001f3c6 Historic Peak!\nRank {int(best_year['Rank'])} of {int(best_year['Total_Countries'])}\n({best_year['Percentile']:.1f}th Percentile)",
    xy=(best_year["Year"], best_year["Percentile"]),
    xytext=(best_year["Year"] - 5, best_year["Percentile"] - 6),
    arrowprops=dict(
        facecolor="#e74c3c", arrowstyle="->", connectionstyle="arc3,rad=-0.1"
    ),
    fontsize=11,
    fontweight="bold",
    color="#e74c3c",
    ha="center",
    fontname="Segoe UI Emoji",
)

# Plot customization
plt.title(
    f"USA's IMO Performance Percentile ({imo_data[0][0]} - {imo_data[-1][0]})\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(imo_data[0][0] - 1, imo_data[-1][0] + 1)
plt.ylim(minpct - 6, 103)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower left", fontsize=11)

plt.tight_layout()
plt.savefig("assets/usa_imo_percentile.png")
plt.show()
