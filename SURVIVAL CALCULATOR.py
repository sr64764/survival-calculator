
def survival():

    age=int(input('Enter Your age: '))
    print("Note: You can write the first letter or the full name of the time unit.")
    print('''
            Options you can Excercise are:
            months
            weeks
            days
            hours
            minutes
            seconds
         ''')
    option= str(input("enter your option: "))
    option= option.lower()
    
    if option=="months" or option=="M":
        mon=age*12
        print("you lived for {0} months.".format(mon))
    elif option=="weeks" or option=="w":
        week=age*52.1429
        print("you lived for {0} weeks.".format(week))
    elif option=="days" or option=="d":
        day=age*365
        print("you lived for {0} days.".format(day))        
    elif option=="hours" or option=="h":
        hou=age*8760
        print("you lived for {0} hours.".format(hou))  
    elif option=="minutes" or option=="m":
        miu=age*525600
        print("you lived for {0} minutes.".format(miu))          
    elif option=="seconds" or option=="s":
        sec=age*31536000
        print("you lived for {0} seconds.".format(sec))          
    else:
        print("invalid option")
    return



if __name__ == "__main__":

    survival()

