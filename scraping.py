
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape_all():
    browser = Browser('chrome', **executable_path, headless=True)
    
    #initiate dictionary of data; scrape results
    mars_dict ={}
    
    # calls functions
    news_title, news_p = mars_news(browser)
    img_url = featured_image(browser)
    #weather_table = mars_weather(browser)
    hemisphere_image_urls = mars_hemi(browser)

    # Run all scraping functions and store results in a dictionary
    mars_dict['news_title'] = news_title
    mars_dict['news_paragraph'] = news_p
    mars_dict['featured_image'] = img_url
    mars_dict['mars_weather'] = mars_weather()
    mars_dict['facts'] = mars_facts()
    mars_dict['last_modified'] = dt.datetime.now()
    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls
    
    # Stop webdriver and return data
    browser.quit()
    return mars_dict

def mars_news(browser):
    # Scrape Mars News
    # Visit the NASA Mars News Site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    #slide_elem.find("div", class_='content_title')
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        # Use the parent element to find the first a tag and save it as `news_title`
        news_title = slide_elem.find_all("div", class_='content_title')[0].get_text()
        #news_title = slide_elem.find("div", class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find_all('div', class_="article_teaser_body")[0].get_text()
    except AttributeError:
        return None, None
    
    return news_title, news_p  

# Use the parent element to find the first a tag and save it as `news_title`
#news_title = slide_elem.find("div", class_='content_title').get_text()
#news_title

# Use the parent element to find the paragraph text
#news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
#news_p

#### Featured Image Scrape
def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')[0]
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    
    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url

#### Mars Facts
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]
    
    except BaseException:
      return None

     # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

### Adding in MARS WEATHER - not requested in Module, but part of started code.
def mars_weather():    
    # Visit the weather website
    #url = 'https://mars.nasa.gov/insight/weather/'
    #browser.visit(url)

    # Parse the data
    #html = browser.html
    #weather_soup = soup(html, 'html.parser')

    # Scrape the Daily Weather Report table
    #weather_table = weather_soup.find('table', class_='mb_table')
    #return weather_table.prettify()

    # Try to grab the data (or lack of data) a different way
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df2 = pd.read_html('https://mars.nasa.gov/insight/weather/')[0]
    
    except BaseException:
      return None

    # columns aleday assigned and set index of dataframe to 'earth' date.
    df2.columns=['Date', 'Mars Date', 'Max Air Temp (F|C)', 'Ave Air Temp (F|C)', 'Min Air Temp (F|C)',
           'Max Wind Speed (mph|m/s)', 'Ave Wind Speed (mph|m/s)', 'Min Wind Speed (mph|m/s)', 
            'Common Wind Speed (mph|m/s)', 'Max Pressure (Pa)', 'Ave Pressure (Pa)', 'Min Pressure (Pa)']

    df_t = df2.T
    if df_t.columns.tolist() == [0]:
        df_t.columns=['No Data Today - check back later!']

    # Convert dataframe into HTML format, add bootstrap
    return df_t.to_html(classes="table table-striped")

### Challenge 10 Begins; insert hemisphere data
def mars_hemi(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere
    html = browser.html
    hemi_soup = soup(html, 'html.parser')
    hemi_data = hemi_soup.find("div", class_="collapsible results")

    # pull out description for each hemisphere into a list to loop through 
    step1 = hemi_data.find_all('div', class_='description')
    hemisphere_image_urls = []
    # Loop through html, pull out 'h3' header with title and construct url from title (eliminate need to go to next page)
    try: 
        for each in step1:
            hemi_title = each.select_one('h3').get_text()
            hemi_title_link = hemi_title.replace(' ', '_').replace('Hemisphere','')
            hemi_link = f'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/{hemi_title_link}.tif/full.jpg'
            hemisphere_image_urls.append({'img_url': hemi_link, 'title':hemi_title})
    except AttributeError:
        return None

    # 4. Return the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
