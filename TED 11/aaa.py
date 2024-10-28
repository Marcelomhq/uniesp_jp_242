# def receive_numbers():
#     lst = []
#     for _ in range(10):
#         # Step 1: Take input number
#         number = int(input("Enter a number: "))

#         # Step 2: Check for duplicates and get their indices
#         indices = [i for i, x in enumerate(lst) if x == number]

#         # Step 3: Append offset of len(lst) if number is a duplicate
#         if indices:
#             indices_with_offset = indices + [len(lst)]
#             print(f"Number {number} already exists. Indices of occurrences (including new index): {indices_with_offset}")
#         else:
#             print(f"Number {number} is unique and will be added.")

#         # Step 4: Add the number to the list regardless of duplicates
#         lst.append(number)
    
#     # Optional: Return the final list
#     return lst

# # Call the function to start receiving numbers
# final_list = receive_numbers()
# print("Final list of numbers:", final_list)

def receive_numbers():
    VET = []
    duplicate_indices = set()  # To store indices of duplicates without repeats

    # Collect 10 numbers from the user
    for _ in range(10):
        number = int(input("Enter a number: "))
        
        if number in VET:
            # Find indices of all occurrences of `number` in the list
            for i, x in enumerate(VET):
                if x == number:
                    duplicate_indices.add(i)  # Add index of existing occurrence
            # Add index where `number` will be appended
            duplicate_indices.add(len(VET))
        # Add the number to the list
        VET.append(number)

    # Print all duplicate indices at the end
    print("Indices of repeated numbers:", sorted(duplicate_indices))

# Run the function to start receiving numbers
receive_numbers()