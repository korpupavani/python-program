"""
looping statements are also called asiterative
statements

thse statements are uused to run a particular
condition
no.of times....dived into"2"types
1.while
2.for
"""

#while:it executes when the condition is true 
"""
 syntax:while condition:
       statements
       exit condition/incrementation
       
#eg:
i=1
while i<=10:
    #print(i---->in this particular line the )
    # "i" value  runs "in" times becuase no
incrementation?exit and specified
  print("the value",i)
   i+=1
    
#eg-2:
 #while true:
     #print("the while condition)
 #note:as default flase is given as condition it wont
 excute
    
#eg:3
# while false:
  #print("the while condition")
#as while is also called entry control
# loop it just checks the condition in the entrance
# as default false is given as condition it wont
execute
"""
i=0
while i<=0:
    i+=1
    if i==6:
        break#terminates/stops the program
    print(i)

i=0
while i<9:
  i+=1
  if i==3:
    continue
  print(i)  