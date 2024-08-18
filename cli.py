"""
Module that contains the command line app.
"""
import argparse
from googletrans import Translator
from art import text2art

# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")

translator = Translator()


def main(args=None):
    print("\n")
    art = text2art("AC215")
    print(art)
    print("\n")
    print("Arguments:", args)
    text = args.text

    if args.file != "":
        # read file
        with open(args.file) as f:
            text = f.read()

    print("\n\n")
    print("Input:", text)

    results = translator.translate(text, src=args.src, dest=args.dest)

    print("Output:", results.text)


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="A simple translation app")

    parser.add_argument(
        "-t", "--text", type=str, default="I love cheese", help="Text to translate"
    )
    parser.add_argument("-f", "--file", type=str, default="", help="File to translate")
    parser.add_argument("-s", "--src", default="en", help="Source Language")
    parser.add_argument("-d", "--dest", default="it", help="Destination Language")

    args = parser.parse_args()

    main(args)
