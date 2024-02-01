#!/usr/bin/env python
import argparse
import sys
from os.path import abspath, dirname, join

sys.path.append(abspath(join(dirname(__file__), "src")))

from get_board import main as get_board_info
from get_pin import main as get_pin_info
from get_user_boards import main as get_user_boards_info
from get_user_pins import main as get_user_pins_info

def main(argv=[]):
    parser = argparse.ArgumentParser(description="Pinterest Information Retrieval Tool")
    parser.add_argument("action", choices=["board", "pin", "user_boards", "user_pins"], help="Specify the action to perform")
    parser.add_argument("-id", "--identifier", required=True, help="Identifier of the board or pin")
    parser.add_argument("-a", "--access-token", help="Access token for Pinterest API")
    parser.add_argument("--log-level", default="ERROR", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Set the logging level")
    args = parser.parse_args(argv)

    if args.action == "board":
        get_board_info(["-b", args.identifier, "--pins", "-a", args.access_token, "--log-level", args.log_level])
    elif args.action == "pin":
        get_pin_info(["-p", args.identifier, "-a", args.access_token, "--log-level", args.log_level])
    elif args.action == "user_boards":
        get_user_boards_info(["--page-size", "25", "--include-empty", "--no-include-archived", "-a", args.access_token, "--log-level", args.log_level])
    elif args.action == "user_pins":
        get_user_pins_info(["--page-size", "25", "-a", args.access_token, "--log-level", args.log_level])

if __name__ == "__main__":
    main(sys.argv[1:])
