__author__ = 'alex'

import argparse
import httplib


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Is the Site Up')
    parser.add_argument('-d', '--domain', dest='domain', help='Domain to inspect', required=False,
                        default='rewrite.local')
    args = parser.parse_args()

    conn = httplib.HTTPConnection(args.domain)
    conn.request("GET", "/")
    conn1 = conn.getresponse()
    connstat = conn1.status

    if connstat == 301:
        domain = conn1.getheader('location')
        print "Your Domain redirects to " + domain
        rd = raw_input("Would you like to use this Domain? (Y/n) ")
        if (rd == "Y") or (rd == "Yes"):
            domain = domain
        else:
            domain = args.domain

    print domain