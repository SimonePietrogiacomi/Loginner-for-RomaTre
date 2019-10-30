# Loginner for RomaTre

Tramite questo programma è possibile effettuare l'accesso alla rete WiFi di Roma Tre senza dover manualmente aprire il browser e inserire i dati

## Requisiti

Il requisito fondamentale e comune a tutti i sistemi operativi è `Python 3`, di seguito vengono indicati i successivi

### Linux

`$ sudo apt install python3-tk fontconfig notify-osd`

### Linux, Windows e Mac

Download dei requisiti per Python

`$ pip3 install -r requirements.txt`

##### Web browser driver

Per permettere a Selenium di aprire il browser e operare su esso è necessario inserire i driver del relativo browser. Attualmente sono supportati Firefox, Chrome e PhantomJS. È importante **scaricare** ed **estrarre** i driver del browser che si ha installato sulla propria macchina. Nel caso in cui non compaia, scaricare i driver di PhantomJS

- **Chrome**: [Chrome driver](https://chromedriver.chromium.org/downloads "Chrome driver") 
- **Firefox**: [Firefox driver](https://github.com/mozilla/geckodriver/releases "Firefox driver")
- **PhantomJS**: [PhantomJS driver](https://phantomjs.org/download.html "PhantomJS driver")

## Setup

Dopo aver scaricato l'intero progetto e aver soddisfatto i requisiti, è necessario completare le seguenti operazioni all'interno dei relativi file di configurazione:

- **login_page_data.json** 
  Inserire all'interno della variabile `username_value` l'username e all'interno di `password_value` la password. Attenzione però al fatto che in questo modo verrebbe salvata in chiaro e chiunque abbia accesso al PC potrà vederla. Per evitare ciò è possibile inserirla ogni volta tramite una finestra che comparirà a schermo. Per scegliere questa strada lasciare vuoto il campo `password_value`, ovvero non inserire nessun carattere all'interno delle virgolette
- **web_browser_driver.json**
  Inserire il path assoluto del driver che si vuole utilizzare. Lasciare gli altri invariati, ci penserà il programma a prendere quello corretto :)

## Utilizzo

Tramite il comando `python3 login_romatre_selenium.py` è possibile avviare il programma. 

Nel caso in cui si utilizzi Linux, si può avviare tramite `./start_login.sh`. È inoltre possibile avviare il programma all'accensione del PC eseguendo lo script appena citato appena finito il boot

## Testing

Attualmente è stato testato sul SO Linux Mint 19.2 Mate

## TODO

- Creare uno script d'avvio per Windows
- Creare o testare uno script d'avvio per Mac
- Testare l'applicativo su Windows e Mac
- Aggiungere il supporto a Safari e, eventualmente, altri browser
