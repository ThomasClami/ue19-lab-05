import requests

def chiengue():
    source="https://random.dog/woof.json"
    r = requests.get(source)
    lien_chien = r.json()["url"]
    print(f"Voici un lien vers une image/gif de chien ! {lien_chien}")

if __name__ == "__main__":
    chiengue()
