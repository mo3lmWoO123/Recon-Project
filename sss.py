import socket
import sys

sys.stdout.reconfigure(encoding="utf-8")


def ip_lookup():
    print("\n[ DNS Lookup ]")

    target = input("Domain: ").strip()

    try:
        ip = socket.gethostbyname(target)

        print(f"\nIP Address : {ip}")

        try:
            host = socket.gethostbyaddr(ip)
            print(f"Host       : {host[0]}")
        except socket.error:
            print("Host       : Not Found")

    except socket.gaierror:
        print("Could not resolve domain")


def subdomain_scanner():
    print("\n[ Subdomain Scan ]")

    domain = input("Domain: ").strip()

    subs = [
        "www",
        "mail",
        "ftp",
        "admin",
        "api",
        "dev",
        "ssh",
        "secure",
        "ns1",
        "cpanel"
    ]

    found = False

    print(f"\nChecking subdomains for {domain}...\n")

    for sub in subs:
        full = f"{sub}.{domain}"

        try:
            ip = socket.gethostbyname(full)
            print(f"{full} -> {ip}")
            found = True

        except socket.gaierror:
            pass

    if not found:
        print("No results")


def quick_port_scanner():
    print("\n[ Port Scan ]")

    target = input("Target: ").strip()

    ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]

    try:
        ip = socket.gethostbyname(target)

        print(f"\nScanning {ip}\n")

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)

            result = sock.connect_ex((ip, port))

            if result == 0:
                print(f"Port {port} OPEN")

            sock.close()

    except socket.gaierror:
        print("Invalid host")


def main_menu():
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
        """)

        print("1) DNS Lookup")
        print("2) Subdomain Scan")
        print("3) Port Scan")
        print("4) Exit\n")

        choice = input("X-RECON > ").strip()

        if choice == "1":
            ip_lookup()

        elif choice == "2":
            subdomain_scanner()

        elif choice == "3":
            quick_port_scanner()

        elif choice == "4":
            print("\nGoodbye.\n")
            break

        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main_menu()