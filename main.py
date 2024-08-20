import argparse
import sys
import os
import asyncio
import structlog


from vendor.virus_total.client import VTClient
from stdlib.utils import is_ip_address, is_url_address
from stdlib.scan_processor import ScanProcessor


from config import Settings

settings = Settings()

logger = structlog.get_logger("SOAR")


def check_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileExistsError(f"file not found {file_path}")




def parse_args(argv):
    parser = argparse.ArgumentParser(prog="SOAR")

    parser.add_argument(
        '--input_file',
        help="IOC input file",
        required=True,
    )

    parser.add_argument(
        '--output_file',
        help="Generated output JSON file name",
        default='results.json',
    )

    args = parser.parse_args(argv)
    check_file_exists(args.input_file)

    return args


async def main():
    args = parse_args(sys.argv[1:])
    scanner = ScanProcessor(args.output_file)

    scanner.add_scanner(
        VTClient(
            settings.api_url,
            settings.api_key,
        ),
    )

    with open(args.input_file, "r") as _file:
        for line in _file:
            line = line.strip()
            results = []
            if not line:
                continue

            if is_ip_address(line):
                results = await scanner.scan_ip(line)
            elif is_url_address(line):
                results = await scanner.scan_address(line)
            else:
                logger.error(
                    f"Found invalid data {line}"
                )
                continue

            if results:
                for result in results:
                    logger.info(result)
            else:
                logger.warning(
                    "There is not result scan",
                    resource=line,
                )


if __name__ == "__main__":

    asyncio.run(
        main()
    )
