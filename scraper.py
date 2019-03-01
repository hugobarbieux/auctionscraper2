# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")
# print(html)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
matchedlinks = root.cssselect("li p a")
# print(matchedlinks)

# Create a dictionary called record
record = {}
# Loop through the items in the matchedlinks, calling each one li
for li in matchedlinks:
  # Store the text contents for li in a new variable listtext
  listtext = li.text_content()
  print(listtext.encode('utf-8'))
  # Store in the 'record' dictionary under the key 'address'
  record['address'] = listtext
  # Save the record to the datastore with 'address' as a unique key
  scraperwiki.sqlite.save(['address'],record)

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
