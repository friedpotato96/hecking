import requests
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def check_username(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Facebook": f"https://www.facebook.com/{username}"
    }

    print(f"\n🔍 Scanning for username: {Fore.CYAN}{username}\n")
    for site, url in sites.items():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[+] Found on {site}: {url}")
            else:
                print(f"{Fore.YELLOW}[-] Not Found on {site}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error checking {site}: {e}")

if __name__ == "__main__":
    username = input("Enter a username to scan: ")
    check_username(username)


