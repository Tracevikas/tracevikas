"""Scrape the public contribution calendar into data/contributions.json (no token needed)."""
import json
import os
import re
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GH_USER", "Tracevikas")
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "contributions.json"


def count_from_tooltip(text: str) -> int:
    m = re.match(r"\s*([\d,]+)\s+contribution", text)
    return int(m.group(1).replace(",", "")) if m else 0


def streaks(days):
    longest = run = 0
    for d in days:
        run = run + 1 if d["count"] else 0
        longest = max(longest, run)
    # current streak: an empty "today" doesn't break it yet
    tail = days[:-1] if days and days[-1]["count"] == 0 else days
    current = 0
    for d in reversed(tail):
        if not d["count"]:
            break
        current += 1
    return current, longest


def main():
    url = f"https://github.com/users/{USERNAME}/contributions"
    html = requests.get(url, headers={"User-Agent": "profile-readme-bot"}, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")

    tips = {t.get("for"): t.get_text(strip=True) for t in soup.find_all("tool-tip")}
    days = [
        {
            "date": td["data-date"],
            "level": int(td.get("data-level", 0)),
            "count": count_from_tooltip(tips.get(td.get("id"), "")),
        }
        for td in soup.select("td.ContributionCalendar-day[data-date]")
    ]
    days.sort(key=lambda d: d["date"])
    if not days:
        raise SystemExit("No contribution cells found - GitHub markup may have changed.")

    total = sum(d["count"] for d in days)
    current, longest = streaks(days)
    best = max(days, key=lambda d: d["count"])

    data = {
        "username": USERNAME,
        "generated": date.today().isoformat(),
        "total": total,
        "current_streak": current,
        "longest_streak": longest,
        "best_day": best,
        "active_days": sum(1 for d in days if d["count"]),
        "days": days,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1))
    print(f"{len(days)} days, {total} contributions, streak {current}/{longest}")


if __name__ == "__main__":
    main()
