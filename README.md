# Vehicle Scraping

Scraping to obtain vehicle details

sites scraped:

- https://www.autoevolution.com/moto/
- https://www.motorcycle.com/specs/

## How to run

Clone the repository and install requirement as follows.

```bash
git clone https://github.com/lukasab/vehicle_scraping.git && cd vehicle_scraping
pip install -r requirements.txt
```

Run the crawler with:

```bash
scrapy crawl vehicle
```

The results are stored in `vehicle_scraping/data`
