MAX_CHARACTER = 279
URL_CHARACTER = 20


class Complain:
    def __init__(self) -> None:
        self.id = ""
        self.title = ""
        self.author = ""
        self.body = ""
        self.source_url = ""

    def to_str(self) -> str:
        str = f"🚩 ADUAN: {self.title}\n\n"
        str += f"{self.body}\n\n"
        str += f"oleh: {self.author}\n"
        str += f"{self.source_url}\n"
        # str += f"aduan#{self.id}\n"
        return str

    def to_tweets(self) -> str:
        self.tweets = []

        self.add_title_and_body_to_tweets()
        self.add_author_to_tweets()
        self.add_url_to_tweets()

        return self.tweets

    def add_title_and_body_to_tweets(self):
        str = f"🚩 ADUAN: {self.title}\n\n"
        str += f"{self.body}"
        while str != "":
            self.tweets.append(str[:MAX_CHARACTER].strip())
            str = str[MAX_CHARACTER:].strip()

    def add_author_to_tweets(self):
        author_str = f"oleh: {self.author}"
        if len(self.tweets[-1]) + len(author_str) + 2 <= MAX_CHARACTER:
            self.tweets[-1] += f"\n\n{author_str}"
        else:
            self.tweets.append(f"{author_str}")

    def add_url_to_tweets(self):
        if len(self.tweets[-1]) + URL_CHARACTER + 1 <= MAX_CHARACTER:
            self.tweets[-1] += f"\n{self.source_url}"
        else:
            self.tweets.append(f"{self.source_url}")
