__author__ = 'alex'

import argparse
import httplib


def adddomain(domain):
    print domain


def aim(domain):
    """

    :param domain:
    """
    a = httplib.HTTPConnection(domain)
    a.request("GET", "/index.php")
    a1 = a.getresponse()
    astat = a1.status
    if (astat == 302) or (astat == 301):
        a2 = a1.getheader('location')
        return a2, astat
    return (domain, astat)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Is the Site Up')
    parser.add_argument('-d', '--domain', dest='domain', help='Add Domain to inspect', required=False,
                        default='www.s24d.de')
    args = parser.parse_args()

c1, c2 = aim(args.domain)
print c1, c2