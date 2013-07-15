__author__ = 'alex'

import argparse
import httplib


def adddomain(domain):
    print domain


def realdomain(falsedomain):
    print falsedomain
    print "Input initial data.  Must be 10 characters, each being a-f."
    input = raw_input()
    while len(input) != 10 or not set(input).issubset('abcdef'):
        print "Must enter 10 characters, each being a-f."
        input = raw_input()
    return falsedomain


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Is the Site Up')
    parser.add_argument('-d', '--domain', dest='domain', help='Domain to inspect', required=False,
                        default='www.s24d.de')
    args = parser.parse_args()

    conn = httplib.HTTPConnection(args.domain)
    conn.request("GET", "/")
    conn1 = conn.getresponse()
    connstat = conn1.status

    if connstat == 301:
        realdomain(conn1.getheader('location'))