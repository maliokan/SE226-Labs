num = int(input("Give time by seconds: "))
hours = num//3600
minutes = (num - hours*3600)//60
sec = (num - hours*3600 - minutes*60)
print(str(num) + " seconds is " + str(hours) +" hours ," + str(minutes) +" minutes, and " + str(sec) +" seconds.")
