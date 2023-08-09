#!/usr/bin/env python3

# I suggest creating a venv for this. I did it with `python3 -m venv daily_snapshot_venv` then source that with `source daily_snapshot_venv/bin/activate`.
# Install 'beautifulsoup4' to the venv

# This program checks that the phpMyAdmin daily downloads are within a day or two of the current time.
# We allow an extra day of wiggle room because of the possibility of working in different time zones.
#
# Written by Isaac Bennetch <bennetch@gmail.com>

import sys
import urllib.request
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("The BeautifulSoup module is not available. Please make sure you have the proper module or are running the correct venv.")
    sys.exit(1)
import datetime

#############
# Main code #
#############


download_url = 'https://www.phpmyadmin.net/downloads/'

page = urllib.request.urlopen(download_url)
soup = BeautifulSoup(page, 'html.parser')
full_text = soup.get_text()
split = full_text.split("generated")

today_date = datetime.date.today()

exit_code = 0

# Process each instance of the keyword on the page, because we can have multiple QA and master versions
for substring in split:
  # Take only the date, not the entire page following it
  generated_date = substring.split()[0]
  # Strip off the trailing comma
  if generated_date.endswith(','):
    generated_date = generated_date[:-1]
  if generated_date != 'phpMyAdmin':
    converted_date = datetime.datetime.strptime(generated_date, '%Y-%m-%d').date()
    difference = today_date - converted_date
    # We give an extra day as a buffer to account for time zones
    if difference > datetime.timedelta(days=1):
      print("Problem found")
      print(("Current date: " + today_date.strftime('%Y-%m-%d')))
      print(("Snapshot date: " + generated_date))
      exit_code = 1
    else:
      print("Everything is groovy")

sys.exit(exit_code)
