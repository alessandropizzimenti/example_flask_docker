from flask import Flask
from data_retriver import DataRetriever

app = Flask(__name__)

@app.route('/')
def random_duck():
    retriever = DataRetriever("https://random-d.uk/api/random")
    duck_url = retriever.get_duck_url()
    
    if duck_url:
        # restituisce direttamente l'immagine senza salvarla
        return f'<img src="{duck_url}" alt="Papera">'
    else:
        return "Nessun dato ricevuto"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)