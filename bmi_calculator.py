#BMI calculator;
#Variables: h -> height | w -> weight | bmi -> int

print("Welcome to the BMI Calculator")
w = float(input("tell me your weight: "))
h = float(input("tell me yout height: "))
bmi = int(w/(h * h))
print("your BMI is:", bmi)