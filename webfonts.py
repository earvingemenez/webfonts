import argparse
from lib.r import Inspect


parser = argparse.ArgumentParser(description='Generates scss file based from your fonts list')
parser.add_argument('location', type=str, help='Font files location directory')
parser.add_argument('--destpath', type=str, help='Path to save the scss file')


if __name__ == "__main__":

    args = parser.parse_args()
    i = Inspect(fonts_path=args.location)

    for dirpath, fontfiles in i.read():
        i.write(dirpath, fontfiles)