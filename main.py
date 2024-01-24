import requests
from bs4 import BeautifulSoup

def trouver_lien_moacloud(url):
    # Faire la requête HTTP pour obtenir le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver tous les éléments avec attribut 'src' contenant 'moacloud.com'
        elements = soup.find_all(src=lambda value: value and 'moacloud.com' in value)

        # Rechercher le lien contenant "moacloud.com"
        for element in elements:
            print(f"Le lien trouvé est : {element['src']}")

        # Si aucun lien n'est trouvé
        if not elements:
            print("Aucun lien contenant 'moacloud.com' n'a été trouvé sur la page.")
    else:
        # En cas d'échec de la requête
        print(f"La requête a échoué avec le code d'état {response.status_code}.")

# Exemple d'utilisation
url_de_la_page = input("Merci d'indiquer l'url de la page ex : https://xakraf.com/rmznt0k9a/b/xakraf/13949784\n >>>")
trouver_lien_moacloud(url_de_la_page)
