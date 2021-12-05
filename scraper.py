from bs4 import BeautifulSoup
import requests
from urllib.parse import parse_qs, urlparse
from config import logger
from object import Complain


URL = "https://kpi.go.id/index.php/id/form-pengaduan"
TITLE = "Pojok Aduan"
PARAMETER_KEY = "detail3"


def get_index_complains_anchors():
    logger.info("Access KPI page...")
    index_page = requests.get(URL, verify=False)
    index_soup = BeautifulSoup(index_page.content, "html.parser")
    index_box = index_soup.find(text=TITLE).parent.parent.parent
    complains = index_box.find_all("a")

    return complains


def get_complain_details(complain_anchor):
    detail_url = complain_anchor["href"]
    logger.info("Get complain detail...")
    detail_page = requests.get(detail_url, verify=False)
    detail_soup = BeautifulSoup(detail_page.content, "html.parser")
    detail_box = detail_soup.find(text=TITLE).parent.parent.parent

    complain = Complain()
    complain.source_url = detail_url
    complain.title = complain_anchor.text
    data = detail_box.find_all("td")
    complain.author = data[0].text
    complain.body = data[1].text
    complain.id = parse_qs(urlparse(detail_url).query)[PARAMETER_KEY][0]

    return complain


def get_latest_complain():
    complain_anchors = get_index_complains_anchors()
    return get_complain_details(complain_anchors[0])


def main():
    complains_anchors = get_index_complains_anchors()
    print(complains_anchors)
    for complains_anchor in complains_anchors:
        complain = get_complain_details(complains_anchor)
        print("------------------")
        # print(complain.to_str())
        print(complain.to_tweets())
        print("------------------")


if __name__ == "__main__":
    main()
