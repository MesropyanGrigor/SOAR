import asyncio
import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

class ScanProcessor:
    def __init__(self, output_file_name):
        self._scanners = set()
        self.results = []
        self._output_file_name = output_file_name

    def __del__(self):
        with open(self._output_file_name, 'w') as _file:
            json.dump({"data": self.results}, _file, cls=DateTimeEncoder)


    def add_scanner(self, scanner):
        self._scanners.add(
            scanner,
        )

    async def scan_ip(self, ip_address):
        coroutines = (
            _scanner.scan_ip(ip_address)
            for _scanner in self._scanners
        )

        gather_result = await asyncio.gather(
            *coroutines,
            return_exceptions=True,
        )
        results = []
        for result in gather_result:
            results.append(result)
            if result:
                self.results.append(
                    dict(result)
                )
        return results



    async def scan_address(self, url):
        coroutines = (
            _scanner.scan_url(url)
            for _scanner in self._scanners
        )

        gather_result = await asyncio.gather(
            *coroutines,
            return_exceptions=True,
        )
        results = []
        for result in gather_result:
            results.append(result)
            if result:
                self.results.append(
                    dict(result)
                )

        return results
