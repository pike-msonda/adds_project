import datetime

def to_datetime(dtstring, dtformat):
    """
    """
    return datetime.datetime.strptime(dtstring, dtformat)

def create_conditions(columns, value, condition,  operator='='):
    condtions = ''
    for i in range(len(columns)):
       condtions += condtions+' '+columns[i] + operator + value +' '+condition
    return condtions;
