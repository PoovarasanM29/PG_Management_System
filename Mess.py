
class Mess:
    def food_menu(self):
        print("\n1.Idly\n2.Dosa\n3.Chappathi\n4.Rice with Sambar/Rasam/Curd\n5.Briyani\n6.Lemon Rice\n7.TomatoRice\n8.Parotta\n9.Veg Briyani\n10.Fruit/Veg Salad")
    def feed_back(self):
        feed=input("Express your Feedback:")
        return f'{feed} \n\n Thank you for Valuable Feedback'
    def get_chef_detail(self):
        self.chef_name="Parvathy"
        self.chef_age=38
        self.chef_spouse="Venkatesan"
        self.chef_phone_number=8796543218
        self.chef_license="CHef1001567"
        return f'Name:{self.chef_name} \nAge:{self.chef_age}\nSpouse:{self.chef_spouse}\nPhone number:{self.chef_phone_number}\nLicense:{self.chef_license}'

m=Mess() #object Creation






