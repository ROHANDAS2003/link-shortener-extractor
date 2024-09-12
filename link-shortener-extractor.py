import pyshorteners
from urllib.request import urlopen

def link_shortener(link):
    try:
        shortener = pyshorteners.Shortener()
        short_link = shortener.tinyurl.short(link)
        print('\t[+] Real Link: ' + link)
        print('\t[+] Shortened Link: ' + short_link)
    except Exception as e:
        print("Error:", e)

def link_opener(link):
    try:
        shortened_url = urlopen(link)
        real_link = shortened_url.geturl()
        print('\t[+] Shortened Link: ' + link)
        print('\t[+] Real Link: ' + real_link)
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    try:
        num = input("Enter your choice ...\n" 
                    "1. Type 1 for shortening link\n"
                    "2. Type 2 for extracting real link from a shortened link\n")

        if num not in ('1', '2'):
            print("Invalid choice.")
            exit()

        link = input("Enter the link: ")

        if num == '1':
            link_shortener(link)
        else:
            link_opener(link)
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print("Error:", e)
