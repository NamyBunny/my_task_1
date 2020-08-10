from main import Save_data_base
from script import My_functions

# nie działa po uruchomięciu new_users_from_api.py
class TestClass():
    ex=My_functions()
    def test_averag_age(self):
        assert self.ex.averag_age('male')==('Average age of men is '+'48.7'+' years')
        assert self.ex.averag_age('female')==('Average age of women is '+'49.5'+' years')
        assert self.ex.averag_age('middle')==('Average age of all people is '+'49.1'+' years')
        assert self.ex.averag_age('all')==('Average age of women is '+'49.5'+' years \n\t Average age of men is '
            +'48.7'+' years \n\t Average age of all people is '+'49.1'+' years')
    def test_percentage_of_women_and_men(self):
        assert self.ex.percentage_of_women_and_men('male')=='Percentage of men is '+'50.2'+' %'
        assert self.ex.percentage_of_women_and_men('female')=='Percentage of women is '+'49.8'+' %'
    def test_most_popular_cities(self):
        assert self.ex.most_popular_cities(1)==['Gisborne was found in the database 7 times. Is this the most popular city?']
        assert self.ex.most_popular_cities(2)==['Gisborne was found in the database 7 times. Is this the most popular city?','Lower Hutt was found in the database 5 times']
        
    def test_most_popular_passwords(self):
        assert self.ex.most_popular_passwords(1)==['"surf" was found in the database 3 times. Is this the most popular password?']
        assert self.ex.most_popular_passwords(5)==['"surf" was found in the database 3 times. Is this the most popular password?',
                                                    '"achtung" was found in the database 3 times',
                                                    '"thrasher" was found in the database 2 times',
                                                    '"jethro" was found in the database 2 times',
                                                    '"review" was found in the database 2 times']
    def test_born_in_between_dates(self):
        assert self.ex.born_in_between_dates('1998-08-29', 'January 12, 2012 10:00 PM')==['Miss Marilce Alves was born in 1998-08-29',
                                                                                                'Ms Allie Hunter was born in 1998-09-09']
    def password_strength(self):
        assert self.ex.password_strength()=='''The strongest password is "('apollo13', 7)".'''


    