# Cyprus News Websites Configuration

NEWS_SOURCES = {
      "sigmalive": {
                "url": "https://www.sigmalive.com",
                "selector": "article",
                "title_selector": "h2, h3",
                "link_selector": "a",
                "date_selector": "time",
                "language": "el"
      },
      "philenews": {
                "url": "https://www.philenews.com",
                "selector": "article",
                "title_selector": "h2",
                "link_selector": "a",
                "date_selector": ".date",
                "language": "el"
      },
      "antenna": {
                "url": "https://www.antenna.com.cy",
                "selector": "article",
                "title_selector": "h2, h3",
                "link_selector": "a",
                "date_selector": "time",
                "language": "el"
      },
      "cybc": {
                "url": "https://www.cybc.com.cy",
                "selector": "article",
                "title_selector": "h2, h3",
                "link_selector": "a",
                "date_selector": "time",
                "language": "el"
      },
      "insidecyprus": {
                "url": "https://insidecyprus.net",
                "selector": "article",
                "title_selector": "h2, h3",
                "link_selector": "a",
                "date_selector": "time",
                "language": "en"
      },
      "cyprus_mail": {
                "url": "https://www.cyprus-mail.com",
                "selector": "article",
                "title_selector": "h2, h3",
                "link_selector": "a",
                "date_selector": "time",
                "language": "en"
      }
}

CRAWLER_CONFIG = {
      "timeout": 10,
      "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
      },
      "retry_attempts": 3,
      "delay_between_requests": 2
}

DATABASE_PATH = "data/articles.json"
LOG_FILE = "logs/crawler.log"
