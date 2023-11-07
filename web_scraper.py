import os
import time
import argparse
from pathlib import Path
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By


def main(args):
    
    home_url = 'https://www.faz.net/'
    target_text = str(args.target_text).lower()

    print("Test Execution Started")
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=options
    )

    #maximize the window size
    driver.maximize_window()
    time.sleep(10)

    #navigate to url
    driver.get(home_url)

    # Check if the target text exists in the page source
    if target_text in driver.page_source.lower():
        print(f"The text {target_text} exists on the page.")

        try:
            iframe = driver.find_element(By.XPATH, '//iframe[@title="SP Consent Message"]')
            # Switch to the iframe context
            driver.switch_to.frame(iframe)

            # Find the accept cookies button and click it
            pop_up_element = driver.find_element(By.XPATH, "//button[@title='EINVERSTANDEN']")
            pop_up_element.click()
            print("Accepted cookies acceptence popup")

            # Switch back to the default frame
            driver.switch_to.default_content()

        except:
            print("No cookies acceptence popup")

        finally:
            # Find all the clickable elements that contain the target text                 
            target_elements = driver.find_elements(By.XPATH, f"//div[contains(concat(' ', @class, ' '), ' Home  ')]/descendant::* \
                                     [contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), \
                                      '{target_text}')][not(self::script)]")
            
            for element in target_elements:
                try:
                    # Look for target text and click to open it
                    driver.execute_script("arguments[0].click();", element)

                    # Get the author and category elements
                    author_element = driver.find_element(By.XPATH, "//a[@class='atc-MetaAuthorLink']")
                    category_element = driver.find_element(By.XPATH, "//a[contains(concat(' ', @class, ' '), \
                                                           'gh-Ressort_Link gh-Hoverable gh-Hoverable-is-active gh-Ressort_Link-is-active')]")

                    # Create a directory to save the news articles
                    news_articles_directory = Path(__file__).parent / "news_articles"
                    if not os.path.exists(news_articles_directory):
                        # If it doesn't exist, create the directory
                        os.makedirs(news_articles_directory)

                    # Save the page source to a html file
                    date = datetime.date(datetime.now())
                    article_file_path = Path(__file__).parent / "news_articles" / f"{date}.html"
                    with open(article_file_path, 'w', encoding='utf-8') as f:
                        f.write(driver.page_source)

                    # Save the meta data of the article to a txt file
                    article_meta_data  = Path(__file__).parent / "news_articles" / f"{date}_meta_data.txt"
                    with open(article_meta_data, 'w', encoding='utf-8') as f:
                        f.write('url:' + driver.current_url + '\n')
                        f.write('author_name:' + author_element.text + '\n')
                        f.write('author_link:' + author_element.get_attribute("href") + '\n')
                        f.write('category:' + category_element.get_attribute("track-label") + '\n')

                    print(f"Saved the news article and meta data to {news_articles_directory}")
                    break
                    
                except:
                    print("Is a non clickable element")

    # Close the WebDriver
    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Article Scraper")
    
    # Define your command-line arguments
    parser.add_argument("target_text", nargs='?', default='donald trump', type=str, help="Target text to search for")
    
    args = parser.parse_args()
    print("Search text:", args.target_text)
    
    main(args=args)