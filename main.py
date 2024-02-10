import json, requests, threading, os, time, argparse
from datetime import datetime
from colorama import Fore

an = datetime.now()
tarih = an.strftime("%d/%m/%Y")
saat = an.strftime("%H:%M:%S")
banner = f"""{Fore.BLUE}
__        __          _     _ _   _            _    
\ \      / /__  _   _| | __| | | | | __ _  ___| | __
 \ \ /\ / / _ \| | | | |/ _` | |_| |/ _` |/ __| |/ /{Fore.RESET}
  \ V  V / (_) | |_| | | (_| |  _  | (_| | (__|   <
   \_/\_/ \___/ \__,_|_|\__,_|_| |_|\__,_|\___|_|\_\\

{Fore.BLUE}WebHook Spammer{Fore.RESET} - {Fore.RED}v1.0{Fore.RESET} Instagram | Telegram = {Fore.BLUE}@keremdemirsec {Fore.RESET}{saat} - {tarih}

"""

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def mesaj_gonder(url, icerik):
    while True:
        veri = {
            "content": f"@everyone {icerik}",
            "username": "Fue",
            "avatar_url": "https://media.tenor.com/H7uiT0t2pysAAAAM/mathilda-lando-leon-the-professional.gif"
        }

        try:
            yanit = requests.post(url, json=veri)
            if yanit.status_code == 204:
                print(f"{Fore.BLUE}[{Fore.GREEN} + {Fore.BLUE}]{Fore.GREEN} Mesaj gönderildi")
            else:
                print(f"{Fore.BLUE}[{Fore.RED} - {Fore.BLUE}]{Fore.RED} Mesaj gönderme başarısız")
        except Exception as e:
            print(f"{Fore.BLUE}[{Fore.RED} - {Fore.BLUE}]{Fore.RESET} Hata: {e}")

        time.sleep(1)
        
def webhook_spammer(url, icerik):
    try:
        yanit = requests.get(url)
        yanit.raise_for_status()
    except Exception as e:
        print(f"{Fore.BLUE}[{Fore.RED} - {Fore.BLUE}]{Fore.RESET} Geçersiz webhook URL'si! Hata: {e}")
        return

    threadler = []
    for i in range(10):
        thread = threading.Thread(target=mesaj_gonder, args=(url, icerik))
        threadler.append(thread)
        thread.start()
        
def webhook_sil(url):
    try:
        yanit = requests.head(url)
        yanit.raise_for_status()
    except Exception as e:
        print(f"{Fore.RED}Geçersiz webhook URL'si! Hata: {e}")
        return

    yanit = requests.delete(url)
    if yanit.status_code == 204:
        print(f"{Fore.BLUE}[{Fore.GREEN} + {Fore.BLUE}]{Fore.GREEN} Webhook başarıyla silindi.")
    else:
        print(f"{Fore.BLUE}[{Fore.RED} - {Fore.BLUE}]{Fore.RESET} Webhook silinirken hata oluştu: {yanit.status_code}")

def main(args):
    if args.islem == "spam":
        webhook_spammer(args.webhook, args.mesaj)
    elif args.islem == "sil":
        webhook_sil(args.webhook)
    else:
        print(f"{Fore.BLUE}[{Fore.RED} - {Fore.BLUE}]{Fore.RESET} Geçersiz işlem! Lütfen 'spam' veya 'sil' olarak belirtin.")

if __name__ == "__main__":
    cls()
    print(banner)
    parser = argparse.ArgumentParser(description='Discord webhook işlemleri')
    parser.add_argument('--webhook', required=True, help='Webhook adresi')
    parser.add_argument('--islem', required=True, choices=['spam', 'sil'], help='Yapılacak işlem (spam veya sil)')
    parser.add_argument('--mesaj', help='Spam işlemi için gönderilecek mesaj (opsiyonel)')
    args = parser.parse_args()
    main(args)