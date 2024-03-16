# functions #
def process():
	# variables #
	num = int(input("Enter the number : "))
	# end variables #

	return [num + 2 * i for i in range(num)]
# end functions #

def main():
	result = process()

	print(f"The result is : {result}")

main()
