days = ['L1 9-11 13-16', 'M2 9-12 15-18', 'M3 9-13 16-20', 'J4 8-12 13-16', 'V5 8-10 12-16', 'L8 10-12 15-19', 'M9 8-10 12-16', 'M10 9-13 15-17', 'J11 8-12 15-18', 'V12 8-12 15-17', 'L15 10-13 15-19', 'M16 10-13 15-17', 'M17 9-12 13-16', 'J18 9-13 15-17', 'V19 9-11 13-16', 'L22 8-10 12-16', 'M23 8-11 13-16', 'M24 8-11 13-17', 'J25 8-12 14-17', 'V26 9-11 14-17', 'L29 8-11 13-16', 'M30 9-11 14-17', 'M31 8-11 13-16']

def parse_day(line):
    parts = line.split()
    day_code = parts[0]
    wd = day_code[0]
    day_num = int(day_code[1:])
    courses = []
    for p in parts[1:]:
        a, b = p.split('-')
        courses.append((int(a), int(b)))
    return day_code, wd, day_num, courses

def first_sport_slot(courses):
    for start in range(7, 17):
        end = start + 3
        ok = True
        for c1, c2 in courses:
            if not (end <= c1 or start >= c2):
                ok = False
                break
        if ok:
            return f"{start+1}-{start+2}"
    return None

def day_index(day_num, wd, m_count_in_week):
    week = (day_num - 1) // 7
    if wd == 'L':
        dow = 0
    elif wd == 'M':
        dow = 1 if m_count_in_week == 1 else 2
    elif wd == 'J':
        dow = 3
    else:  # 'V'
        dow = 4
    return week * 5 + dow

def solve(lines):
    candidates = []
    current_week = None
    m_count = 0

    for line in lines:
        day_code, wd, day_num, courses = parse_day(line)
        week = (day_num - 1) // 7
        if week != current_week:
            current_week = week
            m_count = 0

        if wd == 'M':
            m_count += 1
            m_pos = m_count
        else:
            m_pos = 0

        slot = first_sport_slot(courses)
        if slot:
            idx = day_index(day_num, wd, m_pos)
            candidates.append((idx, day_code, slot))

    result = []
    last_idx = None
    for idx, day_code, slot in candidates:
        if last_idx is None or idx - last_idx >= 2:
            result.append(f"{day_code}:{slot}")
            last_idx = idx

    return " ".join(result)

solve(days)
