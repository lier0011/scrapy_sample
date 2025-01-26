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
* data/fifa_world_cup_schema.sql is MySQL dump of the structure of table world_cup_winners. The table is used to save the crawled csv data.
* data/fifa_world_cup_data.sql contains the data saved in the table world_cup_winners. 

## HOWTO
* checkout the GIT repository
* go into the scrapy_sample directory
* requirements.txt is available, so you can install the dependencies required for this project
* go into the sub-directory fifa_world_cup
* run the command "scrapy crawl fifa"
* The webcrawler extracts the data and save into scrapy_sample/fifa_world_cup/data/fifa_world_cup.csv

## DATABASE
* import the structure using mysql command line. It is required that you already know which database is going to be used. Otherwise, create a new one, before importing the data.
  
  cat data/fifa_world_cup_schema.sql | mysql -u <your_user> -p <your_database>

* import the data from CSV into the database
  
  LOAD DATA INFILE "data/fifa_world_cup.csv" INTO TABLE world_cup_winners
  FIELDS TERMINATED BY ","
  ENCLOSED BY '"'
  LINES TERMINATED BY "\n"
  IGNORE 1 LINES;

* show the data

  SELECT * FROM world_cup_winners
  ![image](https://github.com/user-attachments/assets/c663a8bd-9c9a-4f03-b8a9-080f158da88e)
