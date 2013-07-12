__author__ = 'alex'

import argparse
import httplib
#import httplib2


def adddomain(domain):
    print domain


def connect(domain):
    """

    :param domain:
    """
    c = httplib.HTTPConnection(domain)
    c.request("GET", "/index.php")
    c1 = c.getresponse()
    print c1.getheaders()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Is the Site Up')
    parser.add_argument('-d', '--domain', dest='domain', help='Add Domain to inspect', required=False,
                        default='shop24direct.de')
    args = parser.parse_args()

connect(args.domain)