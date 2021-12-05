import logging
from scraper import get_latest_complain
from tweeter import Tweeter
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Tweet Aduan KPI starts...")
    tweeter = Tweeter()
    complain = get_latest_complain()
    err = tweeter.tweet_complain(complain)
    logging.info(complain.to_str())
    res = {"content": complain.to_str()}
    if err != None:
        res["error"] = err
    return func.HttpResponse(json.dumps(res), status_code=200)
