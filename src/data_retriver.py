import requests

class DataRetriever:
    def __init__(self, url):
        self.url = url

    def retrive_json(self):
        resp = requests.get(self.url)
        if resp.status_code == 200:
            return resp.json()
        return None
        
    def get_duck_url(self):
        data = self.retrive_json()
        if data and "url" in data:
            return data["url"]
        return None

if __name__ == "__main__":
    retriever = DataRetriever("https://random-d.uk/api/random")
    data = retriever.retrive_json()
    
    if data and "url" in data:
        print("URL immagine della papera:", data["url"])
    else:
        print("❌ Nessun dato ricevuto")
