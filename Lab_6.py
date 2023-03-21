# Chloe Sawatzki


# Function to prompt the user for their desired operation
def menu():
	print("Menu", "---------------", "1. Encode", 
		  "2. Decode", "3. Quit", sep="\n")

# Function to encode an 8-digit password
def encoder(password):
	newpass = ''
	for i in password:
		newpass += str(int(i)+3)
	return newpass


# The main function
def main():
	selection = 0
	while selection != 3:  # Will continue the program until the user exits
		menu()
		print()
		selection = int(input("Please enter an option: "))

		# Asks for a user inputed password to then encode
		if selection == 1:
			password = input("Please enter your password to encode: ")
			print("Your password has been encoded and stored!")
			encoded = encoder(password)

		elif selection == 2:
			pass

		print()


if __name__ == "__main__":
	main()