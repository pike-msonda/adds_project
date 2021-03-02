import datetime

def to_datetime(dtstring, dtformat):
    """
    """
    return datetime.datetime.strptime(dtstring, dtformat)
