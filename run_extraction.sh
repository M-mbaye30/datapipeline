#executer ce script avec bash
#!/bin/bash

 cd /home/mouhamed-mbaye/dev/notionlearning

 source venv/bin/activate


 echo "====Extraction $(date) ====" >> cron.log

 python3 extraction.py >> cron.log 

 echo "" >> cron.log