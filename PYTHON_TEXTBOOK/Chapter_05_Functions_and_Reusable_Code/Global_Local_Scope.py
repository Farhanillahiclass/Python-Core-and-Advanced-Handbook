# ==========================================
# PYTHON VARIABLE SCOPE: GLOBAL VS LOCAL
# ==========================================

# 1. GLOBAL VARIABLE DEFINITION
# This lives in the main script body and can be accessed anywhere.
pizza = "Main bahar hoon (Global)"


def mera_function():
    # 2. LOCAL VARIABLE DEFINITION
    # This lives strictly inside the function boundary.
    toy = "Main andar hoon (Local)"
    
    print("--- Inside Function Execution ---")
    print("Local access:", toy)
    print("Global access from inside:", pizza)


def show_same_name_handling():
    # 3. IDENTICAL NAMES HANDLING
    # Python treats these as entirely separate variables.
    pizza = "This is a Local Variable with a Global Name"
    
    print("\n--- Testing Same-Name Shadowing ---")
    print("Inside function (local priority):", pizza)


# ==========================================
# EXECUTION / TESTING THE CODE
# ==========================================
if __name__ == "__main__":
    # Run the basic scope function
    mera_function()
    
    print("\n--- Outside Function Execution ---")
    print("Global access from outside:", pizza)
    
    # Attempting to print 'toy' here would cause a NameError:
    # print(toy) 

    # Run the shadowing demonstration
    show_same_name_handling()
    print("Outside function after shadowing test:", pizza)
