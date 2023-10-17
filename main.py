import datetime
import ics


def read_cal():
    path = "cal.ics"
    file = open(path, "r", encoding="utf-8")
    cal = ics.Calendar(file.read())
    file.close()
    return cal


def clear_cal(cal: ics.Calendar):
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
    calendar = clear_cal(read_cal())
    out = open("new.ics", "w", encoding="utf-8")
    out.write(calendar.serialize())
    out.close()
