"""Rebuild the Days 1–32 running snapshot from post front matter.

Run from any directory with Python, PyYAML and Matplotlib installed:
    python bin/plot_running_progress.py

Speed is calculated from recorded distance / moving time, avoiding rounding
in the app's displayed pace. Partial recordings are plotted but not averaged.
"""

import csv
import json
from pathlib import Path
from statistics import mean

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import yaml


ROOT = Path(__file__).resolve().parents[1]
rows = []
for path in sorted((ROOT / "_posts").glob("*-running-day-*.md")):
    post = yaml.safe_load(path.read_text().split("---", 2)[1])
    if not 1 <= post["day"] <= 32:
        continue
    minutes, seconds = map(int, post["moving_time"].split(":"))
    duration = minutes * 60 + seconds
    distance = post.get("recorded_distance_km", post["distance_km"])
    rows.append({
        "day": post["day"],
        "date": str(post["date"]),
        "distance_km": post["distance_km"],
        "recorded_distance_km": distance,
        "moving_time": post["moving_time"],
        "pace": post["average_pace"],
        "speed_kmh": distance * 3600 / duration,
        "partial": "recorded_distance_km" in post,
        "url": post["permalink"],
    })
rows.sort(key=lambda row: row["day"])
assert [row["day"] for row in rows] == list(range(1, 33)), "Expected all 32 runs"
assert all(row["speed_kmh"] > 0 for row in rows)
complete = [row for row in rows if not row["partial"]]
first = mean(row["speed_kmh"] for row in complete[:7])
last = mean(row["speed_kmh"] for row in complete[-7:])
change = (last / first - 1) * 100
rolling = [mean(row["speed_kmh"] for row in complete[i-6:i+1]) for i in range(6, len(complete))]
summary = {
    "first_seven_kmh": round(first, 2),
    "last_seven_kmh": round(last, 2),
    "change_percent": round(change, 1),
    "runs": [{**row, "speed_kmh": round(row["speed_kmh"], 2)} for row in rows],
}
(ROOT / "_data/running_progress.json").write_text(json.dumps(summary, indent=2) + "\n")
output = ROOT / "assets/data"
output.mkdir(exist_ok=True)
with (output / "running-days-01-32.csv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=summary["runs"][0].keys(), lineterminator="\n")
    writer.writeheader()
    writer.writerows(summary["runs"])

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "svg.fonttype": "none"})
fig, ax = plt.subplots(figsize=(11, 6.6), facecolor="white")
fig.subplots_adjust(left=0.09, right=0.97, top=0.76, bottom=0.22)
fig.text(0.09, 0.93, "Am I getting faster?", fontsize=24, weight="bold", color="#173b60")
fig.text(0.09, 0.875, "32 runs  ·  13 September–14 October 2026", color="#596b7e", fontsize=12)
fig.text(0.09, 0.82, f"First 7: {first:.2f} km/h     →     Latest 7: {last:.2f} km/h     ({change:+.1f}%)", color="#175b96", fontsize=13, weight="bold")
ax.plot([row["day"] for row in rows], [row["speed_kmh"] if not row["partial"] else float("nan") for row in rows],
        color="#91b9d7", linewidth=1.2, marker="o", markersize=5, label="Each complete run")
ax.plot([row["day"] for row in complete[6:]], rolling, color="#175b96", linewidth=2.8, label="Trailing 7 complete-run average")
partial = next(row for row in rows if row["partial"])
ax.scatter(partial["day"], partial["speed_kmh"], color="#b5660b", marker="D", s=65, zorder=5, label="Day 24: partial recording")
ax.axhline(10, color="#7c8793", linestyle="--", linewidth=1)
ax.text(1, 10.06, "10 km/h = 5 km in 30 minutes", fontsize=10, color="#596b7e")
ax.annotate(f"Day 32: {rows[-1]['speed_kmh']:.2f} km/h\n5 km in 30:17", xy=(32, rows[-1]["speed_kmh"]),
            xytext=(25, 9.35), fontsize=10, color="#173b60", arrowprops={"arrowstyle": "-", "color": "#596b7e"})
ax.set(xlim=(0.5, 32.7), ylim=(6.7, 10.35), xlabel="Run day", ylabel="Average speed (km/h) · higher is faster")
ax.set_xticks([1, 4, 8, 12, 16, 20, 24, 28, 32])
ax.grid(axis="y", color="#e4eaf0")
ax.set_axisbelow(True)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color("#ccd7e1")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.19), ncol=3, frameon=False, fontsize=10)
fig.text(0.09, 0.055, "Speed = recorded distance ÷ moving time. Day 24 is excluded from averages (only 3.50 km recorded).", fontsize=9, color="#596b7e")
fig.text(0.09, 0.027, "Descriptive progress, not an adjusted fitness measure: distance, traffic, weather and effort vary between runs.", fontsize=9, color="#596b7e")
destination = ROOT / "assets/img/challenges/running/progress-days-01-32"
fig.savefig(destination.with_suffix(".png"), dpi=180)
svg_path = destination.with_suffix(".svg")
fig.savefig(svg_path)
svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text().splitlines()) + "\n")
plt.close(fig)
print(json.dumps({key: value for key, value in summary.items() if key != "runs"}, indent=2))
