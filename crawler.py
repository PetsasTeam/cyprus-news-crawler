import requests
from bs4 import BeautifulSoup
import json
import logging
import time
from datetime import datetime
from pathlib import Path
import hashlib
from config import NEWS_SOURCES, CRAWLER_CONFIG, DATABASE_PATH, LOG_FILE

# Setup logging
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      handlers=[
                logging.FileHandler(LOG_FILE),
                logging.StreamHandler()
      ]
)
logger = logging.getLogger(__name__)

class CyprusNewsCrawler:
      def __init__(self):
                self.articles = self.load_articles()
                self.session = requests.Session()
                self.session.headers.update(CRAWLER_CONFIG["headers"])

      def load_articles(self):
                """Load existing articles from JSON file"""
                Path("data").mkdir(exist_ok=True)
                if Path(DATABASE_PATH).exists():
                              with open(DATABASE_PATH, 'r', encoding='utf-8') as f:
                                                return json.load(f)
        return []

            def save_articles(self):
                      """Save articles to JSON file"""
                      with open(DATABASE_PATH, 'w', encoding='utf-8') as f:
                                    json.dump(self.articles, f, ensure_ascii=False, indent=2)

                  def get_article_hash(self, title, url):
                            """Generate unique hash for article"""
                            content = f"{title}{url}".encode('utf-8')
                            return hashlib.md5(content).hexdigest()

          def article_exists(self, title, url):
                    """Check if article already exists"""
                    article_hash = self.get_article_hash(title, url)
                    return any(article.get('hash') == article_hash for article in self.articles)

          def crawl_source(self, source_name, source_config):
              """Crawl a single news source"""
              try:
                            logger.info(f"Crawling {source_name}...")
                            response = self.session.get(
                                source_config['url'],
                                timeout=CRAWLER_CONFIG['timeout']
                            )
                            response.encoding = 'utf-8'
                            response.raise_for_status()

                  soup = BeautifulSoup(response.content, 'html.parser')
            articles_found = 0

            # Find all articles
            article_elements = soup.select(source_config.get('selector', 'article'))

            for article in article_elements:
                              try:
                                                    title_elem = article.select_one(source_config.get('title_selector', 'h2'))
                                                    link_elem = article.select_one(source_config.get('link_selector', 'a'))
                                                    date_elem = article.select_one(source_config.get('date_selector', 'time'))

                                  if not title_elem or not link_elem:
                                                            continue

                    title = title_elem.get_text(strip=True)
                    link = link_elem.get('href', '')

                    # Convert relative URLs to absolute
                    if link.startswith('/'):
                                              link = source_config['url'] + link
elif not link.startswith('http'):
                        link = source_config['url'] + '/' + link

                    if not title or not link:
                                              continue

                    # Check for duplicates
                    if self.article_exists(title, link):
                                              continue

                    article_data = {
                                              'title': title,
                                              'url': link,
                                              'source': source_name,
                                              'language': source_config.get('language', 'unknown'),
                                              'crawled_at': datetime.now().isoformat(),
                                              'hash': self.get_article_hash(title, link)
                    }

                    if date_elem:
                                              article_data['date'] = date_elem.get_text(strip=True)

                    self.articles.insert(0, article_data)
                    articles_found += 1
                    logger.info(f"Found: {title[:60]}...")

except Exception as e:
                    logger.warning(f"Error parsing article from {source_name}: {str(e)}")
                    continue

            logger.info(f"✓ {source_name}: Found {articles_found} new articles")
            return articles_found

except requests.exceptions.RequestException as e:
            logger.error(f"✗ Error crawling {source_name}: {str(e)}")
            return 0

    def run(self):
              """Run crawler for all sources"""
        logger.info("=" * 50)
        logger.info("Starting Cyprus News Crawler")
        logger.info("=" * 50)

        total_articles = 0
        for source_name, source_config in NEWS_SOURCES.items():
                      articles_count = self.crawl_source(source_name, source_config)
            total_articles += articles_count
            time.sleep(CRAWLER_CONFIG['delay_between_requests'])

        # Keep only recent 500 articles
        self.articles = self.articles[:500]
        self.save_articles()

        logger.info("=" * 50)
        logger.info(f"Crawl completed. Total new articles: {total_articles}")
        logger.info(f"Total articles in database: {len(self.articles)}")
        logger.info("=" * 50)

if __name__ == "__main__":
      crawler = CyprusNewsCrawler()
    crawler.run()
