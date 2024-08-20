import ipaddress
from urllib.parse import urlparse


def is_ip_address(ip_address):
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        return False

    return True


def is_url_address(url_address):
    try:
        result = urlparse(url_address)
        return all([result.scheme, result.netloc])
    except AttributeError:
        return False
