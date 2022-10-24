def add_time(start_time,add_time,weekday=None):
    
    weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    start_hours = int(start_time.split(":")[0])
    start_minutes = int(start_time.split(':')[1].split()[0])

    add_hours = int(add_time.split(":")[0])
    add_minutes = int(add_time.split(':')[1].split()[0])

    time_minutes = start_minutes + add_minutes
    time_hours = start_hours + add_hours

    days = time_hours//24
    if add_hours > 24:
        add_to_hours =  time_hours - (days*24)
        if time_minutes > 59:
            time_minutes = time_minutes - 60
            add_to_hours += 1 
        display_time = "%d"%(add_to_hours,) + ":" + "%02d"%(time_minutes,)
    elif time_minutes > 59:
        time_minutes = time_minutes - 60
        time_hours+=1
        if time_hours-24 < 0:
            display_time = "%d"%(time_hours,) + ":" + "%02d"%(time_minutes,)
        else:
            display_time = "%d"%(time_hours-24,) + ":" + "%02d"%(time_minutes,)
    else:
        display_time = "%d"%(time_hours-24,) + ":" + "%02d"%(time_minutes,)
    if start_time[-2:] == 'PM':
        if 12 < time_hours < 24:
            days+=1
            display_time = "%d"%(time_hours-12,) + ":" + "%02d"%(time_minutes,) + ' ' + 'AM'
        elif time_hours < 12:
                 display_time = "%d"% (time_hours,) + ":" + "%02d"%(time_minutes,) + ' ' + 'PM'
        elif time_hours == 12:
            display_time = "%d"% (time_hours,) + ":" + "%02d"%(time_minutes,) + ' ' + 'AM'
        elif time_hours > 24:
            days+=1
            time_hours = 24 - (time_hours//12)
            if time_hours > 12:
                display_time = "%d"%(int(display_time.split(":")[0]),) + ":" + "%02d"%(time_minutes,) + " " + "AM"
            else:
                display_time = "%d"%(24 - add_to_hours,) + ":" + "%02d"%(time_minutes,) + " " + "AM"

        else:
            display_time = "%d"%(time_hours-12,) + ":" + "%02d"%(time_minutes,) + ' ' + 'AM'
    else:
        if 12 < time_hours < 24:
            display_time = "%d"%(time_hours-12,) + ":" + "%02d"%(time_minutes,) + " " + "PM"
        elif time_hours == 12:
            display_time = "%d"%(time_hours,) + ":" + "%02d"%(time_minutes,) + " " + "PM"
        elif time_hours < 12:
            display_time = "%d"%(time_hours,) + ":" + "%02d"%(time_minutes,) + " " + "AM"
        elif time_hours >= 24:
            time_hours = time_hours - add_hours
            display_time = "%d"%(time_hours,) + ":" + "%02d"%(time_minutes,) + " " + "AM"
        else:
            display_time = "%d"%(time_hours-12,) + ":" + "%02d"%(time_minutes,) + " " + "PM"

    if days < 1 and bool(weekday) == True:
        weekday = weekday.capitalize()
        display_time += ',' + ' ' + f'{weekday}'

    elif days == 1 and bool(weekday) == True:
        n_days = "(next day)"
        if bool(weekday) == True:
            weekday = weekday.capitalize()
            index = weekdays.index(weekday)+days
            days_later = weekdays[index]
            display_time+= ',' + ' ' + f'{days_later}' + ' ' + n_days
        else:
            display_time+= ' ' + n_days
    elif days > 1 and bool(weekday) == True:
        weekday = weekday.capitalize()
        n_days = f'({days} days later)'
        index = days%7 + weekdays.index(weekday) - len(weekdays)
        days_later = weekdays[index]
        display_time+="," + " " + f"{days_later}" + " " + n_days
        
    elif days == 1 or bool(weekday) == True:
        n_days = "(next day)"
        if bool(weekday) == True:
            weekday = weekday.capitalize()
            index = weekdays.index(weekday)+days
            days_later = weekdays[index]
            display_time+= ',' + ' ' + f'{days_later}' + ' ' + n_days
        else:
            display_time+= ' ' + n_days
        
    elif days > 1:
        n_days = f"({days} days later)"
        display_time += " " + n_days
    else:
        pass
    return display_time
