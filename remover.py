import logging
import sys

from s3 import get_s3


def main():
    if len(sys.argv) < 2:
        raise SyntaxError("url argument is missing: python dumper.py 'url'")

    url = sys.argv[1]

    s3 = get_s3()

    result = s3.remove(url=url)
    if result:
        logging.info("S3 response: %s", result)


if __name__ == "__main__":
    main()
