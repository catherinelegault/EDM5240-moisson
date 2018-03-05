# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "recours.csv"

for n in range(100,1700):
	url = "http://services.justice.gouv.qc.ca/dgsj/rrc/Demande/DemandeDetail.aspx?DemRecID={}".format(n)
	
	print(url)

	contenu = requests.get(url)
	page = BeautifulSoup(contenu.text,"html.parser")
	 #print(page)

	urlRecours = page.find_all("div", class_="title")
	print(len(urlRecours))

	for urlRecour in urlRecours:
			
			try:
				recours = []
				url2 = urlRecour.a["href"]
				
				#print(url2)
				
				recours.append(url2)

				contenu2=requests.get(url2)
				page2=BeautifulSoup(contenu2.text,"html.parser")

				titre=page2.find("h1", id="lblTitre".text
					print(titre)
					recours.append(titre)

				dossier=page2.find("span", id="lblNoDossierTitre").text
					print(dossier)
					recours.append(dossier)

				Palais=page2.find("span", id="lblPalaisTitre").text
					print(Palais)
					recours.append(Palais)

				print(recours)

				loud = open(fichier,"a")
				lary = csv.writer(loud)
				lary.writerow(recours)


			except:
			 	print("Nada")


# 	url2 = "http://services.justice.gouv.qc.ca" + url2
			# 	#print(url2)

			# 	contenu2 = requests.get(url2)
			# 	page2 = BeautifulSoup(contenu2.text,"html.parser")
			# 	#print(url2)


			# 	titre = page2.title.text.split("|")[0].strip()
			
			# 	recours.append(titre)
			# 	print(url2)

