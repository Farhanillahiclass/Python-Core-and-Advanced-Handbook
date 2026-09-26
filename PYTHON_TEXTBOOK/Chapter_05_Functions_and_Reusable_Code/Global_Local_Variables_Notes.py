# =======================================================================
#                  TOPIC: GLOBAL VS LOCAL VARIABLES
# =======================================================================

# 👶 SIMPLIFIED DEFINITIONS:
# 🌍 GLOBAL Variable = A toy placed in the Playground. EVERY child can see and play with it.
# 🏠 LOCAL Variable  = A toy kept inside YOUR ROOM. Only YOU can play with it. Outside kids don't know it exists.

# 🍕 THE 8-YEAR-OLD STORY EXAMPLE:
# Imagine you have a box of "Pizza" in the public playground (Global). Anyone can eat it.
# Now, you go inside your private Treehouse (Function) and buy a new box of "Burgers" (Local).
# People outside the treehouse still only see the Pizza. They cannot see your Burgers!

# --- CODE TEST ---

# 🌍 GLOBAL VARIABLE (Outside the box)
x = "Main bahar hoon (Global)" 


def mera_function():  # 🏠 THE TREEHOUSE (Function Boundary Starts)
    
    # 🏠 LOCAL VARIABLE (Inside the box)
    # This is a brand new 'x' built inside the treehouse.
    # It does NOT change or overwrite the global 'x' outside.
    x = "Main andar hoon (Local)" 
    
    print(x)  # 🤖 Output: "Main andar hoon (Local)"
             # Inside the treehouse, we use our local toy!

# 🏠 Boundary Ends Here!

# 🚀 TESTING THE CODE:


mera_function()  # 1. We enter the treehouse. It prints the Local 'x'.

print(x)  # 2. We are standing outside in the playground now. 
                # We can only see the Global 'x'. 
                # Output: "Main bahar hoon (Global)"

# =======================================================================
# 💡 SUMMARY FOR KIDS: 
# Variables with the SAME NAME can live together if one is INSIDE a function (Local) 
# and one is OUTSIDE a function (Global). They do not fight or overwrite each other!
# =======================================================================
