import argparse
from pyfiglet import Figlet

def start():
    f = Figlet(font='slant')
    print(f.renderText('Welcome to ahasui!'))
    main()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Enter the command")
    args = parser.parse_args()

start()