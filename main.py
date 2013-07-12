__author__ = 'alex'

import argparse, httplib

def adddomain(domain):
    print domain

def connect(domain):
    c = httplib.HTTPConnection(domain)
    c.request("GET", "/index.php")
    c1 = c.getresponse()
    print c1.getheaders()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Is the Site Up')
    parser.add_argument('-d','--domain', dest='domain', help='Add Domain to inspect', required=True)
    args = parser.parse_args()

connect(args.domain)