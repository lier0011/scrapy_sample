# scrapy_sample
A sample crawler using Scrapy to demonstrate how to scrape the list of the FIFA World Cup Finals from this source: 
https://www.topendsports.com/events/worldcupsoccer/winners.htm

## MODULES
The crawler uses scrapy, pandas and re (regex) in order to fulfill the task

## STEPS
* Instead scraping the data directly from the web, I downloaded a snapshot of the webpage, which is saved on data directory. So the web crawler actually uses the offline data by default.
* Once the data is fetched, I use xpath to navigate and extract the elements I want to parse, combined using regex to manipulate the text.
* The parser result is saved as dictionary packed in a list
* Using the DataFrames of Pandas, the data is finally saved into a CSV file

## DATA
* data/fifa_world_cup.html is the offline version of the page, which I grab on 25-01-24
* data/fifa_world_cup.csv is the export file which contains the parsed data

## HOWTO
* checkout the GIT repository
* go into the scrapy_sample directory
* requirements.txt is available, so you can install the dependencies required for this project
* go into the sub-directory fifa_world_cup
* run the command "scrapy crawl fifa"
* The webcrawler extracts the data and save into scrapy_sample/fifa_world_cup/data/fifa_world_cup.csv
