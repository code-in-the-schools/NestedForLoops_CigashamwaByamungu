#I dont know where to Start  

#Outer Loop
for i in range (0,6):
  print("Outer Loop | i = " + str(i) )

  #Inner Loop
  for j in range (0, 6):


    #They must both be even  
    if (i%2) == 0 and (j%2) == 0:
      print("Both even")

    #They must both be odd
    if (i%3) == 0 and (j%3) == 0:
      print("Both odd")
    


    print("inner loop | i = " + str(i) + " | j = " + str(j))


#Original Verison^^^^^^^Experiement Below

