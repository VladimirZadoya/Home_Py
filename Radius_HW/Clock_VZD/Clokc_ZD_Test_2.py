import datetime


now_utc = datetime.datetime.utcnow()


offsets = {
    'Москва': 3,
    'Нью-Йорк': -4,
    'Токио': 9,
    'Казахстан': 6,
    'Санкт-Петербург': 3,
    'Украина': 2
}


for city, offset in offsets.items():
    
    local_time = now_utc + datetime.timedelta(hours=offset)
    print(f'Время в {city}: {local_time.strftime("%Y-%m-%d %H:%M:%S")}')
