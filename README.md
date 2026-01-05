# Cyprus News Web Crawler

A Python web crawler for collecting news articles from major Cypriot news websites.

## Features

- Crawls 6+ major Cyprus news sources
- - Supports both Greek and English news sites
  - - Duplicate detection using hashing
    - - JSON database for article storage
      - - Comprehensive logging
        - - Configurable crawl settings
          - - Rate limiting to respect servers
           
            - ## Supported Sources
           
            - - **SigmaLive** (Greek) - sigmalive.com
              - - **Philenews** (Greek) - philenews.com
                - - **Antenna** (Greek) - antenna.com.cy
                  - - **CYBC** (Greek) - cybc.com.cy
                    - - **Inside Cyprus** (English) - insidecyprus.net
                      - - **Cyprus Mail** (English) - cyprus-mail.com
                       
                        - ## Installation
                       
                        - 1. Clone the repository:
                          2. ```bash
                             git clone https://github.com/PetsasTeam/cyprus-news-crawler.git
                             cd cyprus-news-crawler
                             ```

                             2. Create a virtual environment:
                             3. ```bash
                                python -m venv venv
                                source venv/bin/activate  # On Windows: venv\Scripts\activate
                                ```

                                3. Install dependencies:
                                4. ```bash
                                   pip install -r requirements.txt
                                   ```

                                   ## Usage

                                   Run the crawler:
                                   ```bash
                                   python crawler.py
                                   ```

                                   ## Configuration

                                   Edit `config.py` to:
                                   - Add or modify news sources
                                   - - Change CSS selectors for new site layouts
                                     - - Adjust crawler timeout and delays
                                       - - Modify database path
                                        
                                         - ## Output
                                        
                                         - Articles are saved to `data/articles.json` with the following structure:
                                         - ```json
                                           {
                                             "title": "Article Title",
                                             "url": "https://...",
                                             "source": "source_name",
                                             "language": "en/el",
                                             "crawled_at": "2024-01-05T16:30:00",
                                             "date": "2024-01-05",
                                             "hash": "abc123..."
                                           }
                                           ```

                                           ## Scheduling

                                           To run crawler on a schedule, use cron (Linux/Mac):
                                           ```bash
                                           */30 * * * * cd /path/to/cyprus-news-crawler && python crawler.py
                                           ```

                                           Or Windows Task Scheduler for running every 30 minutes.

                                           ## Requirements

                                           - Python 3.7+
                                           - - requests
                                             - - beautifulsoup4
                                               - - feedparser
                                                 - - python-dotenv
                                                   - - lxml
                                                     - - APScheduler
                                                      
                                                       - ## Project Structure
                                                      
                                                       - ```
                                                         cyprus-news-crawler/
                                                         ├── crawler.py              # Main crawler implementation
                                                         ├── config.py              # Configuration for news sources
                                                         ├── requirements.txt       # Project dependencies
                                                         ├── README.md              # This file
                                                         ├── .gitignore            # Git ignore rules
                                                         ├── data/
                                                         │   └── articles.json     # Collected articles database
                                                         └── logs/
                                                             └── crawler.log       # Crawler logs
                                                         ```

                                                         ## License

                                                         MIT License

                                                         ## Author

                                                         PetsasTeam
