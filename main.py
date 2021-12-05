from scraper import get_latest_complain
from tweeter import Tweeter


def main():
    tweeter = Tweeter()
    complain = get_latest_complain()
    tweeter.tweet_complain(complain)


if __name__ == "__main__":
    main()
