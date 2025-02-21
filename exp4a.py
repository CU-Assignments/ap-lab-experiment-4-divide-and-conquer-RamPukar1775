while True:
   binary_str = input("Enter a 32-bit binary number: ")
   if len(binary_str)==32:
       break
   else:
       print("Invalid input")
reversed_binary_str = binary_str[::-1]

decimal_value = int(reversed_binary_str, 2)

print(f"Reversed Binary: {reversed_binary_str}")
print(f"Decimal Value: {decimal_value}")
