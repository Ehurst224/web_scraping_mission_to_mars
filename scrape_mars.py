# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd

def scrape():
# # NASA Mars News


    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'http://redplanetscience.com/'
    browser.visit(url)

    # Create BeautifulSoup object; parse 
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find Title
    news_title = soup.find('div', class_='content_title').text
    news_title

    # Find Paragraph
    news_p = soup.find('div', class_='article_teaser_body').text
    news_p

    # # JPL Mars Space Images - Featured Image

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    # Create BeautifulSoup object; parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find link
    featured_image = soup.find('img', class_='headerimage')['src']
    featured_image

    # Find URL
    featured_image_url = 'https://spaceimages-mars.com/' + featured_image
    featured_image_url


    # # Mars Facts

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)

    tables = pd.read_html(url)
    mars_facts = tables[0]
    mars_facts.columns = mars_facts.columns.get_level_values(0)
    mars_facts


    # # Mars Hemispheres

    # ### Cerberus

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(url)

    # Create BeautifulSoup object; parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find Title
    cerberus_title = soup.find('h2', class_='title').text
    cerberus_title

    # Find link
    cerberus_image = soup.find_all('a')[4]['href']
    cerberus_image

    # Find URL
    cerberus_image_url = 'https://spaceimages-mars.com/' + cerberus_image
    cerberus_image_url


    # ### Schiaparelli

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(url)

    # Create BeautifulSoup object; parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find Title
    schiaparelli_title = soup.find('h2', class_='title').text
    schiaparelli_title

    # Find link
    schiaparelli_image = soup.find_all('a')[4]['href']
    schiaparelli_image

    # Find URL
    schiaparelli_image_url = 'https://spaceimages-mars.com/' + schiaparelli_image
    schiaparelli_image_url


    # ### Syrtis Major

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(url)

    # Create BeautifulSoup object; parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find Title
    syrtis_title = soup.find('h2', class_='title').text
    syrtis_title

    # Find link
    syrtis_image = soup.find_all('a')[4]['href']
    syrtis_image

    # Find URL
    syrtis_image_url = 'https://spaceimages-mars.com/' + syrtis_image
    syrtis_image_url


    # ### Valles Marineris

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)

    # Create BeautifulSoup object; parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find Title
    valles_title = soup.find('h2', class_='title').text
    valles_title

    # Find link
    valles_image = soup.find_all('a')[4]['href']
    valles_image

    # Find URL
    valles_image_url = 'https://spaceimages-mars.com/' + valles_image
    valles_image_url


    # ### Append Dictionary

    hemisphere_image_urls = [
        {"title": valles_title, "img_url": valles_image_url},
        {"title": cerberus_title, "img_url": cerberus_image_url},
        {"title": schiaparelli_title, "img_url": schiaparelli_image_url},
        {"title": syrtis_title, "img_url": syrtis_image_url},
    ]
    hemisphere_image_urls

    mars = [
        {"News Title" : news_title,
        "Text": news_title,
        "Featured Image": featured_image, "Featured Image URL": featured_image,
        "Mars Facts": mars_facts,
        "Valles Marineris Title": valles_title, "Valles Marineris URL": valles_image_url,
        "Cerberus Title": cerberus_title, "Cerberus URL": cerberus_image_url,
        "Schiaparelli Title": schiaparelli_title, "Schiaparelli URL": schiaparelli_image_url,
        "Syrtis Major Title": syrtis_title, "Syrtis Major URL": syrtis_image_url
        }
    ]
    mars