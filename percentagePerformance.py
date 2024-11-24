a = float(input("Enter your Percentage : "))
if a > 100 :
    print("Enter a valid percentage...!")
elif a >= 90 :
    print("EXCELLENT PERFORMANCE!")
elif a >= 80 :
    print("VERY GOOD PERFORMANCE!")
elif a >= 70 :
    print("GOOD PERFORMANCE!")
elif a >= 60 :
    print("AVERAGE PERFORMANCE!")
else:
    print("POOR PERFORMANCE...!")