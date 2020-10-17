#Temperature Converter
#Pratik Prabhakar 117220752, Sept 27 2017

temp_c = float(input("Please enter the temperature in Celsius."))
temp_f = temp_c*9/5+32
temp_r = (4 / 5) * temp_c  #convert celcius to reamur
temp_K = 273 + temp_c  #convert celcius to Kelvin

print("Faranheit equivalent temperature is: ", temp_f,"F")
print("Reamur equivalent temperature is: ", temp_r,"R")
print("Kelvin equivalent temperature is: ", temp_K,"K")
