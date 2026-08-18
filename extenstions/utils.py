import pytz

from . import jalali
from jalali_date import datetime2jalali, date2jalali


def jalali_converter(time):
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time = datetime2jalali(time).strftime('%H:%M')
    output = "{}/{}/{} ساعت : {}".format(
        time_to_tuple[0],
        time_to_tuple[1],
        time_to_tuple[2],
        time,
    )
    return output


def jalali_converter_date(time):
    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    output = "{}/{}/{}".format(
        time_to_tuple[0],
        time_to_tuple[1],
        time_to_tuple[2],
    )
    return output


from datetime import datetime, timedelta

from datetime import datetime, timedelta, date, timezone


def time_ago(timestamp):
    now = datetime.now(tz=pytz.timezone('Asia/Tehran'))
    diff = now - timestamp
    seconds = diff.total_seconds()
    minutes = seconds // 60
    hours = minutes // 60
    days = diff.days
    weeks = days // 7

    if int(seconds) < 60:
        return "همین الان"
    elif int(minutes) < 60:
        return f"{int(minutes)} دقیقه قبل"
    elif int(hours) < 24:
        return f"{int(hours)} ساعت قبل"
    elif int(days) < 7:
        return f"{days} روز قبل"
    elif int(weeks) <= 4:
        return f"{weeks} هفته قبل"
    else:
        months = days // 30
        if int(months) < 12:
            return f"{months} ماه قبل"
        years = months // 12
        return f"{years} سال قبل"
