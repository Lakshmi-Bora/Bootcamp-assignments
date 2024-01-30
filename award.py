# Request the user to enter the time taken for swimming, cycling and running seperately,

swimming_time = float (input ("Please enter the time taken for swimming in minutes :   "))
cycling_time = float (input ("Please enter the time taken for cycling in minutes:   "))
running_time = float (input ("Please enter the time taken for running in minutes :   "))
print()

#Create a variable to store whether the event is cpmpleted by the participant or not.
event_finished = False

if swimming_time > 0 and cycling_time > 0 and running_time > 0:
    
    event_finished = True

#If all the events were finished, calculate the total time taken and check it with the qualifying time.
# and print the awards out according to the given score limits.
#Else print the related output statement.

if event_finished:
    
    total_time = swimming_time + cycling_time + running_time
    print (f"The total time taken to finish the triathlon is {total_time} minutes")

    if total_time <=100:
        
        print ("Congrats! The participant has been qualified for Provincial Colours.")

    elif total_time <= 105:
        
        print ("Congrats! The participant has been qualified for Provincial Half Colours.")

    elif total_time <=110:
       
        print("Congrats! The participant is qualified for Provincial Scroll.")
  
    else:
       
        print ("Sorry, The participant has not been qualified for any award!")

else:
    
    print ("Sorry, all the events of triathlon should be completed to qualify")
