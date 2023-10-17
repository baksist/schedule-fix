#!/usr/bin/env python3

import sys
import ics
from os.path import splitext

def fix_calendar(cal: ics.Calendar):
    
    new_cal = ics.Calendar()
    
    for e in cal.events:
    
        if (e.name == "Библиотеки  машинного обучения (ПР)"):
            e.end = e.end.shift(hours=+3, minutes=+40)
            e.begin = e.begin.shift(hours=+3, minutes=+40)
            e.location = "СДО"
    
        if ("Интеллектуальные системы и технологии" in e.name or 
            e.name == "Технологии обеспечения информационной безопасности (ПР)" or
            e.name == "Технологии обеспечения информационной безопасности (ЛАБ)"):
            e.location = "Discord"
    
        if e.name == "Социология и педагогика высшей школы (ЛК)":
            continue
        
        new_cal.events.add(e)
    return new_cal


if __name__ == '__main__':
    path_to_calendar = sys.argv[1]
    
    with open(path_to_calendar, "r", encoding="utf-8") as file:
        calendar = ics.Calendar(file.read())
    
    fixed_calendar = fix_calendar(calendar)
    
    with open(f"{splitext(path_to_calendar)[0]}_fixed.ics", "w", encoding="utf-8") as file:
        file.write(fixed_calendar.serialize())