from datetime import datetime, timedelta



def get_birthdays_per_week(users, c_time=datetime.now()):

    mon, tue, wen, thu, fri =  [], [], [], [], []
    b_dict = {'Monday': mon, 'Tuesday': tue, 'Wendsday': wen, 'Thuersday': thu, 'Friday': fri}

    for user in users:
        
        birthday_list = str(user.get('birthday').date()).split('-')
        birthday_list.pop(0)
        birthday = datetime(year=c_time.year, month=int(birthday_list[0]), day=int(birthday_list[1]))
        interval = timedelta(days=6)
        future_time = c_time + interval
        alt_interval = timedelta(days=1)
        past_time = c_time - alt_interval

        if past_time <= birthday < future_time:
                
            if birthday.weekday() == 1:
                tue.append(user.get('name'))

            elif birthday.weekday() == 2:
                wen.append(user.get('name'))

            elif birthday.weekday() == 3:
                thu.append(user.get('name'))

            elif birthday.weekday() == 4:
                fri.append(user.get('name'))

            else:
                mon.append(user.get('name'))

    for day, lst in b_dict.items():

        if lst:
            print(f"{day}: {', '.join(lst)}")
        else:
            print(f"{day}:")
                

c_time = datetime.now()

users = [{'name': 'Kolya', 'birthday': datetime(year=1991, month=7, day=10)},
         {'name': 'Ivan', 'birthday': datetime(year=1987, month=7, day=11)},
         {'name': 'Peter', 'birthday': datetime(year=1964, month=7, day=12)},
         {'name': 'Jack', 'birthday': datetime(year=1999, month=7, day=13)},
         {'name': 'Olya', 'birthday': datetime(year=1997, month=7, day=14)},
         {'name': 'Slava', 'birthday': datetime(year=1986, month=7, day=15)},
         {'name': 'Serg', 'birthday': datetime(year=1974, month=7, day=16)},
         {'name': 'Alex', 'birthday': datetime(year=1996, month=7, day=17)},
         {'name': 'Pavel', 'birthday': datetime(year=1998, month=7, day=18)}]

get_birthdays_per_week(users)