avg_rain = float(0)
years = 0
rainfall = 0
months_list = ['Jan',
               'Feb',
               'March',
               'April',
               'May',
               'June',
               'July',
               'Aug',
               'Sept',
               'Oct',
               'Nov',
               'Dec']
months = 12
y = 0

print('    Welcome!\n')
years = int(input('How many years :'))

while y < years:
    m = 0
    while m < months:
        print('    Year', y+1 , months_list[m])
        rainfall = int(input('Rainfall :'))
        avg_rain = avg_rain + rainfall
        m = m + 1
    y = y + 1

print('\n    Data Collection Complete!')
print('The total amount of rain for', years, 'or', years * 12, 'months is', avg_rain, 'inches.')

avg_rain = avg_rain / (years * 12)
print('The average rain each month was', avg_rain, 'inches.')