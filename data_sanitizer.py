from stats import show_stats

def trim_data(arg):
	'''Function that takes an input,
	sanitize or trims the repeated data 
	and return it as a unique one'''

	# Takes a txt file and stores it in a variable beforing closing
	with open(arg) as file:
		data_list = file.readlines()

	# For loop to replace '\n' in list items.
	# This procedure was written because last item was kept 
	# ignored by sets due to absence of newline character
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

	# Checks whether list has data or not.
	if unique_data_list:
		# Prints the unique data
		for u in unique_data_list:
			print(u)
	
	else:
		print("None")

	# Shows statistics
	show_stats(new_data, unique_data_list)

trim_data('emails.txt')
