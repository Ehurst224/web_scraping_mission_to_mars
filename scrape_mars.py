# Dependencies
from bs4 import BeautifulSoup as bs
#import requests
#import pymongo
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
    featured_image = 'image/featured/mars1.jpg'
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
    # mars_facts


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
    cerberus_image = 'images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'
    cerberus_image

    # Find URL
    cerberus_image_url = 'https://marshemispheres.com/' + cerberus_image
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
    schiaparelli_image = 'images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'
    schiaparelli_image

    # Find URL
    schiaparelli_image_url = 'https://marshemispheres.com/' + schiaparelli_image
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
    syrtis_image = 'images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'
    

    # Find URL
    syrtis_image_url = 'https://marshemispheres.com/' + syrtis_image


    # ### Valles Marineris

    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)

    # Create BeautifulSoup object; parse
    html = browser.html
    soup = bs(html, 'html.parser')

    # Find Title
    valles_title = soup.find('h2', class_='title').text
    

    # Find link
    valles_image = 'images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'
    print(valles_image)

    # Find URL
    valles_image_url = 'https://marshemispheres.com/' + valles_image
   


    # ### Append Dictionary

    hemisphere_image_urls = [
        {"title": valles_title, "img_url": valles_image_url},
        {"title": cerberus_title, "img_url": cerberus_image_url},
        {"title": schiaparelli_title, "img_url": schiaparelli_image_url},
        {"title": syrtis_title, "img_url": syrtis_image_url},
    ]
   

    mars = {"news_title" : news_title,
        "text": news_p,
        "featured_image": featured_image, "featured_url": featured_image_url,
        # "Mars Facts": mars_facts,
        "valles_marineris_title": valles_title, "valles_marineris_url": valles_image_url,
        "cerberus_title": cerberus_title, "cerberus_url": cerberus_image_url,
        "schiaparelli_title": schiaparelli_title, "schiaparelli_url": schiaparelli_image_url,
        "syrtis_major_title": syrtis_title, "syrtis_major_url": syrtis_image_url
        }
    
    print(mars)
    browser.quit()
    return mars
# scrape()