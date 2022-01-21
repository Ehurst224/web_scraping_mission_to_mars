import pandas as pd
import pandas as pd
from IPython.display import HTML
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)

tables = pd.read_html(url)
mars_facts = tables[0]
mars_facts.columns = mars_facts.columns.get_level_values(0)
mars_facts


result = mars_facts.to_html()
print(result)