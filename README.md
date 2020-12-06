![logo](./Templates/mars.jpeg)
# Mission-to-Mars: *a journey in scraping*... 


## Background
Our Mission to Mars web app is underway, but more data needs to be added and some modifications need to be made.  ***So what's next?***

Thanks to the scrape friendly NASA websites, we can include all four of the hemisphere images!  Modifying the scrape app and the HTML, this next phase of the app will include the 4 hemispheres, their titles, and thumbnail images. 

## Objectives
The focus of this phase spans 3 deliverables:

1. Scrape Full-Resolution Mars Hemisphere Images and Titles
2. Update the Web App with Mars Hemisphere Images and Titles
3. Add Bootstrap 3 Components

## Resources
The following resources were used to create the code for the scrape, the app to run it, and the visualization  

* Code: 
	1. Python and many imports including Pandas, ChromeDriverManager, and DateTime
	2. BeautifulSoup
	3. Splinter
* App and Database : 
	1. Flask
	2. Mongo DB to store and update the database
* Vizualization: 
	1. HTML
	2. Bootstrap 3
* Web sites scraped:
	* [https://mars.nasa.gov/news/]()
	* [https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars]()
	* [http://space-facts.com/mars/]()
	* [https://mars.nasa.gov/insight/weather/]()
	* [https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars]()
	 

## Obstacles
Part of the starter code includes a scrape of ```https://mars.nasa.gov/insight/weather/```. However, NASA's Insight has stopped reporting on daily weather at the time this project was completed.

Regardless - and in hopes it NASA would resume publicizing this data - a chart was created (empty) and displayed with the Mars Facts section.  A public, scrape-friendly website with daily MARS temperature site could not be found to replace.  Let's hope NASA starts reporting this data again soon!

## Enhancements
Layout and colors were altered from the original visualization using Bootstrap 3 and CSS elements.  In addition, the following Bootstrap elements were included:

1. **Glowing Scrape Button**: 
	* Employing the orange color of mars, the SCRAPE NEW DATA button glows on an infinite loop to grab the attention of the user.
	* The button text becomes underlined to show the button has been clicked and app is processing.
2. **Background image** to the Jumbotron Title: used the space portion of the image from Module 10 thumbnail...I knew it was safe!
3. **Hyperlinked Thumbnail** images of the hemispheres are included at the bottom of the web page.


