import sys
import ssl
import socket
from datetime import datetime

# Add extra trusted CA stores here 
extra_ca = []

class Certificate(object):

    def __init__(self):
        self.valid = False
        self.error = ''

    def load(self, data):
        ''' Dinamically populates object with all certificate info and
        marks it as valid. '''
        for k, v in data.iteritems():
            setattr(self, k, v)
        self.datetime = datetime.strptime(self.notAfter, '%b %d %H:%M:%S %Y %Z')
        self.valid = True


def get_cert(host):
    ''' Returns a Certificate object formed with all values from the
    certificate '''
    certificate = Certificate()
    context = ssl.create_default_context()
    for ca in extra_ca:
        context.load_verify_locations(ca)
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    try:
        conn.connect((host, 443))
        certificate.load(conn.getpeercert())
    except ssl.CertificateError as e:
        certificate.error = "{0}: UNTRUSTED {1}".format(host, e)
    except socket.gaierror as e:
        certificate.error = "{0}: ERROR {1}".format(host, e)
    except socket.error as e:
        certificate.error = "{0}: ERROR {1}".format(host, e)
    return certificate

if __name__ == "__main__":
    ''' Example of how to use reading site from args '''
    site = sys.argv[1]
    certificate = get_cert(site)
    if certificate.valid:
        print("{0}: Valid Until {1}".format(site, certificate.notAfter))
    else:
        print(certificate.error)
