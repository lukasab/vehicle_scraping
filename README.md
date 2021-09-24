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

To scrape the autoevolution site run the crawler with:

```bash
scrapy crawl autoevolution
```

To scrape the motorcycle site run the crawler with:

```bash
scrapy crawl motorcycle
```

The results are stored in `vehicle_scraping/data`

## Estimated time to scrape data

We have added a download delay of 0.5 seconds for every request although, this makes the scrapping slower, it makes it possible. Not setting a download delay will cause your IP to be banned, or you might take the site down.

This is the amount of time it took to scrape each site:

- Autoevolution: 9248.006482s ~= 2.5 hours
- Motrcycle: TBD 18284s 5.1 = TBD hours
