__author__ = 'alex'

import argparse
import httplib


def adddomain(domain):
    print domain


def realdomain(falsedomain):
    print falsedomain
    print "Your Domain redirects to " + falsedomain
    rd = raw_input("Would you like to use this Domain? (Y/n) ")
    if (rd == "Y") or (rd == "Yes"):
        return falsedomain
    else:
        return 0
    #input = raw_input()
    #while len(input) == "no":
    #    print "Must enter 10 characters, each being a-f."
    #    input = raw_input()


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
