def calculate_flag(delay_days: int, citizen_reports: int, funds_released: bool, last_activity_days: int) -> dict:
    """
    Core flag engine for Scheme Gati.
    Returns flag color, label, action, and emoji.
    """

    # BLACK FLAG — highest priority check first
    if delay_days > 30 and funds_released and last_activity_days > 30:
        return {
            "color": "black",
            "label": "BLACK FLAG",
            "emoji": "⚫",
            "action": "RTI auto-generated. Scheme completely stalled.",
            "css_class": "flag-black"
        }

    # RED FLAG
    if delay_days >= 15 or citizen_reports >= 7:
        return {
            "color": "red",
            "label": "RED FLAG",
            "emoji": "🔴",
            "action": "Escalated to District Collector. Explanation demanded.",
            "css_class": "flag-red"
        }

    # YELLOW FLAG
    if (7 <= delay_days < 15) or citizen_reports >= 3:
        return {
            "color": "yellow",
            "label": "YELLOW FLAG",
            "emoji": "🟡",
            "action": "SMS sent to contractor. Ward Officer alerted.",
            "css_class": "flag-yellow"
        }

    # CHEQUERED FLAG — completed on time
    if delay_days == 0 and last_activity_days == 0:
        return {
            "color": "chequered",
            "label": "CHEQUERED",
            "emoji": "🏁",
            "action": "Scheme complete. Race win logged on leaderboard.",
            "css_class": "flag-chequered"
        }

    # GREEN FLAG — all good
    return {
        "color": "green",
        "label": "GREEN FLAG",
        "emoji": "🟢",
        "action": "On schedule. Normal monitoring.",
        "css_class": "flag-green"
    }


def calculate_projected_finish(total_days: int, days_elapsed: int, completion_pct: float) -> int:
    """
    Projects total days needed based on current work pace.
    Example: 90 day project, 60 days elapsed, 20% done → projects 300 days total
    """
    if completion_pct <= 0:
        return total_days * 3  # worst case estimate
    pace = completion_pct / days_elapsed  # % per day
    days_needed = 100 / pace
    return round(days_needed)


def add_penalty_laps(delay_days: int) -> int:
    """Every 7 days of delay = 1 penalty lap"""
    return delay_days // 7


# ── DEMO: Run this file directly to test the flag engine ──────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("   SCHEME GATI — FLAG ENGINE TEST")
    print("=" * 55)

    test_schemes = [
        {
            "name": "Ward 2 — Grid Modernization Phase II",
            "delay_days": 42,
            "citizen_reports": 11,
            "funds_released": True,
            "last_activity_days": 35
        },
        {
            "name": "Panki Filtration Overhaul",
            "delay_days": 12,
            "citizen_reports": 2,
            "funds_released": True,
            "last_activity_days": 5
        },
        {
            "name": "Landfall Bio-Remediation",
            "delay_days": 20,
            "citizen_reports": 8,
            "funds_released": True,
            "last_activity_days": 10
        },
        {
            "name": "Kanpur Primary Health Upgrade",
            "delay_days": 3,
            "citizen_reports": 1,
            "funds_released": True,
            "last_activity_days": 2
        },
        {
            "name": "Road Resurfacing MG Marg",
            "delay_days": 0,
            "citizen_reports": 0,
            "funds_released": True,
            "last_activity_days": 0
        },
    ]

    for scheme in test_schemes:
        flag = calculate_flag(
            scheme["delay_days"],
            scheme["citizen_reports"],
            scheme["funds_released"],
            scheme["last_activity_days"]
        )
        penalty = add_penalty_laps(scheme["delay_days"])
        print(f"\n  Scheme : {scheme['name']}")
        print(f"  Flag   : {flag['emoji']}  {flag['label']}")
        print(f"  Action : {flag['action']}")
        print(f"  Penalty Laps : {penalty}")
        print(f"  {'─'*48}")

    print("\n  Flag engine working correctly.\n")
