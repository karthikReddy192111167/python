#To find season

def findseason (M) :
    list1 = [[12 , 1 , 2], [3 , 4 , 5], [6 , 7 , 8], [9 , 10 , 11]]
    if M in list1[0] :
	    print ( "WINTER" )
    elif M in list1[1] :
	    print ( "SUMMER" )
    elif M in list1[2] :
	    print ( "SPRING" )
    elif M in list1[3] :
	    print ( "AUTUMN" )
    else :
	    print ( "Invalid Month Number" )
M = int(input('Enter the month number to find season:'))
print("For Month:", M);
findseason ( M )

