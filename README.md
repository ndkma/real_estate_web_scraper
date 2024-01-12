# real_estate_web_scraper
A web scraper that uses Python and Selenium to scrape real estate data off of a specific website

HOW TO USE

This scraper scrapes real estate data from a website called 28hse.com.

Make sure you install selenium with 'pip install selenium' in your venv.
You will need Chrome installed on your system as well.

If you were navigate to https://www.28hse.com/en/rent/residential, you will see 15 listings
at the bottom of the page. Underneath you will see page numbers, from 1 to approx. 1050. These
are the listings and the pages that are scraped.

If you run the program, it will ask how many pages you want to scrape. Let's assume you select 2.
It will scrape the data from the 15 listings on the https://www.28hse.com/en/rent/residential 
page first, as it is page 1. 

It will then click on the right arrow at the bottom to navigate to page 2. It will then
scrape those 15 listings as well.

This is repeated based on how many pages you specified.

It creates a CSV file in the program folder and appends the data to it. The data scraped is as follows:

-Description
-Link to listing page
-District
-Address line 1
-Address line 2
-Saleable and gross area
-Lease price
-Agency name
-Description tags

Please note the data is appended to the CSV file. If you want to rerun the program, delete
the CSV file first to avoid duplications.