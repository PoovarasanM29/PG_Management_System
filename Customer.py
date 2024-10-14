class Customer:
    def __init__(self,name,Age,phone_no,email,location):
        self.name=name
        self.Age = Age
        self.phone_no =phone_no
        self.Email= email
        self.location=location

    def get_user_detail(self):
        return f'name:{self.name}\nAge:{self.Age}\nphone number:{self.phone_no}\nEmail :{self.Email}\nNative Location:{self.location}'



cus=Customer('chella',55,329047836,'chellamuthu2024@gmail.com','Vellore')








