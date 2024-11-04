import logging
import sys

from s3 import get_s3


def main():
    if len(sys.argv) < 2:
        raise SyntaxError("filename argument is missing: python dumper.py 'filename'")

    filename = sys.argv[1]
    logging.info("LOAD -> S3: %s", filename)

    s3 = get_s3()

    result = s3.load(filename=filename, prefix="pg_dump/")
    logging.info("S3 response: %s", result)


if __name__ == "__main__":
    main()
