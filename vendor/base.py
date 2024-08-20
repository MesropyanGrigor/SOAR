import abc

class BaseClient:
    @abc.abstractmethod
    async def scan_ip(self, ip_address):
        """Scanning the ip address"""

    @abc.abstractmethod
    async def scan_url(self, url):
        """Scanning the url"""