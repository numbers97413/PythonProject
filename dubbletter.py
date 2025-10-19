def find_duplicates():
    # Get input from user
    user_input = input("Enter numbers separated by spaces: ")

    # Convert input string to list of integers
    try:
        numbers = [int(num) for num in user_input.split()]

        # Check for duplicates using a dictionary
        count_dict = {}
        duplicates = []

        # Count occurrences of each number
        for num in numbers:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] == 2:  # Add to duplicates when count reaches 2
                duplicates.append(num)

        if not duplicates:
            print("No duplicates found!")
        else:
            print(f"Duplicates found: {duplicates}")

        return numbers, duplicates

    except ValueError:
        print("Error: Please enter valid integers separated by spaces")
        return [], []


# Run the function
if __name__ == "__main__":
    numbers, duplicates = find_duplicates()
    if numbers:
        print(f"Original list: {numbers}")