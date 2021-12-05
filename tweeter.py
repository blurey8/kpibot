from requests.api import request
from tweepy.errors import Forbidden
from config import create_api, logger
import time

from object import Complain


class Tweeter:
    def __init__(self) -> None:
        self.api = create_api()

    def tweet(self, content: str):
        logger.info("Tweeting...")
        self.api.update_status(content)

    def tweets(self, contents: "list[str]"):
        logger.info(f"Tweeting {len(contents)} post...")
        print(len(contents[0]))
        try:
            prev_tweet = self.api.update_status(contents[0])
            for content in contents[1:]:
                print(len(content))
                prev_tweet = self.api.update_status(
                    content,
                    in_reply_to_status_id=prev_tweet.id,
                    auto_populate_reply_metadata=True,
                )
        except Forbidden as e:
            if e.api_errors[0]["code"] == 187:
                logger.info("No new complain.")
                return "No new complain."
            else:
                logger.error(f"Error: {e.api_errors}")
                return e
        except Exception as e:
            logger.error(f"Error: {e}")
            return e
        return None

    def tweet_complain(self, complain: Complain):
        return self.tweets(complain.to_tweets())


def main():
    tweeter = Tweeter()
    id = 1
    while True:
        tweeter.tweet(f"Test tweet from Tweepy Python {id}")
        id += 1
        logger.info("Waiting...")
        if id > 2:
            break
        time.sleep(60)


if __name__ == "__main__":
    main()
