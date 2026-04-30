"""
Scheme Gati — Demo Seed Data
12 realistic schemes across 4 wards in Kanpur Urban.
All flag states represented for a complete demo.
"""
SCHEMES = [
    # ── WARD 1 — KIDWAI NAGAR ─────────────────────────────────────────────────
    {
        "id": "UP/KNP/W1/2024/001",
        "name": "Road Resurfacing — MG Marg",
        "ward": "Ward 1 — Kidwai Nagar",
        "type": "Infrastructure",
        "contractor": "M/S Bharat Roads Pvt. Ltd.",
        "budget": "4,80,00,000",
        "funds_released": "2,40,00,000",
        "start_date": "01 Jan 2024",
        "deadline": "31 Mar 2024",
        "delay_days": 0,
        "completion_pct": 100,
        "citizen_reports": 0,
        "last_activity_days": 0,
        "milestones": ["Site clearance", "Base layer", "Bitumen layering", "Road markings", "Handover"],
        "current_lap": 5,
        "flag": "chequered",
        "note": "Completed on time. Race win."
    },
    {
        "id": "UP/KNP/W1/2024/002",
        "name": "Primary School Building — Sector 3",
        "ward": "Ward 1 — Kidwai Nagar",
        "type": "Education",
        "contractor": "M/S Vidya Constructions",
        "budget": "6,20,00,000",
        "funds_released": "3,10,00,000",
        "start_date": "15 Feb 2024",
        "deadline": "15 Aug 2024",
        "delay_days": 4,
        "completion_pct": 62,
        "citizen_reports": 1,
        "last_activity_days": 3,
        "milestones": ["Foundation", "Walls", "Roofing", "Electrical", "Finishing", "Handover"],
        "current_lap": 3,
        "flag": "green",
        "note": "On schedule. Minor delay within tolerance."
    },

    # ── WARD 2 — ARYA NAGAR ───────────────────────────────────────────────────
    {
        "id": "UP/KNP/W2/2024/003",
        "name": "Grid Modernization Phase II",
        "ward": "Ward 2 — Arya Nagar",
        "type": "Smart City",
        "contractor": "M/S Shakti Infrastructure Pvt. Ltd.",
        "budget": "14,28,00,000",
        "funds_released": "9,80,00,000",
        "start_date": "12 Mar 2024",
        "deadline": "10 Sep 2024",
        "delay_days": 42,
        "completion_pct": 18,
        "citizen_reports": 11,
        "last_activity_days": 35,
        "milestones": ["Survey", "Equipment install", "Cable laying", "Testing", "Commissioning"],
        "current_lap": 1,
        "flag": "black",
        "note": "STALLED. Funds released. Zero activity for 35 days. RTI auto-generated."
    },
    {
        "id": "UP/KNP/W2/2024/004",
        "name": "Panki Water Treatment Upgrade",
        "ward": "Ward 2 — Arya Nagar",
        "type": "Water",
        "contractor": "M/S AquaTech Solutions",
        "budget": "8,12,40,000",
        "funds_released": "4,06,20,000",
        "start_date": "05 Apr 2024",
        "deadline": "05 Oct 2024",
        "delay_days": 12,
        "completion_pct": 44,
        "citizen_reports": 2,
        "last_activity_days": 5,
        "milestones": ["Excavation", "Pipeline", "Treatment unit", "Testing", "Handover"],
        "current_lap": 2,
        "flag": "yellow",
        "note": "12 days behind. Contractor SMS sent."
    },

    # ── WARD 3 — CIVIL LINES ──────────────────────────────────────────────────
    {
        "id": "UP/KNP/W3/2024/005",
        "name": "Landfall Bio-Remediation",
        "ward": "Ward 3 — Civil Lines",
        "type": "Environment",
        "contractor": "M/S GreenEarth Pvt. Ltd.",
        "budget": "22,50,00,000",
        "funds_released": "11,25,00,000",
        "start_date": "20 Jan 2024",
        "deadline": "20 Jul 2024",
        "delay_days": 20,
        "completion_pct": 30,
        "citizen_reports": 8,
        "last_activity_days": 10,
        "milestones": ["Assessment", "Excavation", "Bio-treatment", "Soil testing", "Closure"],
        "current_lap": 2,
        "flag": "red",
        "note": "RED FLAG. 20 days delayed + 8 citizen reports. DC alerted."
    },
    {
        "id": "UP/KNP/W3/2024/006",
        "name": "Civil Lines Footpath Renovation",
        "ward": "Ward 3 — Civil Lines",
        "type": "Infrastructure",
        "contractor": "M/S Urban Pave Co.",
        "budget": "1,85,00,000",
        "funds_released": "92,50,000",
        "start_date": "01 Mar 2024",
        "deadline": "30 Apr 2024",
        "delay_days": 3,
        "completion_pct": 80,
        "citizen_reports": 0,
        "last_activity_days": 1,
        "milestones": ["Demolition", "Base prep", "Tiling", "Finishing"],
        "current_lap": 3,
        "flag": "green",
        "note": "Nearly complete. On track."
    },
    {
        "id": "UP/KNP/W3/2024/007",
        "name": "Solar Street Lighting — Phase I",
        "ward": "Ward 3 — Civil Lines",
        "type": "Energy",
        "contractor": "M/S SunPower Infra",
        "budget": "3,40,00,000",
        "funds_released": "1,70,00,000",
        "start_date": "10 Feb 2024",
        "deadline": "10 May 2024",
        "delay_days": 9,
        "completion_pct": 55,
        "citizen_reports": 4,
        "last_activity_days": 7,
        "milestones": ["Procurement", "Foundation poles", "Panel install", "Wiring", "Testing"],
        "current_lap": 2,
        "flag": "yellow",
        "note": "9 days delayed. 4 reports. Yellow flag active."
    },

    # ── WARD 4 — GOVIND NAGAR ─────────────────────────────────────────────────
    {
        "id": "UP/KNP/W4/2024/008",
        "name": "Kanpur Primary Health Centre Upgrade",
        "ward": "Ward 4 — Govind Nagar",
        "type": "Health",
        "contractor": "M/S MediConstruct Pvt. Ltd.",
        "budget": "9,60,00,000",
        "funds_released": "4,80,00,000",
        "start_date": "01 Feb 2024",
        "deadline": "01 Aug 2024",
        "delay_days": 3,
        "completion_pct": 71,
        "citizen_reports": 1,
        "last_activity_days": 2,
        "milestones": ["Demolition", "Structure", "OT setup", "Equipment", "Inspection", "Handover"],
        "current_lap": 4,
        "flag": "green",
        "note": "Good progress. Minor delay."
    },
    {
        "id": "UP/KNP/W4/2024/009",
        "name": "PM Awas Yojana — Block C Housing",
        "ward": "Ward 4 — Govind Nagar",
        "type": "Housing",
        "contractor": "M/S Nirmaan Builders",
        "budget": "18,00,00,000",
        "funds_released": "12,00,00,000",
        "start_date": "15 Nov 2023",
        "deadline": "15 May 2024",
        "delay_days": 38,
        "completion_pct": 22,
        "citizen_reports": 9,
        "last_activity_days": 40,
        "milestones": ["Foundation", "Plinth", "Columns", "Slab", "Walls", "Finishing", "Handover"],
        "current_lap": 2,
        "flag": "black",
        "note": "STALLED. 38 days. 9 reports. Safety Car triggered. RTI generated."
    },
    {
        "id": "UP/KNP/W4/2024/010",
        "name": "Drainage Canal Desilting",
        "ward": "Ward 4 — Govind Nagar",
        "type": "Sanitation",
        "contractor": "M/S ClearFlow Infra",
        "budget": "2,10,00,000",
        "funds_released": "1,05,00,000",
        "start_date": "01 Apr 2024",
        "deadline": "30 Apr 2024",
        "delay_days": 0,
        "completion_pct": 100,
        "citizen_reports": 0,
        "last_activity_days": 0,
        "milestones": ["Inspection", "Desilting", "Cleaning", "Verification"],
        "current_lap": 4,
        "flag": "chequered",
        "note": "Completed on time. Race win."
    },
    {
        "id": "UP/KNP/W4/2024/011",
        "name": "Community Centre Renovation",
        "ward": "Ward 4 — Govind Nagar",
        "type": "Social",
        "contractor": "M/S Civil Pride Works",
        "budget": "5,50,00,000",
        "funds_released": "2,75,00,000",
        "start_date": "10 Mar 2024",
        "deadline": "10 Jul 2024",
        "delay_days": 17,
        "completion_pct": 35,
        "citizen_reports": 6,
        "last_activity_days": 8,
        "milestones": ["Demolition", "Structure repair", "Interior", "Exterior", "Inauguration"],
        "current_lap": 2,
        "flag": "red",
        "note": "17 days delayed. 6 reports. RED FLAG. Explanation demanded."
    },
    {
        "id": "UP/KNP/W4/2024/012",
        "name": "E-Waste Collection Centre",
        "ward": "Ward 4 — Govind Nagar",
        "type": "Environment",
        "contractor": "M/S EcoDispose Ltd.",
        "budget": "1,20,00,000",
        "funds_released": "60,00,000",
        "start_date": "01 Mar 2024",
        "deadline": "01 Jun 2024",
        "delay_days": 5,
        "completion_pct": 68,
        "citizen_reports": 0,
        "last_activity_days": 3,
        "milestones": ["Site prep", "Structure", "Equipment", "Handover"],
        "current_lap": 3,
        "flag": "green",
        "note": "On schedule."
    },
]

# Ward leaderboard data
WARD_STANDINGS = [
    {"rank": 1, "ward": "Ward 1 — Kidwai Nagar",  "total": 2, "completed": 1, "ontime_pct": 85, "avg_delay": 2},
    {"rank": 2, "ward": "Ward 3 — Civil Lines",   "total": 3, "completed": 0, "ontime_pct": 62, "avg_delay": 10},
    {"rank": 3, "ward": "Ward 4 — Govind Nagar",  "total": 5, "completed": 2, "ontime_pct": 48, "avg_delay": 18},
    {"rank": 4, "ward": "Ward 2 — Arya Nagar",    "total": 2, "completed": 0, "ontime_pct": 30, "avg_delay": 27},
]

if __name__ == "__main__":
    from flag_engine import calculate_flag, add_penalty_laps

    print("\n" + "=" * 60)
    print("   SCHEME GATI — DEMO SEED DATA SUMMARY")
    print("=" * 60)

    flag_counts = {"green": 0, "yellow": 0, "red": 0, "black": 0, "chequered": 0}

    for s in SCHEMES:
        flag = calculate_flag(s["delay_days"], s["citizen_reports"], True, s["last_activity_days"])
        penalty = add_penalty_laps(s["delay_days"])
        flag_counts[flag["color"]] = flag_counts.get(flag["color"], 0) + 1
        print(f"\n  {flag['emoji']}  {s['name']}")
        print(f"     Ward     : {s['ward']}")
        print(f"     Budget   : ₹{s['budget']}")
        print(f"     Delay    : {s['delay_days']} days | Reports: {s['citizen_reports']} | Penalty laps: {penalty}")

    print("\n" + "─" * 60)
    print(f"  🟢 Green     : {flag_counts['green']}")
    print(f"  🟡 Yellow    : {flag_counts['yellow']}")
    print(f"  🔴 Red       : {flag_counts['red']}")
    print(f"  ⚫ Black     : {flag_counts['black']}")
    print(f"  🏁 Chequered : {flag_counts['chequered']}")
    print(f"\n  Total schemes loaded : {len(SCHEMES)}")
    print("─" * 60)
    print("\n  Seed data ready for demo.\n")
