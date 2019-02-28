from urllib import request
from bs4 import BeautifulSoup
import requests
import csv
from urllib import request


csv_file = open('khaleej.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['JOB TITLE','DESCRIPTION','INDUSTRY','SALARY','EXPERIENCE','JOB TYPE','GENDER','STREET','CITY','LISTED DATE' ,'EXPIRES' ,'URL', 'EMAIL'])
page = 1

try:

	for x in range(100):
		file_url = r'https://buzzon.khaleejtimes.com/page/'+str(page)+'/?s=&sa=search&scat=39'
		def download_stoch_data(csv_url):
			response = request.urlopen(csv_url)
			csv = response.read()
			csv_str=str(csv)
			lines = csv_str.split("\\n")	
			dest_url = r'khaleejtimes.html'
			fx = open(dest_url, "w")
			for line in lines:
				fx.write(line + "\n")

		download_stoch_data(file_url)

		#for the link 
		with open('khaleejtimes.html') as html_file:
			soup2 = BeautifulSoup(html_file,'lxml')

		csv_file = open('khaleej.csv','a')
		csv_writer = csv.writer(csv_file)

		for Joblink in soup2.find_all('div', class_="post-right full"):
				
			try:
					job = Joblink.a['href']
					jobtitle = Joblink.a.text
					file_url2 = job

					def download_stoch_data(csv_url2):
						response = request.urlopen(csv_url2)
						csv = response.read()
						csv_str=str(csv)
						lines = csv_str.split("\\n")	
						dest_url = r'pages.html'
						fx = open(dest_url, "w")
						for line in lines:
							fx.write(line + "\n")
					download_stoch_data(file_url2)

					#for the Email and descriptions
					with open('pages.html') as html_file:
						soup3 = BeautifulSoup(html_file,'lxml')

					Jobemail= soup3.find('div', class_="bigright")
					jobe = Jobemail.a['href']
					jobesplit= jobe.split(':')[1]


					jobdesc = Jobemail.find(id="cp_industry").text
					jobdescsplit = jobdesc.split(':')[1]


					jsalary = Jobemail.find(id="cp_salary").text
					jsalarysplit= jsalary.split(':')[1]

 
					jexperience = Jobemail.find(id="cp_experience").text
					jexperiencesplit= jexperience.split(':')[1]

					jtype = Jobemail.find(id="cp_job_type").text
					jtypesplit = jtype.split(':')[1]

					jgender = Jobemail.find(id="cp_gender").text
					jgendersplit = jgender.split(':')[1]


					jstreet = Jobemail.find(id="cp_street").text
					jstreetsplit = jstreet.split(':')[1]

					jcity = Jobemail.find(id="cp_city").text
					jcitysplit = jcity.split(':')[1]

					jlisted = Jobemail.find(id="cp_listed").text
					jlistedsplit = jlisted.split(':')[1]

					jexpire = Jobemail.find(id="cp_expires").text
					jexpiresplit = jexpire.split(':')[1]

					Jdescription2 = soup3.find('div', class_="single-main")
					x = Jdescription2.p.text


					print(jobtitle)
					print(x)
					print(jobdescsplit)
					print(jsalarysplit)
					print(jexperiencesplit)
					print(jtypesplit)
					print(jgendersplit)
					print(jstreetsplit)
					print(jcitysplit)
					print(jlistedsplit)
					print(jexpiresplit)
					print(job)
					print(jobesplit)
					print()

			except Exception as e:
				print(e)
				job = None
				jobdescsplit= None
				jsalarysplit= None
				jexperiencesplit= None
				jtypesplit= None
				jgendersplit= None
				jstreetsplit= None
				jcitysplit= None
				jlistedsplit= None
				jexpiresplit= None
				jobesplit= None
			csv_writer.writerow([jobtitle,x,jobdescsplit,jsalarysplit,jexperiencesplit,jtypesplit,jgendersplit,jstreetsplit,jcitysplit,jlistedsplit,jexpiresplit,job,jobesplit])
		page += 1
except Exception as e:
 print(e)
 print("scraping Complete")
 print(page)
csv_file.close()





