import requests
import json
from models import People
from datetime import datetime
from main import Data_processing,Save_data_base



class New_users_from_api(Save_data_base):
    def save_new_db(self, how_many_new_users):

        url='https://randomuser.me/api/'
        param='results=%s'%how_many_new_users
        res = requests.get(url,param)
        js_data = json.loads(res.text)


        for person_data in js_data["results"]:
                
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

                            phone=int(super(New_users_from_api, self).phone_cleaner(person_data['phone'])),
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
                            number_of_days_before_birthday=super(New_users_from_api, self).number_of_days_befor_birthday(datetime.strptime(person_data['dob']['date'], "%Y-%m-%dT%H:%M:%S.%fZ"), datetime.now())
                
                
        )
        p_db.save()

if __name__=='__main__':
    save_new=New_users_from_api()
    save_new.save_new_db(5)