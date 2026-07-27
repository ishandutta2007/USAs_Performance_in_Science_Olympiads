import matplotlib.pyplot as plt
import pandas as pd

# Historical IOI Data for USA (1992 - 2026)
# Format: (Year, USA's Unofficial Team Rank, Total Participating Countries)
# Source: stats.ioinformatics.org (unofficial team rank computed from sum of
# individual scores). USA first participated in IOI 1992.
ioi_data = [
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
]


# Create DataFrame
df = pd.DataFrame(ioi_data, columns=["Year", "Rank", "Total_Countries"])

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

# Highlight standout historic peaks (Top-5% finishes)
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
    xytext=(best_year["Year"] - 5, best_year["Percentile"] - 2),
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
    f"USA's IOI Performance Percentile ({ioi_data[0][0]} - {ioi_data[-1][0]})\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)

plt.xlim(ioi_data[0][0] - 1, ioi_data[-1][0] + 1)
plt.ylim(minpct - 6, 103)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower left", fontsize=11)

plt.tight_layout()
plt.savefig("assets/usa_ioi_percentile.png")
plt.show()
