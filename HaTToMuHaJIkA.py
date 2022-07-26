import datetime
from datetime import  date, datetime, timedelta
import dateutil.relativedelta
from dateutil.relativedelta import relativedelta

class DF:
    months = ['января', 'февраля', 'марта', 'апреля', "мая", "июня", "июля", "августа", "сентября", "октября", 'ноября', 'декабря']
    week = ['понедельник','вторник','среду','четверг','пятницу','субботу','воскресенье']

    def year(str):
        ytxt = ['года']
        for p in ytxt:
            if p in str:
                return str[str.find(p) - 5:str.find(p) - 1]
        else:
            return None

    def month(str):
        for p in DF.months:
            if p in str:
                return DF.months.index(p) + 1
        return None

    def day(str):
        for p in DF.months:
            if p in str:
                if str[str.find(p) - 3].isdigit():
                    return str[str.find(p) - 3:str.find(p) - 1]
                else:
                    return str[str.find(p) - 2:str.find(p) - 1]
        return None

    def time(str):
        global MESSAGE
        if 'утром' in str or 'вечером' in str or 'ночью' in str or 'днем' in str:
            if 'утром' in str:
                MESSAGE['DATE']['hour'] = 9
                MESSAGE['DATE']['minute'] = 0
            elif 'днем' in str:
                MESSAGE['DATE']['hour'] = 12
                MESSAGE['DATE']['minute'] = 0
            elif 'вечером' in str:
                MESSAGE['DATE']['hour'] = 18
                MESSAGE['DATE']['minute'] = 0
            elif 'ночью' in str:
                MESSAGE['DATE']['hour'] = 23
                MESSAGE['DATE']['minute'] = 0
        elif str.rfind(':') and str[str.rfind(':')-1].isdigit() and str[str.rfind(':')+1].isdigit():
            time = str[str.rfind(':') - 2:str.rfind(':') + 3]
            if time[0] == ' ':
                MESSAGE['DATE']['hour'] = time[1:2]
                MESSAGE['DATE']['minute'] = time[3:]
            else:
                MESSAGE['DATE']['hour'] = time[:2]
                MESSAGE['DATE']['minute'] = time[3:]

    def DoW(str):
        for i in DF.week:
            if i in str:
                if datetime.now().weekday()<DF.week.index(i):
                    return DF.week.index(i)-datetime.now().weekday()

def DD(str):
    months = [ 'января', 'февраля', 'марта', 'апреля', "мая", "июня", "июля", "августа", "сентября", "октября", 'декабря']
    week = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
    for i in months:
        if i in str:
            return str[:str.find(i)-3]
    for i in week:
        if i in str:
            return str[:str.find(i)-3]

    if 'через' in str:
        return str[:str.find('через') - 1]
    else:
        for i in str:
            if i.isdigit():
                str = str[:str.find(i) - 1]
                if str[-1] == 'в' and str[-2] == ' ':
                    str = str[:-2]
                return str

    if 'завтра' in str:
        return str[:str.find('завтра') - 1]
    elif 'послезавтра' in str:
        return str[:str.find('послезавтра') - 1]
    else:
        return str

def DT(list):
    global current_time
    if len(list)==1:
        if list[0]=='год':
            current_time += timedelta(years=1)
        elif list[0] == 'час':
            current_time += timedelta(hours=1)
        elif list[0] == 'день':
            current_time += timedelta(days=1)
        elif list[0]=='месяц':
            current_time += timedelta(months=1)
        elif list[0] == 'минуту':
            current_time += timedelta(minutes=1)
        elif list[0]=='неделю':
            current_time += timedelta(days=7)
    elif  list[1] == 'года' or list[1] == 'лет':
        current_time += timedelta(years=int(list[0]))
    elif list[1] == 'месяца' or list[1] == 'месяцев':
        current_time += timedelta(months=int(list[0]))
    elif list[1] == 'месяц':
        current_time += timedelta(months=1)
    elif list[1] == 'дня' or list[1] == 'дней':
        current_time += timedelta(days=int(list[0]))
    elif list[1] == 'день':
        current_time += timedelta(days=1)
    elif list[1] == 'часа' or list[1] == 'часов':
        current_time += timedelta(hours=int(list[0]))
    elif list[1] == 'час':
        current_time += timedelta(hours=1)
    elif list[1] == 'минут' or list[1] == 'минуты':
        current_time += timedelta(minutes=int(list[0]))
    elif list[1] == 'минуту':
        current_time += timedelta(minutes=1)
    elif list[1]=='недель':
            current_time += timedelta(days=7*list[0])

def DC():
    global MESSAGE
    c=datetime(int(MESSAGE['DATE']['year']),int(MESSAGE['DATE']['month']),int(MESSAGE['DATE']['day']),int(MESSAGE['DATE']['hour']),int(MESSAGE['DATE']['minute']))

    if c>datetime.now():
        return True
    else:
        return False

def MDT(c):
    MESSAGE['DATE']['year'] = c.year
    MESSAGE['DATE']['month'] = c.month
    MESSAGE['DATE']['day'] = c.day
    MESSAGE['DATE']['hour'] = c.hour
    MESSAGE['DATE']['minute'] = c.minute

def addToInt():
    global MESSAGE
    int(MESSAGE['DATE']['year'])
    int(MESSAGE['DATE']['month'])
    int(MESSAGE['DATE']['day'])
    int(MESSAGE['DATE']['hour'])
    int(MESSAGE['DATE']['minute'])

def SD():
    global msgin
    while '  ' in msgin:
        msgin=msgin.replace('  ',' ')

def chis(str):
    str=str[str.rfind('числа')-3:str.rfind('числа')-1]
    if str[0]==' ':
        str=str[1:]
    c = datetime.now()
    if int(str)<int(datetime.now().day):
        c += relativedelta(months=1)
        c -= relativedelta(days= c.day-int(str))
        return c
    else:
        c += timedelta(days=int(str) - c.day)
        return c

def z():
    global MESSAGE
    num=[1,2,3,4,5,6,7,8,9]
    snum=['1','2','3','4','5','6','7','8','9']
    if MESSAGE['DATE']['month'] in num or MESSAGE['DATE']['month'] in snum :
        MESSAGE['DATE']['month'] = '0' + str(MESSAGE['DATE']['month'])

    if  MESSAGE['DATE']['day'] in num or MESSAGE['DATE']['day'] in snum:
        MESSAGE['DATE']['day'] = '0' + str(MESSAGE['DATE']['day'])

    if  MESSAGE['DATE']['minute'] in num:
        MESSAGE['DATE']['minute'] = '0' + MESSAGE['DATE']['minute']



try:
    msgin = input()
    SD()
    MESSAGE = {'STATUS': None, 'DATE': {'year': None, 'month': None, 'day': None, 'hour': None, 'minute': None},
               'TEXT': None}
    if 'через' in msgin:
        str = msgin[msgin.rfind('через') + 6:]
        list = str.split(' ')
        current_time = datetime.now()
        while list:
            DT(list[:2])
            list.remove(list[0])
            if list:
                list.remove(list[0])
        MDT(current_time)
    elif 'завтра' in msgin or 'послезавтра' in msgin:
        current_time = datetime.now()
        if 'завтра' in msgin:
            current_time += timedelta(days=1)
        if 'послезавтра' in msgin:
            current_time += timedelta(days=2)
        MDT(current_time)
    elif 'числа' in msgin:
        c=chis(msgin)
        MDT(c)
    elif 'понедельник' in msgin or'вторник' in msgin or 'среду' in msgin or 'четверг' in msgin or 'пятницу' in msgin or 'субботу' in msgin or'воскресенье' in msgin:
        current_time = datetime.now()
        current_time+= relativedelta(days=DF.DoW(msgin))
        MDT(current_time)
        DF.time(msgin)
    else:
        MESSAGE['DATE']['year'] = DF.year(msgin)
        MESSAGE['DATE']['month'] =DF.month(msgin)
        MESSAGE['DATE']['day'] = DF.day(msgin)
        DF.time(msgin)
        if not MESSAGE['DATE']['year']:
            MESSAGE['DATE']['year'] = datetime.now().year
        if not MESSAGE['DATE']['month']:
            MESSAGE['DATE']['month'] = datetime.now().month
        if not MESSAGE['DATE']['day']:
            MESSAGE['DATE']['day'] = datetime.now().day
            if not DC():
                MESSAGE['DATE']['day'] += 1
        if not MESSAGE['DATE']['hour']:
            MESSAGE['DATE']['hour'] = datetime.now().hour
        if not MESSAGE['DATE']['minute']:
            MESSAGE['DATE']['minute'] = datetime.now().minute
        if not DC():
            MESSAGE['DATE']['year'] += 1
    MESSAGE['TEXT'] = DD(msgin)
    MESSAGE['STATUS'] = 'SUCCESS'
    print(MESSAGE)
except Exception as e:
    MESSAGE['STATUS'] = 'ERROR'
    MESSAGE['TEXT'] = e
    print(MESSAGE)