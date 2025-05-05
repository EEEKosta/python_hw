bugs = [
    "Ошибка 1 — Hi",
    "Ошибка 2 — Low",
    "Ошибка 1 — Mid",
    "Ошибка 1 — low",
    "Ошибка 1 — High"
]

priority_bugs = {
    'high': 0,
    'mid': 1,
    'low': 2
}

def get_priority(bug):
    parts = bug.split('—')
    if len(parts) > 1:
        priority = parts[1].strip().lower()
        return priority_bugs.get(priority, 999)
    return 999

sorted_bugs = sorted(bugs, key=get_priority)

for bug in sorted_bugs:
    print(bug)