#! /usr/bin/python
import urllib.request as req
from bs4 import BeautifulSoup
import time
import json
import os
import re
import sys

class Webparser():
	def __init__(self):
		pass

	def redcheck(self):
		time.sleep(2.0)
		print("\n\n", "==" * 8, " Trying reddit feed check ", "==" * 8, "\n\n")
		self.url = "https://old.reddit.com/top/"
		#download the URL and extract the content to the variable html 
		self.request = req.Request(self.url)
		self.html = req.urlopen(self.request).read()
		#print(html)
		#pass the HTML to Beautifulsoup.
		self.soup = BeautifulSoup(self.html,'html.parser')
		#get the HTML of the table called site Table where all the links are displayed
		self.main_table = self.soup.find("div",attrs={'id':'siteTable'})
		#Now we go into main_table and get every a element in it which has a class "title" 
		self.links = self.main_table.find_all("a",class_="title")
		self.extracted_records = []
		for self.link in self.links: 
			time.sleep(1.0)
			self.title = self.link.text
			self.url = self.link['href']
			self.record = {
			'title':self.title,
			'url':self.url
			}
			self.extracted_records.append(self.record)
			time.sleep(2.0)
			if int(len(self.extracted_records)) >= 5:
				break	
		print(self.extracted_records)
		print("\n\n", "==" * 8, " reddit feed check Done ", "==" * 8, "\n\n")
		time.sleep(2.0)

	def redcheck_json(self):
		time.sleep(2.0)
		print("\n\n", "==" * 8, " Trying reddit feed check as json ", "==" * 8, "\n\n")
		self.file_input = input("Please specify the json file name to store the data \n\n>")
		validsyn = r'.json'
		self.file_validation =  re.match(validsyn, self.file_input)
		if self.file_validation:
			pass
		else:
			print("\n\n" "Try input json file name again as \"json!!\"", "\n\n")
			sys.exit()
		self.url = "https://old.reddit.com/top/"
		#download the URL and extract the content to the variable html 
		self.request = req.Request(self.url)
		self.html = req.urlopen(self.request).read()
		#print(html)
		#pass the HTML to Beautifulsoup.
		self.soup = BeautifulSoup(self.html,'html.parser')
		#get the HTML of the table called site Table where all the links are displayed
		self.main_table = self.soup.find("div",attrs={'id':'siteTable'})
		#Now we go into main_table and get every a element in it which has a class "title" 
		self.links = self.main_table.find_all("a",class_="title")
		self.extracted_records = []
		for self.link in self.links: 
			time.sleep(1.0)
			self.title = self.link.text
			self.url = self.link['href']
			self.record = {
			'title':self.title,
			'url':self.url
			}
			self.extracted_records.append(self.record)
			time.sleep(2.0)
			if int(len(self.extracted_records)) >= 5:
				break
		with open(os.path.join('/tmp/', self.file_input), 'w') as self.outfile:
			json.dump(self.extracted_records, self.outfile, indent=4)
		print("\n", "The file has stored been stored as {}".format(self.outfile), "\n")
		print("\n\n", "==" * 8, " reddit feed check as json Done ", "==" * 8, "\n\n")
		time.sleep(2.0)

if __name__ == '__main__':
	searcher = Webparser()
	#searcher.redcheck()
	searcher.redcheck_json()

