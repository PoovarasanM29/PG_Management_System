
class Owner:
    def __init__(self):
        self.name="Aadhi"
        self.age=41
        self.phone_no=9876543219
        self.email="Aadhipg2024@gmail.com"
    def owner_license(self):
        return f'name:Aadhi\nAge:40\ncertificate no:VLR9879876\n Valid : 2030'
    def get_owner_detail(self):
        return f'name:{self.name}\nAge:{self.age}\nphone number:{self.phone_no}\nEmail :{self.email}'


own=Owner()

# print("If you want to know the Owner details..")
# want=input("Enter your wish yes or no:").lower()
# if want=="yes":
#     print(own.owner_license())
# else:
#     print("Ok..Lets Talk about further..")


