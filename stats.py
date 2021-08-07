def show_stats(new_data, unique_data_list):
	'''Function to calculate and
	show statistics'''
	
	print("\n---------- STATS ----------")

	if new_data:
		print(f"Total items: {len(new_data)}")

		trimmed_content = len(new_data) - len(unique_data_list)

		# Calculates trimmed items in numbers and in percentage.
		print(f"Trimmed items: {trimmed_content} or "
			f"{int(trimmed_content * 100 / len(new_data))}%")

		# Calculates trimmed items in numbers and in percentage.
		print(f"Remaining items: {len(unique_data_list)} or "
			f"{int(len(unique_data_list) * 100 / len(new_data))}%")
	else:
		print("Total items: 0")
		print("Trimmed items: 0")
		print("Remaining items: 0")

	return 