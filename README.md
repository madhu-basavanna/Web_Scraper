# Clone the repository 
```
git clone https://github.com/madhu-basavanna/Web_Scraper
```

# Run Selenium Docker
```
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:199.0
```

# Install requirements
```
pip install -r requirements.txt
```

# Run web_scraper.py with argument
```
python3 web_scraper.py 'mercedes-benz'
```