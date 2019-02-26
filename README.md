PythTube - YT downloader / mp3 converter

Συγγραφέας: Κώστας Κόντος

ΟΔΗΓΙΕΣ ΕΓΚΑΤΑΣΤΑΣΗΣ ΠΡΟΑΠΑΙΤΟΥΜΕΝΩΝ ΚΑΙ ΧΡΗΣΗΣ

1. sudo apt-get install ffmpeg (για την λειτουργία της μετατροπής σε mp3)
2. rm -rf env
3. virtualenv env (αν δεν υπάρχει, πρώτα sudo apt-get install python3-pip και
   μετά sudo -H pip3 install virtualenv)
4. source env/bin/activate
5. pip install -r requirements.txt
6. python modules/video_dl.py

Σημειώσεις
- Προσοχή στα path, είναι καλύτερα να μην αφήσετε το path αποθήκευσης του
  βίντεο κενό
- Αντί για ~ χρησιμοποιήστε /home/username/
