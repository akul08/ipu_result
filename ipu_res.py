''' </> by Akul Mehra '''
from bs4 import BeautifulSoup as bs # To parse the html page
import subprocess # To run a command to download pdf.
import requests # To Download the Html page of GGSIPU Results

url = "http://ggsipuresults.nic.in/ipu/results/resultsmain.htm"
link = ''

r = requests.get(url)
soup = bs(r.text)

while 1:
	try:
		branch = raw_input('Enter Your Branch(hint : CSE) : ').upper() or 'CSE'
		sem = raw_input('Enter Your Sem(hint :2nd) : ') or '2nd'
		''' Find all the <td> elements that contain result info. '''
		start_branch = soup.find_all('td', style="width: 249px")

		for x in start_branch:
			next_sib = x.find_next_sibling('td').get_text() # The next column of page that comtains sem info.
			if sem in next_sib:
				if branch in x.get_text():
					print x.get_text(), next_sib
					y = raw_input("Want to see next Link? Y/N ") # If this is your result or next link. 
					if(y == 'Y' or y == 'y'):
						continue
					else:
						print 'Voila'
						print 'Your result Declared. Generating Link: '
						href = x.find_next_sibling('td').find_next_sibling('td').contents[1]
						''' PDF Link to your result. '''
						link = 'http://ggsipuresults.nic.in/ipu/results/' + href['href']
						print link
						break
		print "Finished"
		if(y == 'Y' or y == 'y'):
			print 'Result not Declared !'	
		break
	except:
		print 'Result not Declared !'
		break
if link:
	print('Starting Automatic Download , Please wait while Download finishes.')
	command = ['wget', link]
	output = subprocess.call(command) # Downloading Pdf Using wget.
	print 'Have a Nice Day!!'
