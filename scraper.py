# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# First import libraries
# The word 'import' is a command that you use to import a library into your code and it's followed by the name of the library.
# Libraries are collections of functions and other code has been written by other people to solve a particular collection of problems.
import scraperwiki
import lxml.html
#
# # Read in a page
# The line of code goes to a specific URL, scrapes all the html from that page using a function from
# the scraperwiki library called 'scrape()' and puts it in a new variable we call html
html = scraperwiki.scrape("https://www.sdlauctions.co.uk/property-list/")

# # Now that the URL is in quotation marks it is being supplied as a string
# Add a print command to see that varibla html
# Print the variable html containing the webpage
# print(html)
#
# # Drilling down into the page - Find something on the page using css selectors
# These lines dig further into the webpage
# The first line converst it to a type of variable it can do this with - don't need to change it
root = lxml.html.fromstring(html)

# The css selector is the only bit you need to change when adapting this code to different webpages
# Change "div[align='left']" to a different CSS selector to grab something else
# root.cssselect("div[align='left']")

# # To adapt this for your own purposes, you first need to identify the html code you want to target in your webpage
# Change "li p a" to a different CSS selector to grab something else
# Look for an a tag inside a p tag inside an li tag
# Store the matches in a new variable called 'matchedlinks'
matchedlinks = root.cssselect("li p a")
#print that
# print(matchedlinks)

# # matchedlinks is a list, so it starts and ends with a square bracket and each is saparated by a comma
# The list is very long because there are a lot of matches for the pattern indentified by the CSS selector
# Each item doesn't make much sense so convert each item back to something that makes sense
# To do something with each item, we need to "loop through" that list and deal with each item in turn.

# Create a dictionary called record
record = {}
# Loop through the items in the matchedlinks, calling each one li
for li in matchedlinks:
  # Store the text contents for li in a new variable listtext
  listtext = li.text_content()
  print(listtext.encode('utf-8'))
  # The function .text_content() converts the confusing item <Element a at 0x7f751c00a680> into someting readable :
  # the text contents of the tag that was grabbed.
  # Store in the 'record' dictionary under the key 'address'
  record['address'] = listtext
  # Save the record to the datastore with 'address' as a unique key
  scraperwiki.sqlite.save(['address'],record)

# The function .text_content() converts the confusing item <Element a at 0x7f751c00a680> into someting readable :
# the text contents of the tag that was grabbed.

# # We store that in a variable and print it.
# At this point we can comment out some print commands which take up an unnecessary time.

# # It should print a lot of text and hit an error (that we'll solve later)
# A whole bunch of data has been scraped, now it's time to get it out...

# # Saving the scraped data
# Data is often savec in a type of variable called dictionary. Dictionary = series of paris (called key-value pairs)
# We need to save the data in two stages
# Store each part of data in a dictionary variable under some sort of key, like "address".
# Store each dictionary in a table, one row (dictionary) at a time.

# # We add the line before within the loop which stores some information inside that dictionary.
# The address bit creates a key in the dictionary. Think of it like a column header in a table.
# listtext is stored against that key, like it's being put in that column.

# # Now that we've stored the data in the dictionary, we need to save it to a table. We need another line:
# scraperwiki.sqlite.save(['address'],record) - (This is added inside the loop).
# This saves record (the dictionary) to a sqlite database.

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
