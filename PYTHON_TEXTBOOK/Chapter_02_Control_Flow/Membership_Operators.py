# ==========================================
# PYTHON MEMBERSHIP OPERATORS: IN & NOT IN
# ==========================================

# Variables
search_x = 10
search_y = 5
numbers_list = [1, 2, 3, 4, 5, 6]

print("--- Testing 'in' Operator ---")
# Checks if 10 is inside the list
if search_x in numbers_list:
    print(f"{search_x} is available in the list.")
else:
    print(f"{search_x} is NOT available in the list.")

print("\n--- Testing 'not in' Operator ---")
# Checks if 5 is absent from the list
if search_y not in numbers_list:
    print(f"{search_y} is NOT available in the list.")
else:
    print(f"{search_y} is available in the list.")

