import bilibili
import douyu
import huya
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("platform", help="Live platform e.g. douyu")
    parser.add_argument("room", help="room id")
    args = parser.parse_args()

    match args.platform:
        case "douyu":
            print(douyu.DouYu(args.room).get_real_url())
        case "bilibili":
            print(bilibili.get_real_url(args.room))
        case "huya":
            print(huya.get_real_url(args.room))
        case _:
            print(f"There's no platform called {args.platform}, please check your input.")
