import ssl
import socket
import sys


def sslscan(siteelem):
    with socket.create_connection((siteelem, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=siteelem) as ssock:
            print(siteelem + " " + ssock.version())


print(len(sys.argv))
context = ssl.create_default_context()

if len(sys.argv) == 1:
    site = input("Enter the site you'd like to scan: ")
    sslscan(site)
else:
    filename = sys.argv[1]
    for line in open(filename):
        line = line.strip()
        sslscan(line)
