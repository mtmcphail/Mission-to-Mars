# Mission-to-Mars...*a pictoral journey*


## Background
Our Mission to Mars web app is underway, but more data needs to be added and some modification need to be made.  So what's next?

Thanks to the scrape friendly NASA websites,  scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, you’ll use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

## Objectives
* Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles
* Deliverable 2: Update the Web App with Mars Hemisphere Images and Titles
* Deliverable 3: Add Bootstrap 3 Components

## Resources
Many technologies were used to create the code for the scrape, the app to run it, and the visualization  

* Code: 
	1. Python and many imports including Pandas, ChromeDriverManager, and DateTime
	2. BeautifulSoup
	3. Splinter
* App: 
	1. Flask
	2. Mongo DB to store and update the database
* Vizualization: 
	1. HTML
	2. Bootstrap 3

## Obstacles
Part of the starter code includes a scrape of ```https://mars.nasa.gov/insight/weather/```. However, NASA's Insight has stopped reporting on daily weather at the momment.

Regardless, a chart was created (empty) and displayed with the Mars Facts section.  A public, scrape-friendly website with daily MARS temperature site could not be found to replace.  Let's hope NASA styarts reporting this data again soon!

## Enhancements
Layout and colors were altered from original visualiztion.  In addition, the following Bootstrap elements were included:

1. Glowing Scrape Button: using the ornage color of mars, the SCRAPE NEW DATA button glows on an infinite loop to grab the attention of the user.
2. 
