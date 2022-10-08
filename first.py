#First module
import booking as b1
list3=[]
def display_menu():
    print("MENU")
    print("1.Booking")
    print("2.Cancel ticket")
    print("3.print available tickets")
    print("4.print booked ticket")
    print()

def trainbooking():
    option=int(input("Enter your choice 1/2/3/4"))
    if option==1:
        c=b1.book()
        list3.append(c)
    
        

def main():
    display_menu()
    print("Welcome to train booking agency")
    again="y"
    while again.lower()=="y":
        trainbooking()
        again=input("Again want to book(y/n")
        print()
    print("Bye")

if __name__=="__main__":
    main()
    
        
