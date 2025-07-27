# ScrapySteamCS2Items

A Scrapy-based web scraper for collecting Counter-Strike 2 (CS2) item data from the Steam Community Market. This project analyzes item prices and calculates potential profit margins for trading opportunities.

## Features

- **Steam Market Scraping**: Scrapes CS2 item data from steamcommunity.com
- **Price Analysis**: Compares buying and selling prices to calculate profit margins
- **Dockerized Setup**: Complete Docker Compose environment with PostgreSQL and monitoring tools
- **Web Interface**: ScrapydWeb for managing and monitoring scraping jobs
- **Database Storage**: PostgreSQL database with PgAdmin for data management

## Architecture

The project consists of several components:

- **Scrapy Spider**: Core scraping logic for Steam Community Market
- **PostgreSQL**: Database for storing scraped item data
- **ScrapydWeb**: Web interface for spider management and monitoring
- **PgAdmin**: Database administration interface

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd ScrapySteamCS2Items
```

2. Create environment file:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Start the services:
```bash
docker-compose up -d
```

4. Access the interfaces:
   - ScrapydWeb: http://localhost:5000
   - PgAdmin: http://localhost:5050
   - Scrapyd API: http://localhost:6800

## Environment Variables

Create a `.env` file with the following variables:

```env
DB_NAME=cs2_items
DB_USER=postgres
DB_PASSWORD=your_password
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin_password
PROXY=your_proxy_url_if_needed
```

## Usage

### Running the Spider

1. Via ScrapydWeb interface (recommended):
   - Open http://localhost:5000
   - Navigate to "Jobs" > "Schedule"
   - Select the "steamspider" spider
   - Click "Schedule"

2. Via Scrapyd API:
```bash
curl http://localhost:6800/schedule.json -d project=itemspider -d spider=steamspider
```

3. Via command line (inside container):
```bash
docker exec -it cs2_scrapy scrapy crawl steamspider
```

### Data Access

Access your scraped data through:
- PgAdmin interface at http://localhost:5050
- Direct PostgreSQL connection on port 5432
- Database files in `CS2Scraper/dbs/` directory

## Spider Configuration

The spider is configured to:
- Target CS2 items (appid: 730)
- Filter items by price range ($1-$100)
- Calculate profit margins with 10% Steam fee consideration
- Use rotating user agents for requests
- Support proxy configuration

## Project Structure

```
ScrapySteamCS2Items/
├── CS2Scraper/
│   ├── itemspider/
│   │   ├── spiders/
│   │   │   └── steamspider.py    # Main spider logic
│   │   ├── items.py              # Data models
│   │   ├── pipelines.py          # Data processing
│   │   └── settings.py           # Spider configuration
│   ├── logs/                     # Spider logs
│   ├── dbs/                      # Local database files
│   └── requirements.txt          # Python dependencies
├── docker-compose.yml            # Service orchestration
└── README.md                     # This file
```

## Development

### Adding New Features

1. Modify spider logic in `CS2Scraper/itemspider/spiders/steamspider.py`
2. Update data models in `CS2Scraper/itemspider/items.py`
3. Customize data processing in `CS2Scraper/itemspider/pipelines.py`

### Local Development

For local development without Docker:

1. Install dependencies:
```bash
cd CS2Scraper
pip install -r requirements.txt
```

2. Configure settings in `itemspider/settings.py`

3. Run spider:
```bash
scrapy crawl steamspider
```

## Monitoring

- **ScrapydWeb**: Monitor spider execution, view logs, and manage jobs
- **Logs**: Available in `CS2Scraper/logs/` directory
- **Database**: Monitor data collection through PgAdmin

## Legal Notice

This tool is for educational and research purposes. Ensure compliance with Steam's Terms of Service and robots.txt when using this scraper. Use appropriate delays and respect rate limits.

## License

[Add your license information here]