#Goals-against average, or GAA, is the number of goals allowed per 60 minutes played, rounded to two decimal points.

#The formula for calculating this statistic consists of multiplying the number of goals allowed by 60 and divide by the total number of minutes played.

#funtion for GAA

def function():
  name = str(input("Enter name of goalie: ")) # input for name and for goals per period
  
  period1 = int(input("Enter total number of goals this season that were scored for period 1: "))
  
  period2 = int(input("Enter total number of goals scored this season that were for period 2: "))
  
  period3 = int(input("Enter total number of goals scored this season that were for period 3: "))
  
  games = int(input("Enter total games played: "))
  print('\n')

  minutesPlayed = games * 60 # number of games played will be times by 60 min per game
  
  periodMinutes = games * 20 # one period is 20 min so for period average it is multiplied by 20
  
  # Calculate the average
  average = (period1 + period2 + period3) / minutesPlayed * (60) # formula for GAA total 
  
  # GAA for each period below
  averagePeriod1 = (period1 / periodMinutes) * 20
  averagePeriod2 = (period2 / periodMinutes) * 20
  averagePeriod3 = (period3 / periodMinutes) * 20
  
  # print out for each period and total GAA for goalie
  print ("Your Goals Against Average for period 1 is: ", round(averagePeriod1, 3), "\n")
  
  print ("Your Goals Against Average for period 2 is: ", round(averagePeriod2, 3), "\n")
  
  print ("Your Goals Against Average for period 3 is: ", round(averagePeriod3, 3), "\n")

  # Print out the total GAA
  print ("Your Goals Against Average for the year is: ", round(average, 3), "\n")
  
  # determine how the goalie did
  if average <= 2:
    print("Goalie " + name +  " you had a GREAT YEAR and should be an ALLSTAR\n")
  if average > 2 and average <= 6 :
    print("Goalie " +name + " you did GOOD, but NOT an ALLSTAR, better luck next year\n")
  if average > 6:
    print("Goalie " + name + " played HORRIBLE. Coach you should have BENCHED this goalie and put in the BACKUP \n")

  # determine if user wants to continue
  while True:
    again = input("Thank you for using this GAA calculator, would you like to try again? \n Please type \"y\" for yes or \"n\" for no: ")
    if again not in {"y","n"}:
      print("please enter valid input\n")
    elif again == "n":
      print( "Thank you for checking the Goal Against Average")
      break
    elif again == "y":
      return function() #returns to begining of program 
function()