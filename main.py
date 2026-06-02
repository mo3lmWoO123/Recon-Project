import socket
import requests
import whois
import dns.resolver

def dns_lookup():
    print("\n[ DNS Lookup ]")

    domain = input("Domain: ").strip()

    try:
        ip = socket.gethostbyname(domain)
        print(f"\nIP Address: {ip}")

        try:
            host = socket.gethostbyaddr(ip)
            print(f"Hostname: {host[0]}")
        except:
            print("Hostname: Not Found")

    except:
        print("Could not resolve domain")


def whois_lookup():
    print("\n[ WHOIS Lookup ]")

    domain = input("Domain: ").strip()

    try:
        data = whois.whois(domain)

        print(f"\nDomain: {domain}")
        print(f"Registrar: {data.registrar}")
        print(f"Created: {data.creation_date}")
        print(f"Expires: {data.expiration_date}")

    except:
        print("WHOIS lookup failed")


def dns_records():
    print("\n[ DNS Records ]")

    domain = input("Domain: ").strip()

    records = ["A", "MX", "NS", "TXT"]

    for record in records:
        try:
            print(f"\n{record} Records:")

            answers = dns.resolver.resolve(domain, record)

            for answer in answers:
                print(answer)

        except:
            print(f"No {record} records found")


def headers_lookup():
    print("\n[ HTTP Headers ]")

    url = input("URL (https://example.com): ").strip()

    try:
        r = requests.get(url, timeout=5)

        print()

        for key, value in r.headers.items():
            print(f"{key}: {value}")

    except:
        print("Request failed")


def robots_check():
    print("\n[ robots.txt ]")

    domain = input("Domain: ").strip()

    url = f"https://{domain}/robots.txt"

    try:
        r = requests.get(url, timeout=5)

        print("\n" + r.text)

    except:
        print("Could not fetch robots.txt")


def sitemap_check():
    print("\n[ sitemap.xml ]")

    domain = input("Domain: ").strip()

    url = f"https://{domain}/sitemap.xml"

    try:
        r = requests.get(url, timeout=5)

        print("\n" + r.text[:3000])

    except:
        print("Could not fetch sitemap.xml")


def subdomain_check():
    print("\n[ Subdomain Check ]")

    domain = input("Domain: ").strip()

    words = [
        "www",
        "mail",
        "ftp",
        "admin",
        "api",
        "dev",
        "blog",
        "test"
    ]

    found = False

    for word in words:
        sub = f"{word}.{domain}"

        try:
            ip = socket.gethostbyname(sub)

            print(f"{sub} -> {ip}")

            found = True

        except:
            pass

    if not found:
        print("No results")


while True:

    print(r"""
 __   __      ____  _____ ____ ___  _   _
 \ \ / /     |  _ \| ____/ ___/ _ \| \ | |
  \ V / _____| |_) |  _|| |  | | | |  \| |
   > < |_____|  _ <| |__| |__| |_| | |\  |
  /_/ \_\    |_| \_\_____\____\___/|_| \_|

======================================
          X-RECON by fdq12
======================================

1) DNS Lookup
2) WHOIS Lookup
3) DNS Records
4) HTTP Headers
5) robots.txt
6) sitemap.xml
7) Subdomain Check
8) Exit
""")

    choice = input("X-RECON > ").strip()

    if choice == "1":
        dns_lookup()

    elif choice == "2":
        whois_lookup()

    elif choice == "3":
        dns_records()

    elif choice == "4":
        headers_lookup()

    elif choice == "5":
        robots_check()

    elif choice == "6":
        sitemap_check()

    elif choice == "7":
        subdomain_check()

    elif choice == "8":
        print("\nGoodbye.\n")
        break

    else:
        print("Invalid option")

    input("\nPress Enter to continue...")
