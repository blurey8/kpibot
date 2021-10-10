import logging
from bs4 import BeautifulSoup
import requests
from urllib.parse import parse_qs, urlparse

URL = "https://kpi.go.id/index.php/id/kpi-daerah"
TITLE = "Pojok Aduan"
PARAMETER_KEY = "detail3"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    logger.info("Access KPI page...")
    index_page = requests.get(URL)
    index_soup = BeautifulSoup(index_page.content, "html.parser")
    index_box = index_soup.find(text=TITLE).parent.parent.parent
    complains = index_box.find_all("a")

    for complain in complains:
        detail_url = complain["href"]
        logger.info("Get complain detail...")
        detail_page = requests.get(detail_url)
        detail_soup = BeautifulSoup(detail_page.content, "html.parser")
        detail_box = detail_soup.find(text=TITLE).parent.parent.parent

        title = complain.text
        data = detail_box.find_all("td")
        author = data[0].text
        text = data[1].text
        id = parse_qs(urlparse(detail_url).query)[PARAMETER_KEY][0]

        print(f"({id}) {author}: {title}")
        print(text)
        print(f"-- {detail_url}")
        print()


if __name__ == "__main__":
    main()
