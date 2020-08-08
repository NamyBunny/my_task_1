from models import People
import json
from pprint import pprint
from datetime import datetime

class Data_processing():

    # oczyść numer telefonu ze znaków specjalnych (powinny zostać same cyfry)

    def phone_cleaner(self, symbols):
        phone=''
        for symbol in symbols:
            if symbol.isdecimal():
                phone+=symbol
        return phone

    # stwórz dodatkowe pole z liczbą dni pozostałych do urodzin danej osoby

    def number_of_days_befor_birthday(self,birthday, date_now):
        

        if_leap_year=0
        if ((birthday.year in range(1900,date_now.year, 4) and birthday.month==2 and birthday.day==29) or (date_now.year in range(1900,date_now.year,4))and date_now.month==2 and date_now.day==29):
            if_leap_year=1
            birthday=datetime(birthday.year, birthday.month, birthday.day-1)

        
        if (birthday.month==date_now.month and birthday.day<=date_now.day) or birthday.month<date_now.month:
            date1=date_now
            date2=datetime(date_now.year+1, birthday.month, birthday.day)
            delta=date2-date1
            days=delta.days
            return days+if_leap_year

        else:
            date1=date_now
            date2=datetime(date_now.year, birthday.month, birthday.day)
            delta=date2-date1
            days=delta.days 
            return days
        
    # usuń pole ‘picture’.

    def delete_picture(self):
        with open('persons.json', 'r', encoding='utf-8') as f:
            people_data = json.load(f)
        
        
            dict_list_1=[]
            try:
                for person_data in people_data["results"]:
                    del person_data['picture']
                
                    dict_list_1.append(person_data)
            
                j_dict={'results':dict_list_1, "info":{"seed":"abc","results":1000,"page":1,"version":"1.3"}}
                with open('persons.json', 'w') as f:
                    json.dump(j_dict, f)
            except KeyError:
                print('The picture field has already been deleted')
    


class Save_data_base(Data_processing):

    def save_db(self):
        with open('persons.json', 'r', encoding='utf-8') as f:
            people_data = json.load(f)

            for person_data in people_data["results"]:
                

                p_db = People.create(
                            gender=person_data['gender'],
                            title=person_data['name']['title'],
                            first_name=person_data['name']['first'],
                            last_name=person_data['name']['last'],
                            street_number=int(person_data['location']['street']['number']),
                            street_name=person_data['location']['street']['name'],
                            city=person_data['location']['city'],
                            state=person_data['location']['state'],
                            country=person_data['location']['country'],
                            postcode=str(person_data['location']['postcode']),
                            coordinates_latitude=float(person_data['location']['coordinates']['latitude']),
                            coordinates_longitude=float(person_data['location']['coordinates']['longitude']),
                            timezone_offset=int(person_data['location']['timezone']['offset'].split(':')[0]),

                            

                            timezone_description=person_data['location']['timezone']['description'],
                            email=person_data['email'],
                            
                            dob_date=datetime.strptime(person_data['dob']['date'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                            dob_age=person_data['dob']['age'],
                            
                            
                            registered_date=datetime.strptime(person_data['registered']['date'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                            registered_age=person_data['registered']['age'],

                            # oczyść numer telefonu ze znaków specjalnych (powinny zostać same cyfry)

                            phone=int(super(Save_data_base, self).phone_cleaner(person_data['phone'])),
                            cell=person_data['cell'],
                            id_name=person_data['id']['name'],
                            id_value=person_data['id']['value'],
                            nat=person_data['nat'],


                            uuid=person_data['login']['uuid'],
                            username=person_data['login']['username'],
                            password=person_data['login']['password'],
                            salt=person_data['login']['salt'],
                            md5=person_data['login']['md5'],
                            sha1=person_data['login']['sha1'],
                            sha256=person_data['login']['sha256'],
                            

                            # stwórz dodatkowe pole z liczbą dni pozostałych do urodzin danej osoby
                            number_of_days_before_birthday=super(Save_data_base, self).number_of_days_befor_birthday(datetime.strptime(person_data['dob']['date'], "%Y-%m-%dT%H:%M:%S.%fZ"), datetime.now())
                
                
        )
        p_db.save()

if __name__=='__main__':
    save_bata=Save_data_base()
    save_bata.delete_picture()
    save_bata.save_db()

