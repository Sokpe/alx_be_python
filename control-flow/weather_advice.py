weather= input("Whats the weather like today? (sunny, rainy, cold): ").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather =="rainy":
    print("Dont forget your umbrella and wear a raincoat.") 

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry i dont have recommendations for this weather")