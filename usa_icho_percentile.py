import matplotlib.pyplot as plt
import pandas as pd

# Historical IChO Data for USA (1984 - 2026)
# Format: (Year, USA's Unofficial Team Rank, Total Participating Countries)
icho_data = [
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
]

# Create DataFrame
df = pd.DataFrame(icho_data, columns=["Year", "Rank", "Total_Countries"])

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
    f"\U0001f3c6 Historic Peak!\nRank {int(best_year['Rank'])} of {int(best_year['Total_Countries'])}\n({best_year['Percentile']:.0f}th Percentile)",
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
    f"USA's IChO Performance Percentile ({icho_data[0][0]} - {icho_data[-1][0]})\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(icho_data[0][0] - 1, icho_data[-1][0] + 1)
plt.ylim(minpct - 6, 103)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower left", fontsize=11)

plt.tight_layout()
plt.savefig("assets/usa_icho_percentile.png")
plt.show()
