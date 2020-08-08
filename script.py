import argparse
from models import People 
from datetime import date, datetime 
from dateutil.parser import parse
import re
from main import Save_data_base
from new_data_from_api import New_users_from_api

class My_functions():
    def averag_age(self, for_whom:str)->str:
        list_of_men_age=[]
        list_of_women_age=[]
        for person in People.select():
            if person.gender=='female':
                list_of_women_age.append(person.dob_age)
            else:
                list_of_men_age.append(person.dob_age)
        
        average_age_of_women =str(round(sum(list_of_women_age)/len(list_of_women_age),1))
        average_age_of_men=str(round(sum(list_of_men_age)/len(list_of_men_age),1))
        
        list_of_all_person_age=list_of_women_age+list_of_men_age
        average_age=str(round(sum(list_of_all_person_age)/len(list_of_all_person_age),1))
        
        if for_whom=='male':
            print('Average age of men is '+average_age_of_men+' years')
        if for_whom=='female':
            print('Average age of women is '+average_age_of_women+' years')
        if for_whom=='middle':
            print('Average age of all people is '+average_age+' years')
        if for_whom=='all':   
            print('Average age of women is '+average_age_of_women+' years \n\t Average age of men is '
            +average_age_of_men+' years \n\t Average age of all people is '+average_age+' years')


    def percentage_of_women_and_men(self, gender:str)->str:
        count_of_men=0
        count_of_women=0
        for person in People.select():
            if person.gender=='female':
                count_of_women+=1
            else:
                count_of_men+=1
        all_count=count_of_women+count_of_men
        if gender=='female':
            print('Percentage of women is '+str(count_of_women/all_count*100)+' %')
        if gender=='male':
            print('Percentage of men is '+str(count_of_men/all_count*100)+' %')


    def most_popular_cities(self, number_of_cities:int) ->str:
        list_of_cities=[]
        for person in People.select():
            list_of_cities.append(person.city)
        citi_count={}
        for citi in list_of_cities:
            
            citi_count.update({citi:list_of_cities.count(citi)})
        sort_citi= sorted(citi_count.items(), key=lambda x: x[1], reverse=True)
        
        count_of_iteration=0
        for citi, num in sort_citi:
            count_of_iteration+=1
            if count_of_iteration==1 and number_of_cities!=0:
                print(str(citi)+' was found in the database '+str(num)+' times. Is this the most popular city?')
            elif count_of_iteration<=number_of_cities:
                print(str(citi)+' was found in the database '+str(num)+' times')
            else:
                break
         

    def most_popular_passwords(self, number_of_passwords:int) ->str:
        list_of_passwords=[]
        for person in People.select():
            list_of_passwords.append(person.password)
        password_count={}
        for password in list_of_passwords:
                password_count.update({password:list_of_passwords.count(password)})
        sort_passwords= sorted(password_count.items(), key=lambda x: x[1], reverse=True)
        
        count_of_iteration=0
        for password, num in sort_passwords:
            count_of_iteration+=1
            if count_of_iteration==1 and number_of_passwords!=0:
                print('"'+str(password)+'"'+' was found in the database '+str(num)+' times. Is this the most popular password?')
            elif len(sort_passwords)<number_of_passwords:
                print('There are not so many passwords')
                break
            elif count_of_iteration<=number_of_passwords:
                print('"'+str(password)+'"'+' was found in the database '+str(num)+' times')
            else:
                break
        

    def born_in_between_dates(self,date1:str, date2:str) ->str:
        date1=parse(date1)
        date2=parse(date2)
        if date1>date2:
            later_date=date1
            earlier_date=date2
        else:
            later_date=date2
            earlier_date=date1

        print(later_date)
        for person in People.select():
            if person.dob_date<=later_date and person.dob_date>=earlier_date:
                print(str(person.title)+' '+str(person.first_name)+' '+str(person.last_name)+' was born in '+str(person.dob_date.date()))

    def password_strength(self):
        password_count={}
        for person in People.select():
            count=0
            if re.search('[0-9]', person.password):
                count+=1
            if re.search('[A-Z]', person.password):
                count+=2
            if re.search('[a-z]', person.password):
                count+=1
            if re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', person.password):
                count+=3
            if len(person.password)>=8:
                count+=5
            password_count.update({person.password:count})
        
        sort_passwords= sorted(password_count.items(), key=lambda x: x[1], reverse=True)
        print('The strongest password is ' +'"'+str(sort_passwords[0])+'"'+'.')








class Script_manager(My_functions,New_users_from_api):
    def script_manager(self):
        parser = argparse.ArgumentParser(description='Serves to run scripts')
        
        parser.add_argument(
        '-average-age',
        type=str,
        default='Nothing',
        help='Enter: female, male, middle, all',
        dest="age")
        
        parser.add_argument(
        '-percentage',
        type=str,
        default='Nothing',
        help='Enter: female, male, all',
        dest="gender")

        parser.add_argument(
        '-most-popular-cities',
        type=int,
        default=0,
        help='Enter the number of cities to be displayed',
        dest="number_of_cities")

        parser.add_argument(
        '-most-popular-passwords',
        type=int,
        default=0,
        help='Enter the number of passwords to be displayed',
        dest="number_of_passwords")

        parser.add_argument(
        '--db1','-born-between-d1',
        type=str,
        default='Nothing',
        help='Enter two dates to see employees born in between',
        dest="date1")
        parser.add_argument(
        '--db2','-born-between-d2',
        type=str,
        default='Nothing',
        help='Enter two dates to see employees born in between',
        dest="date2")

        parser.add_argument(
        '-password-strength',
        default=False, 
        action='store_true',
        help='Enter the number of passwords to be displayed',
        dest="password_strength")

        parser.add_argument(
        '-save-data',
        default=False, 
        action='store_true',
        help='Enter to save data from "persons.json" in data base',
        dest="save_data")

        parser.add_argument(
        '-delete-picture',
        default=False, 
        action='store_true',
        help='Enter to delete picture field from "persons.json".',
        dest="delete_picture")

        parser.add_argument(
        '-new-data',
        type=int,
        default=0,
        help='Enter the number of random entries to add',
        dest="new_data")

        args = parser.parse_args()
        # age-------------------------------------------------------------------
        if args.age !='Nothing':
            super(Script_manager, self).averag_age(args.age)
        # percentage------------------------------------------------------------
        if args.gender !='Nothing':
            super(Script_manager, self).percentage_of_women_and_men(args.gender)
        # cities----------------------------------------------------------------
        if args.number_of_cities !=0:
            super(Script_manager, self).most_popular_cities(args.number_of_cities)
        # passwords-------------------------------------------------------------
        if args.number_of_passwords !=0:
            super(Script_manager, self).most_popular_passwords(args.number_of_passwords)
        # betwen dates--------------------------------------------------------------
        if args.date1 !='Nothing' and args.date2 !='Nothing':
            super(Script_manager, self).born_in_between_dates(args.date1, args.date2)
        # password-strength----------------------------------------------------------
        if args.password_strength==True:
            super(Script_manager, self).password_strength()
        # save db-----------------------------------------------------------------------
        if args.save_data==True:
            super(Script_manager, self).save_db()
        # delete picture----------------------------------------------------------------
        if args.delete_picture==True:
            super(Script_manager, self).delete_picture()
        # new api data--------------------------------------------------------------------
        if args.new_data !=0:
            super(Script_manager, self).save_new_db(args.new_data)



if __name__=="__main__":
    sc_manager = Script_manager()
    sc_manager.script_manager()
    
