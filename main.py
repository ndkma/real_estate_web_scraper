from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import csv

# Specify how many pages to scrape
pages_to_scrape = int(input("How many pages do you want to scrape? "))

driver = webdriver.Chrome()
driver.get('https://www.28hse.com/en/rent/residential')

def scrape_page():
    # 'Items' refers to the 'info blocks' that contain listing information
    items = driver.find_elements(By.CSS_SELECTOR, '.item.property_item')

    # Create the csv file in append mode and instantiate the writer
    with open('scraped_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # For each 'block' from all the 'blocks' on the page
        for item in items:

            # Create a row list to collect all the data to be written to the csv later on
            row = []
            descriptions = item.find_elements(By.CLASS_NAME, 'detail_page')

            # Listing description
            try:
                listing_description = descriptions[1].text
                row.append(listing_description)
            except IndexError:
                row.append("")
            except NoSuchElementException:
                row.append("")

            # Hyperlink
            try:
                link = descriptions[1].get_attribute('href')
                row.append(link)
            except IndexError:
                row.append("")
            except NoSuchElementException:
                row.append("")

            district_info = item.find_elements(By.CLASS_NAME, 'district_area')
            for district in district_info:

                # HK district and address line 1
                location_info = district.find_elements(By.TAG_NAME, 'a')
                try:
                    hk_district = location_info[0].text
                    row.append(hk_district)
                except IndexError:
                    row.append("")
                except NoSuchElementException:
                    row.append("")

                try:
                    address_line_1 = location_info[1].text
                    row.append(address_line_1)
                except IndexError:
                    row.append("")
                except NoSuchElementException:
                    row.append("")

                # Address line 2
                try:
                    location_info_2 = district.find_element(By.CLASS_NAME, 'unit_desc')
                    address_line_2 = location_info_2.text
                    row.append(address_line_2)
                except IndexError:
                    row.append("")
                except NoSuchElementException:
                    row.append("")

            # Find the saleable area and gross area
            size_info = item.find_elements(By.CLASS_NAME, 'areaUnitPrice')
            try:
                size = size_info[0].text
                row.append(size)
            except IndexError:
                row.append("")
            except NoSuchElementException:
                row.append("")

            # Find the lease price
            try:
                lease_price = item.find_element(By.CLASS_NAME, 'green')
                row.append(lease_price.text)
            except IndexError:
                row.append("")
            except NoSuchElementException:
                lease_price = item.find_element(By.CSS_SELECTOR, '.ui.right.floated.large.label')
                row.append(lease_price.text)

            # Find the agency name
            agency = item.find_element(By.CLASS_NAME, 'companyName')
            try:
                agency_name = agency.text
                row.append(agency_name)
            except IndexError:
                row.append("")
            except StaleElementReferenceException:
                row.append("")
            except NoSuchElementException:
                row.append("")

            # Find description tags
            labels = item.find_elements(By.CLASS_NAME, 'label')
            tags = []
            for i in range(1, 12):
                try:
                    tags.append(labels[i + 3].text.strip())
                except IndexError:
                    break
                except NoSuchElementException:
                    break
            row.append(tags)

            # Write the collected data stored in 'row' to the csv file
            writer.writerow(row)

page_counter = 0

# Scrape the initial page
scrape_page()
page_counter += 1
print(f"Pages scraped: {page_counter}")

# Scrape subsequent pages
while pages_to_scrape > 1:
    # Click the 'next page' button
    next_button = driver.find_element(By.CSS_SELECTOR, '.angle.icon.right')
    next_button.click()
    time.sleep(1.5)

    scrape_page()

    # Update counters
    pages_to_scrape -= 1
    page_counter += 1
    print(f"Pages scraped: {page_counter}")

