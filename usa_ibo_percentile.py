import matplotlib.pyplot as plt
import pandas as pd

# Historical IBO Data for USA (2003 - 2025)
# Format: (Year, USA's Unofficial Team Rank, Total Participating Countries)
# USA first participated in IBO in 2003 via CEE/USABO.
ibo_data = [
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
]


# Create DataFrame
df = pd.DataFrame(ibo_data, columns=["Year", "Rank", "Total_Countries"])

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
    xytext=(best_year["Year"] - 5, best_year["Percentile"]),
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
    f"USA's IBO Performance Percentile ({ibo_data[0][0]} - {ibo_data[-1][0]})\nRelative Positioning to Overall Pool Size",
    fontsize=16,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Year", fontsize=12, labelpad=10)
plt.ylabel("Competitive Percentile (%) — Higher is Better", fontsize=12, labelpad=10)
plt.xlim(ibo_data[0][0] - 1, ibo_data[-1][0] + 1)
plt.ylim(minpct - 6, 103)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="lower left", fontsize=11)

# Informative visual anchor for the 2020 gap
plt.axvspan(2019.5, 2020.5, color="#ecf0f1", alpha=0.7, zorder=1)
plt.text(
    2020,
    minpct + 2,
    "2020\nNo Participation",
    color="#7f8c8d",
    fontsize=9,
    ha="center",
    fontweight="bold",
)

plt.tight_layout()
plt.savefig("assets/usa_ibo_percentile.png")
plt.show()
