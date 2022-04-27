# value=int(input("Enter temperature: "))
# unit=input("Enter temperature unit: ")
#
# result = convert_temperature(value, unit)
# print(result)
# 1 var
value = int(input("Enter temperature: "))
unit = input("Enter temperature unit C or F : ")
convert_temp_C_to_F = value * 9 / 5 + 32
# convert_temp_C_to_F = value % 9 % 5 + 32
convert_temp_F_to_C = (value - 32) * 5 / 9
# convert_temp_F_to_C = (value - 32) % 5 % 9
if unit == 'c':
    result = convert_temp_C_to_F
    print(result)
elif unit == 'f':
    result = convert_temp_F_to_C
    print(result)


# # 2 var
# def convert_temperature(value, unit):
#
#     if unit == 'C':
#         return value * 9 / 5 + 32
#
#     elif unit == 'F':
#         return (value - 32) * 5 / 9
#
#     else:
#         raise ValueError('Invalid argument')
#
# res = convert_temperature(10, 'F')
# print(res)



