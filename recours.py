# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

# D'ABORD, ON CRÉE UNE VARIABLE AVEC NOTRE URL DE DÉPART
url1 = "http://services.justice.gouv.qc.ca/dgsj/rrc/Demande/DemandeRecherche.aspx"


fich = "recourscollectifs.csv"

entetes = {
	"User-Agent":"CLegault - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"c_legault@icloud.com"
}

contenu = requests.get(url1, headers=entetes)


page = BeautifulSoup(contenu.text,"html.parser")

print(page)


i = 0


for ligne in page.find_all("tr"):
    
  
    if i != 0:

        print(ligne)
       
   
        lien = ligne.a["href"]
        # print(lien)
        
        
        hyperlien = "http://services.justice.gouv.qc.ca/dgsj/rrc/Demande/" + lien
        print(hyperlien)

        
        contenu2 = requests.get(hyperlien, headers=entetes)
        page2 = BeautifulSoup(contenu2.text, "html.parser")
        
        
        recours = []
        
        
        recours.append(hyperlien)
        
        
        for item in page2.find_all("tr"):
            # print(item)
            
            
            if item.td is not None:
                recours.append(item.td.text)
            
            # SINON (SI C'EST DU NÉANT), AJOUTE «None» À NOTRE LISTE
            else:
                recours.append(None)
        
        print(recours)
        
       
        achille = open(fich,"a")
        talon = csv.writer(achille)
        talon.writerow(recours)
        
    # ON AUGMENTE NOTRE COMPTEUR DE 1
    i =+ 1
       
        