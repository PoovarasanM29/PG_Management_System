#import all the respective modulus
from Customer import Customer
from Mess import Mess
from Owner import Owner
from Rooms import Room


def main():   #main Function
    print("1.Get user detail\n2.Get Owner Details\n3.Room Details\n4.Food Menu\n5.Owner License\n6.Chef License")#options

    A1 = Customer('Saravanan', 21, 9876543219, 'saravananchellamuthu@gmail.com', 'Vellore') #object for Customer
    A2 = Owner() #object for owner
    A3 = Room()  #object for room
    A4 = Mess()  #object for mess
    while True:
        choice=int(input("Enter your choice:"))
        match(choice):
            case 1:
                print("Your Details")
                print(A1.get_user_detail()) #calling the function to get user details
            case 2:
                print(A2.get_owner_detail())   #calling the function to get owner details
            case 3:
                print(A3.get_PG_facility())  #calling the function to get PG details
            case 4:

                print("choices are listed below..👇\n1.Food Menu\n2.Exit")
                choices = int(input("Enter Your choice:"))
                match (choices):
                    case 1:
                        print(A4.food_menu())  #calling the function for food menu
                        select = int(input("select your food :"))
                        match (select):
                            case 1:
                                print("Taste your Idly... ")
                            case 2:
                                print("Taste your Dosa... ")
                            case 3:
                                print("Taste your Chappathi... ")
                            case 4:
                                print("Taste your Rice with Sambar/Rasam/Curd ... ")
                            case 5:
                                print("Taste your Briyani ... ")
                            case 6:
                                print("Taste your Lemon rice ,Cool Your as like as Ice... ")
                            case 7:
                                print("Taste your Tomato Rice ... ")
                            case 8:
                                print("Taste your Parotta... ")
                            case 9:
                                print("Taste your Veg Briyani... ")
                            case 10:
                                print("Taste your Fruit/Veg Salad... ")
                        print(A4.feed_back()) #calling the feed back function to express valuable customer feedback

                    case 2:
                        print("Customer Leaving.... or Customer not visited...")


            case 5:
                print(A2.owner_license()) # calling the owner license detail function
            case 6:
                print(A4.get_chef_detail())  # calling the chef detail function
        quit=input("If you want to quit PRESS Q or q:").lower()
        if quit == 'q': #conditon is true then break the loop
            break
        else:
            continue # condition is false then continue the program
if __name__=="__main__":
    main() #calling main function





