
while True:
        
        t = int(input("Enter the Temperature from '0' to '50' = "))
        if((t >= 0) and (t <= 50)) :
            print()
            v = int(input("Enter the Wind Speed between '3' to '120' = "))
            if((v >= 3) and (v <= 120)):
                windChill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * pow(v, 0.16)
                print()
                print("Temperature = " , t)
                print("Wind speed  = " , v)
                print("Wind chill  = " , windChill)
                print()
            else:
                print("Enter the Valid Wind Speed")
        else:
        	print("Enter the Valid Temperature")
    