ez2294
Final

Description of files present:

allwords.txt		- file containing all lyrics of all songs that have entered the billboard hot-100 in the past year
app.py
billboardcounter.py	- reads lyrics and counts number of times keyword occurs
readme.txt		- this file
RIP Nipsey 		- LIST.ipynb - lyric scrapping using lists
RIP Nipsey.ipynb 	- lyrics scrapping using sets
static			- images etc for Flask
templates		- web pages for Flask
test.html		- should probably remove this
test_files
words.txt 		- file containing all lyrics of all songs that have entered the billboard hot-100 in the past year (with duplicates removed)


Requirements for notebooks:
lyricsgenius  - API access token aswell
billboard
time


I suppose the only part of the project that needs explanation is the "Billboard Search" link. 
It basically returns to the user the number of times a given keyword has appeared in the 
Billboard Hot-100 between April-2019 to March-2020. Why only such a specific timeframe? Because I initially 
wanted to find out how many times a specific musician (who passed away in March-2019) was mentioned after he passed.
After I built it around this specific purpose I realized it could be used for any keyword. 

The notebook contains the code used for scrapping the dataset of lyrics using an API from genius.com

Everything else is pretty much standard according the FINAL prompt. 