__author__ = 'alex'

import argparse
import httplib


def adddomain(domain):
    print domain


def aim(domain):
    """

    :param domain:
    """
    c = httplib.HTTPConnection(domain)
    c.request("GET", "/index.php")
    c1 = c.getresponse()
    if (c1.status == 302) or (c1.status == 301):
        c2 = c1.getheader('location')
        return c2,
    return domain


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Is the Site Up')
    parser.add_argument('-d', '--domain', dest='domain', help='Add Domain to inspect', required=False,
                        default='www.s24d.de')
    args = parser.parse_args()

c1 = aim(args.domain)
print c1