# Exif-Viewer
Questo progetto consiste in un Visualizzatore di immagini che analizza e mostra i Tag ed i rispettivi valori EXIF.

# Cosa sono gli Exif
Gli **Exif** (acronimo di **EX**changable **I**mage file **F**ormat sono il dettaglio tecnico sull'immagine appena registrata dalla fotocamera sotto forma di file. Alcuni esempi più comuni di informazioni contenute all'interno degli exif sono: risoluzione, tempo di scatto, sensibilità ISO, data e ora di acquisizione, ecc... . 
Alcune particolari informazioni contenute nei tag Exif sono quelle riguardanti la **Localizzazione**. In particolare, nei metadati possono essere incluse informazioni relative alla localizzazione degli scatti, che potrebbero provenire da un ricevitore **GPS** connesso alla fotocamera.

# Il Programma
Il programma in questione è un **Visualizzatore di immagini _.jpg_** che consente la visualizzazione dei tag Exif presenti all'interno dell'immagine. Di seguiro verranno presentate le **funzionalità principali**, la **GUI** e l'**implementazione** del programma.

## Funzionalità
In questa sezione si vogliono presentare brevemente le funzionalità del programma:
1. Consente di **caricare una lista di immagini .jpg**;
2. Presenta all'utente una sola immagine alla volta ed i relativi tag e valori Exif;
3. Consente di **ruotare l'immagine** incrementando la rotazione di 90° in senso orario;
4. Consente di **iterare all'interno della lista di immagini** presentando le immagini precedenti e successive all'interno della stessa;
5. Nel caso in cui sono presenti le informazioni di geolocalizzazione permette di **collegarsi a Google Maps visualizzando il luogo in cui è stata scattata la foto**;
6. Nel caso in cui la finestra venga ridimensionata, la fotografia presentata all'utente verrà **scalata di conseguenza mantenendo i rapporti originali dell'immagine**. La massima grandezza dell'immagine presentata all'utente è di _512px X 512px_.

## La GUI
All'interno della GUI possono essere individuati diversi elementi:
1. **Bottone per il caricamento delle immagini**: apre un modal che ci consentirà di selezionare la directory contente le immagini o le immagini che vogliamo visualizzare;
2. **Bottone per la localizzazione**: attivato solo se presenti le informazioni GPS dell'immagine, in questo caso al suo click aprirà una nuova scheda all'interno di un browser e si collegherà a google maps mostrando il luogo in cui è stata scattata l'immagine; 
3. **Bottone di rotazione dell'immagine**: incrementa la rotazione dell'immagine di 90° rispetto alla rotazione attuale;
4. **Bottone Previous**: permette di cambiare l'immagine corrente, caricando l'immagine precedente nella lista, aggiornando tutte le informazioni e gli elementi grafici all'interno GUI; 
5. **Bottone Next**: permette di cambiare l'immagine corrente, caricando quella successiva nella lista, aggiornadno tutte le informazioni e gli elemenit grafici all'interno della GUI; 
6: **Tabella Exif**: presenta le informazioni EXIF contenute all'interno dell'immagine corrente.

#### Shortcut
Un elemento fondamentale per migliorare l'esperienza dell'utente sono le **shortcut** (scorciatoie). All'interno del programma sono presenti tante scorciatoie quante sono le azioni, tranne che per l'azione di caricamento delle immagini.
In particolare, le _shortcut_ inserite all'interno del programma sono le seguenti:


# Implementazione
