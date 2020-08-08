Oprócz standardowych modułów Pythona użyłem:
peewee
pip install peewee

parse
pip install python-dateutil

requests
pip install requests




1.Żeby stworzyć data base trzeba najpierw trzeba uruchomić operations.py
2.Żeby zapisać dane do bazy trzeba uruchomić main.py (to także pozwala na usunięcie pola 'picture' z pliku 'persons.json' 
lub użyć komendy   python script.py -save-data  
3.W pliku models.py zawarta jest struktura bazy
4.Plik new_data_from_api.py pozwala na pobierania danych z api


Spis dostępnych komend:
-average-age female
-average-age male
-average-age middle
-average-age all

-percentage female
-percentage male
-percentage all

-most-popular-cities (Enter the number of cities to be displayed)

-most-popular-passwords (Enter the number of passwords to be displayed)


'--db1'   oraz    '-born-between-d1'  take str data for example '1998.01.01' or '1998-01-01' and ect...
'--db2'   oraz    '-born-between-d2'  take str data for example '1998.01.01' or '1998-01-01' and ect...
For exemple: 
python scripts.py --db1 1998/07/01  --db2 2001.03.05


-password-strength      
return the most strangth password


-save-data   
Enter to save date from from "persons.json" in data base


-delete-picture
Enter to delete picture field from "persons.json"



-new-data (Enter the number of random entries to add to db)

