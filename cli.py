"""
Module that contains the command line app.
"""
import argparse
from googletrans import Translator

# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description='Command description.')

translator = Translator()


def main(args=None):

    print("Args:", args)

    results = translator.translate(args.text, src=args.src, dest=args.dest)

    print(results.text)


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(
        description='A simple translation app')

    parser.add_argument("-t", "--text", type=str, default="Hello",
                        help="Text to translate")
    parser.add_argument("-s", "--src", default="en",
                        help="Source Language")
    parser.add_argument("-d", "--dest", default="ja",
                        help="Destination Language")

    args = parser.parse_args()

    main(args)
