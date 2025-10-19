# Esempio di Progetto Docker con Python e Flask

Questo progetto è un semplice esempio di come "dockerizzare" un'applicazione web Python utilizzando Flask. L'applicazione contatta un'API online per ottenere immagini casuali di papere e le visualizza nel browser.

## Funzionalità

-   **Applicazione Flask**: Un semplice server web che risponde a una richiesta sulla root (`/`).
-   **API Esterna**: Utilizza l'API [random-d.uk](https://random-d.uk/api) per ottenere un URL di un'immagine di una papera in formato JSON.
-   **Docker**: Il progetto è configurato per essere eseguito all'interno di un container Docker, garantendo un ambiente di esecuzione consistente.
-   **Docker Compose**: Utilizza Docker Compose per semplificare l'avvio e la gestione del container.

## Prerequisiti

Assicurati di avere installato Docker sul tuo sistema.

-   [Docker](https://docs.docker.com/get-docker/)

## Struttura del Progetto

```
.venv
.gitignore
README.md
src/
├── Dockerfile
├── app.py
├── data_retriver.py
├── docker-compose.yml
└── requirements.txt
```

-   `src/app.py`: Il file principale dell'applicazione Flask.
-   `src/data_retriver.py`: Un modulo per recuperare i dati dall'API.
-   `src/Dockerfile`: Le istruzioni per costruire l'immagine Docker dell'applicazione.
-   `src/docker-compose.yml`: Il file di configurazione per Docker Compose.
-   `src/requirements.txt`: Elenca le dipendenze Python del progetto.
