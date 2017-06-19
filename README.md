**_[!] spYDyishai is still a work in progress.. wait for it [!]_**
- guided / un-guided run
- make the guided run pretty
- build a web based front-end

**spYDyishai** is a spider like credentials harvester for gmail. (_it does not do any sort of google hacking / OSINT recon or such._)
The main idea behind **spYDyishai** is that it logs in to Gmail with any set of given initial credentials and it then looks for all saved passwords on the logedin account, if it finds any other Gmail accounts it will then follow to that account and do the same.. hopefully until the end of time and life as we know it.

[-] **spYDyishai** was written as a PoC after talking to Google.


## Prerequisites

None for now

## Usage

The `spYDyishai.py` file
---
  * `python spYDyishai.py` :: | **run it with flags for a quick execution or without any for a guided run**

  GENRAL
  - spYDyishai help       --sh
  - spYDyishai help file  --hf
  - set proxy             --p


  USER INPUT
  - manual input          --mi
  - from file             --fi

  SYSTEM OUTPUT
  - to screen             --os
  - to flat file          --of
  - to DB                 --odb

  MANAGE DATA
  - read from DB          --rfdb
  - delete from DB        --dfdb
  - delete all DB         --dadb
  - read from file        --rff
  - delete from file      --dff
  - delete all file       --daf


The `gmailConnect.py` file
---
    * `python gmailConnect.py` :: | **never actually needs to run on it's own, it includes all the crawling and leeching functionality**

The `dataManagement.py` file
---
  * `python dataManagement.py` :: | **never actually needs to run on it's own, it includes all the DB management functionality**

The `credentialslist.ini` file
---
  * `NO RUN FUNC` :: | **never actually needs to run on it's own, it includes all the credentials resources if you choose to work with a resource file**
