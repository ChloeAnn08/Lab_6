#8-Digit Encoder

def menu():
	print("Menu", "---------------", "1. Encode", 
		  "2. Decode", "3.Quit", sep="\n")

def encoder(password):
	new = ''
	for i in password:
		new += str(int(i)+3)
	return new

def main():
	selection = 0
	while selection != 3:
		menu()
		selection = int(input("Please enter an option: "))

		if selection == 1:
			password = input("Please enter your password to encode: ")
			print("Your password has been encoded and stored!")
			print(encoder(password))

		#elif selection == 2:
			#decode(password)

		elif selection == 3: 
			break


if __name__ == "__main__":
	main()