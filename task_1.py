time ='1h 45m,360s,25m,30m 120s,2h 60s'
def calc():
    total = 0
    parts= time.split(',')
    for part in parts:
        subparts=part.split()
        for sub in subparts:
            if 'h' in sub:
                hours = int(sub.replace('h',''))
                total += hours * 60
            elif 'm' in sub:
                minutes = int(sub.replace('m',''))
                total += minutes
            elif 's' in sub:
                seconds = int(sub.replace('s',''))
                total += seconds // 60
    return total

print(calc())
    
