import django


def calc_days_left(start_date,end_date):
    delta = end_date - start_date
    return delta.days