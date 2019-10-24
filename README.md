# Loginner-for-RomaTre

## Requisiti

### Per i soli utenti Linux

Per poter utilizzare TKinter e inserire la password da una finestra

`$ sudo apt install python3-tk`

Per poter utilizzare PhantomJS, ovvero un browser headless

`$ sudo apt install fontconfig`

Per visualizzare una notifica sul DE in caso di successo

`$ sudo apt install notify-osd`

### Per tutti quanti

Download dei requisiti per Python

`$ pip3 install -r requirements.txt`

##### Web browser driver

Per permettere a Selenium di aprire il browser e operare su esso è necessario inserire i driver del relativo browser. Attualmente sono supportati Firefox, Chrome e PhantomJS. È importante scaricare i driver del browser che si ha installato sulla propria macchina. Nel caso in cui non compaia, scaricare i driver di PhantomJS

- **Chrome**: [Chrome driver](https://chromedriver.chromium.org/downloads "Chrome driver") 
- **Firefox**: [Firefox driver](https://github.com/mozilla/geckodriver/releases "Firefox driver")
- **PhantomJS**: [PhantomJS driver](https://phantomjs.org/download.html "PhantomJS driver")

## Setup

Dopo aver scaricato l'intero progetto e aver soddisfatto i requisiti, è necessario completare le seguenti operazioni all'interno dei relativi file di configurazione:

- **start_login.sh**
  Inserire all'interno della variabile `path_to_python_file` il percorso assoluto della cartella contenente il file `login_romatre_selenium.py`
- **login_page_data.json** 
  Inserire all'interno della variabile `username_value` l'username e all'interno di `password_value` la password. In questo modo sarebbe salvata in chiaro e chiunque abbia accesso al PC potrà vederla. Per evitare ciò è possibile inserirla ogni volta tramite una finestra che comparirà a schermo. Per scegliere questa strada lasciare vuoto il campo `password_value`, ovvero non inserire nessun carattere all'interno delle virgolette
- **web_browser_driver.json**
  Inserire il path assoluto del driver che si vuole utilizzare. Lasciare gli altri invariati, ci penserà il programma a prendere quello corretto :)
