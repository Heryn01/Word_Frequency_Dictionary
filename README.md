# Word_Frequency_Dictionary

A word frequency python dicitonary generated using the Scrapy framework to parse an html version of To Kill a Mockingbird, extendable to other web texts.

Word frequency dictionary usage:
  1. Download repository
  2. In the repository directory, naviagate to '/FrequencyDict/FrequencyDictionary/'
  3. Run frequency.py to receive a human readable dictionary of words and their associated number of uses.
  
Scrapy:
  1. Make sure Scrapy is installed on the runtime environement (conda installation recommended).
  2. navigate to /reponame/FrequencyDictionary/spiders/freebooks_spiders.py
  3. Edit parse function as necessary with correct css selectors for other books.
