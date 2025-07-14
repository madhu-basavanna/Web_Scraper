# Web_Scraper

A simple web scraping project built with Python that extracts news articles from web pages.

## Features

- Extracts news articles from web pages using Selenium
- Searches for specific keywords in articles
- Saves article content and metadata to files
- Easy to use and customize
- Outputs data in a structured format (HTML and text files)

## Technologies Used

- Python
- Selenium WebDriver
- Docker (for Selenium Chrome)

## Getting Started

### Prerequisites

- Python 3.x installed
- Docker (for running Selenium Chrome container)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/madhu-basavanna/Web_Scraper.git
   cd Web_Scraper
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Selenium Docker container:
   ```bash
   docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:199.0
   ```

### Usage

1. Make sure the Selenium Docker container is running (see installation step 3).
2. Run the web scraper with a search term:
   ```bash
   python web_scraper.py 'your-search-term'
   ```

   Example:
   ```bash
   python web_scraper.py 'mercedes-benz'
   ```

3. The scraper will:
   - Search for articles containing your search term on faz.net
   - Save the article content as an HTML file in the `news_articles/` directory
   - Save article metadata (URL, author, category) as a text file

## Folder Structure

```
Web_Scraper/
├── web_scraper.py      # Main scraping script
├── requirements.txt    # Python dependencies
├── news_articles/      # Directory for saved articles
│   ├── *.html         # Scraped article content
│   └── *_meta_data.txt # Article metadata
└── README.md          # Project documentation
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)