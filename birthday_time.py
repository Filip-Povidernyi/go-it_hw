from datetime import datetime, timedelta



def get_birthdays_per_week(users, c_time=datetime.now()):

    mon, tue, wen, thu, fri =  [], [], [], [], []
    b_dict = {'Monday': mon, 'Tuesday': tue, 'Wendsday': wen, 'Thuersday': thu, 'Friday': fri}

    for user in users:

        interval = timedelta(days=6)
        future_time = c_time + interval
        alt_interval = timedelta(days=1)
        past_time = c_time - alt_interval

        if past_time <= user.get('birthday') < future_time:
                
            if user.get('birthday').weekday() == 1:
                tue.append(user.get('name'))

            elif user.get('birthday').weekday() == 2:
                wen.append(user.get('name'))

            elif user.get('birthday').weekday() == 3:
                thu.append(user.get('name'))

            elif user.get('birthday').weekday() == 4:
                fri.append(user.get('name'))

            else:
                mon.append(user.get('name'))

    for day, lst in b_dict.items():

        if lst:
            print(f"{day}: {', '.join(lst)}")
        else:
            print(f"{day}:")
                

c_time = datetime.now()

users = [{'name': 'Kolya', 'birthday': datetime(year=c_time.year, month=7, day=5)},
         {'name': 'Ivan', 'birthday': datetime(year=c_time.year, month=7, day=14)},
         {'name': 'Peter', 'birthday': datetime(year=c_time.year, month=7, day=7)},
         {'name': 'Jack', 'birthday': datetime(year=c_time.year, month=7, day=9)},
         {'name': 'Olya', 'birthday': datetime(year=c_time.year, month=7, day=8)},
         {'name': 'Slava', 'birthday': datetime(year=c_time.year, month=7, day=10)},
         {'name': 'Serg', 'birthday': datetime(year=c_time.year, month=7, day=11)},
         {'name': 'Alex', 'birthday': datetime(year=c_time.year, month=7, day=13)},
         {'name': 'Pavel', 'birthday': datetime(year=c_time.year, month=7, day=12)}]

get_birthdays_per_week(users)