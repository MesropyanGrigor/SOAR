import httpx
import base64

from vendor.virus_total.models import Result
from vendor.base import BaseClient

class VTClient(BaseClient):
    """Virus Total Client"""
    _name = "VirusTotal"
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(VTClient, cls).__new__(cls)

        return cls._instance

    def __init__(self, url, api_key):
        self._client = httpx.AsyncClient(
            base_url=url,
            headers={
                "accept": "application/json",
                "content-type": "application/x-www-form-urlencoded",
                "x-apikey": api_key,
            },
        )

    async def scan_ip(self, ip_address):
        response = await self._client.post(
            f"/ip_addresses/{ip_address}/analyse",
        )

        if response.status_code == httpx.codes.OK:
            response = await self._client.get(
                f"/ip_addresses/{ip_address}",
            )
        payload = response.json()
        if response.status_code == httpx.codes.OK:
            return Result(
                identifier=ip_address,
                type='IP',
                last_analysis_time=payload['data']['attributes']['last_analysis_date'],
                is_malicious=payload['data']['attributes']['last_analysis_stats']['malicious'],
            )

        return None

    async def scan_url(self, url):

        payload = {
            'url': url
        }

        response = await self._client.post(
            "/urls",
            data=payload,
        )

        if response.status_code == httpx.codes.OK:
            resource_id = base64.b64encode(url.encode())
            response = await self._client.get(
                f"/urls/{resource_id.decode()}",
            )

        payload = response.json()
        if response.status_code == httpx.codes.OK:
            return Result(
                identifier=url,
                type='URL',
                last_analysis_time=payload['data']['attributes']['last_analysis_date'],
                is_malicious=payload['data']['attributes']['last_analysis_stats']['malicious'],
            )

        return None

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        return hash(self) == hash(other)
