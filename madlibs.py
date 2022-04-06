def main():
	# write your code here
	time = input("Enter a number from 1 to 12: ")
	items = input("Enter a noun (plural): ")
	name = input("Enter a name: ").title()
	scream = input("Enter any sentance: ").upper()
	action = input("Enter a verb: ")
	print(
		f"It was {time} o'clock when I heard a knock at the door \nI opened the door and there was a box full of {items} with a note saying \"From: {name}\".\nJust as I closed the door I heard a scream '{scream}'.\nI froze in my place and all I could do was {action}."
	)



if __name__ == '__main__':
	main()