from datetime import  datetime
date,month,year = input("Using This Format(date-month-year)\nEnter Your Birthdate:").split('-')
date = int(date)
month = int(month)
year = int(year)

# Data For Western Zodiac
z_west = {
        'Aries' : {
            'start': datetime(day=21,month=3,year=year),
            'end': datetime(day=20,month=4,year=year)
            },
        'Taurus' : {
            'start' : datetime(day=20,month=4,year=year),
            'end': datetime(day=20,month=5,year=year)

        },
        'Gemini' : {
            'start' : datetime(day=21,month=5,year=year),
            'end': datetime(day=21,month=6,year=year)

        },
        'Cancer' : {
            'start' : datetime(day=22,month=6,year=year),
            'end': datetime(day=22,month=7,year=year)

        },
        'Leo' : {
            'start' : datetime(day=23,month=7,year=year),
            'end': datetime(day=22,month=8,year=year)

        },
        'Virgo' : {
            'start' : datetime(day=23,month=8,year=year),
            'end': datetime(day=22,month=9,year=year)

        },
        'Libra' : {
            'start' : datetime(day=23,month=8,year=year),
            'end': datetime(day=23,month=9,year=year)

        },
        'Scorpio' : {
            'start' : datetime(day=24,month=10,year=year),
            'end': datetime(day=22,month=11,year=year)

        },
        'Sagittarius' : {
            'start' : datetime(day=23,month=11,year=year),
            'end': datetime(day=21,month=12,year=year)

        },
        'Capricorn' : {
            'start' : datetime(day=22,month=12,year=year),
            'end': datetime(day=19,month=1,year=year+1)

        },
        'Aquarius' : {
            'start' : datetime(day=20,month=1,year=year),
            'end': datetime(day=18,month=2,year=year)

        },
        'Pisces' : {
            'start' : datetime(day=19,month=2,year=year),
            'end': datetime(day=19,month=3,year=year)

        }
    }

# Data for chinese zodiac
z_china = {
        0 : 'Monkey',
        1 : 'Rooster',
        2 : 'Dog',
        3 : 'Pig',
        4 : 'Rat',
        5 : 'Ox',
        6 : 'Tiger',
        7 : 'Rabbit',
        8 : 'Dragon',
        9 : 'Snake',
        10: 'Horse',
        11: 'Sheep'
    }

# Function for chinese zodiac finder
def chinese_zodiac(year):
    return z_china[year%12]


# Function for Western zodiac finder
def western_zodiac(day,month,year):
    cdate = datetime(day=day,month=month,year=year)
    capricorndate = datetime(day=day,month=month,year=year+1)

    for main_key,main_val in z_west.items():
        if cdate>=main_val['start'] and cdate<= main_val['end']:
            return main_key

        elif capricorndate >= main_val['start'] and capricorndate <= main_val['end']:
            return main_key


print(f'Your Birthday : {date}.{month}.{year}')
print(f'Your Western Zodiac : {western_zodiac(date,month,year)}')
print(f'Your Chinese Zodiac : {chinese_zodiac(year)}')
















   #
   #
   # if year % 12 == 0:
   #      return_val = 'Monkey'
   #  elif year % 12 == 1:
   #      return_val = 'Rooster'
   #  elif year % 12 == 2:
   #      return_val = 'Dog'
   #  elif year % 12 == 3:
   #      return_val = 'Pig'
   #  elif year % 12 == 4:
   #      return_val = 'Rat'
   #  elif year % 12 == 5:
   #      return_val = 'Ox'
   #  elif year % 12 == 6:
   #      return_val = 'Tiger'
   #  elif year % 12 == 7:
   #      return_val = 'Rabbit'
   #  elif year % 12 == 8:
   #      return_val = 'Dragon'
   #  elif year % 12 == 9:
   #      return_val = 'Snake'
   #  elif year % 12 == 10:
   #      return_val = 'Horse'
   #  elif year % 12 == 11:
   #      return_val = 'Sheep'
   #
