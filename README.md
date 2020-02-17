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
![alt text](https://github.com/cerullosalvatore/Exif-Viewer/blob/master/screen_1.png)

#### Shortcut
Un elemento fondamentale per migliorare l'esperienza dell'utente sono le **shortcut** (scorciatoie) che è un set di uno o più tasti di una tastiera di un PC che richiamano una certa operazione del software qundo vengono premuti dall'utente. 
All'interno del programma sono presenti tante scorciatoie quante sono le azioni, tranne che per l'azione di caricamento delle immagini.
In particolare, le _shortcut_ inserite all'interno del programma sono le seguenti:
* **CTRL+M**: effettua l'azione della localizzazione dell'immagine;
* **CTRL+R**: effettua l'azione di rotazione dell'immagine;
* **left arrow**: effettua l'operazione di switching dell'immagine corrente a quella precedente nella lista;
* **right arrow**: effettua l'operazione di switching dell'immagine corrente a quella successiva nella lista.

####ToolTip
Le funzioni, come le scorciatoie sono presentate all'utenete attraverso dei **ToolTip**: messaggi di testo che vengono visualizzati quando il cursore è posizionato su un pulsante.
![alt text](https://github.com/cerullosalvatore/Exif-Viewer/blob/master/screen_2.png)

# Implementazione
Il sistema è stato progettato attraverso il paradigma del **Model-View-Controller**. Secondo questo modello è possibile dividere un'applicazione interattiva in tre comonenti: 
- **Modello**: cotiene i dati di base e le funzionalità correlate;
- **Viste**: mostrano le informazioni all'utente;
- **Controllori**: gestiscono l'input dell'utente e mediano la comunicazione tra viste e modello.
Nel caso in esame, sfruttando **Pyhton 3.7** e **PyQT5**, è stato possibile sfruttare l'**Observer-Pattern** in cui il **Modello** e la **Vista** possono _pubblicare_ informazioni sui cambiamento di stato e sulle interazioni; e **Vista** e **Controllore** possono _iscriversi_ a ciò di cui hanno bisogno.

## Struttura del progetto
All'interno di questa directory sono presenti diversi file e diverse directory, di seguito spiegherò brevemente cosa sono:
* **Icon**: directory contente le icone sfruttate dalla GUI;
* **ImageTest**: directory che contiene alcune immagini con cui è possibile testare la GUI.
* **Model**: directory contente i modelli dei dati dell'applicazione. Al suo interno sono presenti 5 file che si occupano della gestione dei dati. I file, nel dettaglio sono:
  - _localizationUtiliy.py_ : contiente delle funzioni utili per individuare le coordinate;
  - _model_ : contiene il modello con il quale il controllore andrà ad interagire;
  - _observableImage_ : contiene la definizione della classe rappresentatitva delle immagini Exif osservabile;
  - _observableList_ : contiene la definizione della classe rappresentattiva di una lista osservabile;
  - _observableObject_: contiene la definizione della classe di un semplice oggetto Osservabile.
* **View**: directory contente i file che definiscono la vista dell'applicazione. I file in essa contenuti sono:
  - _Main.ui_ : file generato dal programma _PyQt designer_ (sfruttato per la realizzazione dell'interfaccia);
  - _view.py_ : vista derivata dal file Main.ui attraverso il comando _pyuc5_;
  - _windowResizable.py_ : viene definita una QMainWindow che effettua l'Override dell'evento di ridimensionamento.
* _controller.py_ : questo file contiene tuttte le interazioni necessarie tra la vista ed il modello, è il **controllore** dell'applicazione;
* _main.py_ : main dell'applicazione.

## Test
Per poter testare il progetto, all'interno della directory **ImageTest** sono presenti alcune immagini .jpg che rispecchiano il funzionamento dell'applicazione. In particolare:
- _0.jpg_ : immagine (100x77) con alcune informazioni Exif ma senza GPS; 
- _1.jpg_ : immagine (1024x765) con Exif e informazioni GPS;
- _2.jpg_ : immagine (2682x1992) con Exif ma non GPS;
- _3.jpg_ : immagine senza alcuna informazione Exif.
