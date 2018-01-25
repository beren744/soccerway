# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("https://us.soccerway.com/teams/england/chelsea-football-club/661/")
#
# # Find something on the page using css selectors (w3c page)
root = lxml.html.fromstring(html)
root.cssselect("td div a")
for name in names:
  print name.attrib['href']
  record['link']=name.attrib["href] 
#record is a variable for name.attrib
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
                             
                             
## # Write out to the sqlite database using scraperwiki library
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
