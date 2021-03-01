# scraping-quotes-authors
web scraping quotes and author details using scrapy from **http://quotes.toscrape.com/**

## The files containing the scraped output data is present in the **tutorial/output** folder.

## prerequisite:
1. Have latest version of Python and pip installed.
2. Have both pip and python added to the environment variable.
3. Have **virtualenv** installed command to install - *pip install virtualenv*

## Instructions to setup environment on your own machine.

1. Clone or download the Zip from github. Unzip the folder.
2. Change directory into the project folder **scraping-quotes-authors**
3. create a virtual environment using the command - *virtualenv venv*
4. activate the virtual environment - *source venv/Scripts/activate*(linux) or *venv\Scripts\activate*(windows)
5. install required dependencies from requirements.txt - *pip install -r requirements.txt*
6. if you have issues with installing any modules install it individually using pip. *pip install <module_name>*
7. Issue with Twisted module on windows.
  - You might have issue while installing twisted module on windows.
  - we need to install this using wheel(**.whl**) file provided **Twisted-20.3.0-cp39-cp39-win_amd64.whl**
  - To install twisted using wheel(**.whl**) file - *pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl*
8. Try installing from requirements.txt again

## Executing the Spiders(web Scrapers).
1. Change Directory to the **tutorial** folder(Topmost one) - *cd tutorial*
2. There are two Spiders one scrapes the Author data and another scrapes the Qoutes.
3. Scraping Spiders command structure - *Scrapy crawl <Spider Name> -o <folder(optional)>/<filename.extension>*
4. Scraping authors - *Scrapy crawl author -o output/author.json*
5. Scraping quotes - *Scrapy crawl quotes - o output/quotes.json*
6. we can also extract in *.csv* and *.jl* formats.
7. important that we are in the Topmost **tutorial** folder and not the one inside it.
