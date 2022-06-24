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
        if not (e.name == "Практика" or e.name == "Военная кафедра"):
            e.alarms[0].trigger = datetime.timedelta(minutes=-15)
            new_cal.events.add(e)
    return new_cal


if __name__ == '__main__':
    calendar = clear_cal(read_cal())
    out = open("new.ics", "w", encoding="utf-8")
    out.write(str(calendar))
    out.close()
