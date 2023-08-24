"""
                        🚀 Frontier Tech Leaders Programme
||||||||||||||||||||||||||||||||| ASSIGNMENT 1 ||||||||||||||||||||||||||||||||||

"""


#Calculate BMI and determine category
def calculate_bmi(weight: float, height: float):

  if weight < 0 or height < 0:
    raise Exception("weight or height cannot be a negative value")
  else:
    bmi = weight / pow(height, 2)
    """
          The 5.2f part after the colon is the format specification.
          The f denotes fixed-point notation.
          The 5 is the total width of the field being printed, lefted-padded by space.
          The 2 is the number of digits after the decimal point.

          Example: 
          x=f"{2.857142857142858:05.2f}"
          print(x)  # 02.86
         
    """
    msg = f"Your BMI is {bmi:5.2f}. You have a(n)"

    if bmi < 18.5:
      return f"{msg} Underweight"
    elif 18.5 <= bmi <= 24.9:
      return f"{msg} Normal weight"
    elif 25 <= bmi <= 29.9:
      return f"{msg} Overweight"
    return f"{msg} Obesity"



print("=========WELCOME TO BMI CALCULATOR PROGRAM==========")

#Error handling (Using <try - raise - except> )
try:
  #Get data from user
  
  """
      #Accept weight in pounds and height in inches
  weight_in_pounds = float(input("Enter your weight (lbs): "))
  height_in_inches = float(input("Enter your height (inch): "))
  #convert weight in pounds to kg and height in inches to m
  weight=weight_in_pounds/2.20462
  height=height_in_inches/39.3701
  """

  weight = float(input("Enter your weight (kg): "))
  height = float(input("Enter your height (m): "))

  if not type(weight) is float or not type(height) is float:
    raise ValueError("You must to enter a value")

  print(calculate_bmi(weight, height))
 
except ZeroDivisionError as e:
  print(f"Error => Height cannot be a zero\n{e} ")
except ValueError as e:
  print(f"Error => You must to enter a value\n({e})")
except Exception as e:
  print(f"Error => {e}")

finally:
  print("Finished...")