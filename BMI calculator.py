#BMI calculator
weight = input("Enter your weight(in kg); ")
height = input("Enter your height(in m); ")
def bmi():
	return float(weight)/(float(height)*float(height)) 
result= bmi()
print("\nYour BMI is "+ str(result))
if result > 25:
	print("You are overweight.")
elif result < 18:
	print("You are underweight.")
else:
	print("You are healthy.")