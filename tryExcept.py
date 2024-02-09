#Example 1

# fav_num = input("What is your favourite number? > ")

# try:
#     number = int(fav_num)    
# except:
#     print("This is not a number")
# else:
#     print(number)
# finally:
#     print("The Try Except block is now finished.")

#Example 2
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except ValueError:
    print("Not a number.")
except:
    print("Something went wrong.")
else:
    print("eswfwsef")