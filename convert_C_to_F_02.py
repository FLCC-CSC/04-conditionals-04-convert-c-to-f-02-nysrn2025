# FILE NAME - convert_C_to_F_02.py

# NAME: KEVIN LEE 
# DATE: 10/8/2025
# BRIEF DESCRIPTION: This program converts temperatures between Celsius and Fahrenheit based on user selection
  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Display menu header
print("===== Temperature Converter =====")
print()

# Display menu options
print("  1. Convert from Celsius to Fahrenheit")
print("  2. Convert from Fahrenheit to Celsius")
print()

# Get user's menu choice
choice = input("Please choose from the above menu: ")

# Get temperature to convert
temperature = float(input("Enter a temperature to convert: "))
print()

# Perform conversion based on user choice
if choice == "1":
    # Convert Celsius to Fahrenheit
    fahrenheit = temperature * 9/5 + 32
    print(f"{temperature} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
elif choice == "2":
    # Convert Fahrenheit to Celsius
    celsius = (temperature - 32) * 5/9
    print(f"{temperature} degrees Fahrenheit is {celsius} degrees Celsius.")








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

One important lesson I learned was how to create user-friendly menu systems that guide 
the user through multiple steps. This lab taught me how to structure programs with 
clear input prompts, handle different conversion paths using conditional statements, 
and ensure the output format matches exactly what's expected.






'''