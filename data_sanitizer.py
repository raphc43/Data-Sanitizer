def data(arg):
	'''Function that takes an input,
	sanitize or trims the repeated data 
	and return it as a unique one'''

	# Takes a file and stores it in a variable beforing closing
	with open(arg) as file:
		data_list = file.readlines()

	# For loop to replace '\n' in list items.
	''' This procedure was written because because last
	item was kept ignored due to absence of newline character '''
	new_data = []
	for d in data_list:
		if '\n' in d:
			new_data.append(d.replace('\n', '')) 

	# For loop to append those items which didn't have \n.
	for d in data_list:
		if '\n' not in d:
			new_data.append(d) 

	# A for loop mechanism to remove empty list items.
	while '' in new_data:
		new_data.remove('')
			 
	# Assigning a unique list to a new variable
	unique_data_list = set(new_data)
	
	print("Unique items: ")

	# Runs a for loop to print unique values
	if unique_data_list:
		for u in unique_data_list:
			print(u)
	
	else:
		print("None")


	# Statistics
	print("\n---------- STATS ----------")

	if new_data:
		print(f"Total items: {len(new_data)}")

		trimmed = len(new_data) - len(unique_data_list)
		print(f"Trimmed items: {trimmed} or {int(trimmed * 100 / len(new_data))}%")
		print(f"Remaining items: {len(unique_data_list)} or "
			f"{int(len(unique_data_list) * 100 / len(new_data))}%")
	else:
		print("Total items: 0")
		print("Trimmed items: 0")
		print("Remaining items: 0")

data('emails.txt')