# ==========================================
# PYTHON LOGICAL OPERATORS: AND, OR, NOT
# ==========================================

# Dummy data for testing
has_admit_card = True
is_on_time = False

has_student_id = True
has_ticket = False

is_raining = True

# ------------------------------------------
# 1. TESTING 'and' OPERATOR (Both must be True)
# ------------------------------------------
print("--- Testing 'and' ---")
can_sit_in_exam = has_admit_card and is_on_time
print("Can sit in exam?", can_sit_in_exam)  # Will print False because is_on_time is False

# ------------------------------------------
# 2. TESTING 'or' OPERATOR (At least one must be True)
# ------------------------------------------
print("\n--- Testing 'or' ---")
can_enter_park = has_student_id or has_ticket
print("Can enter park?", can_enter_park)  # Will print True because has_student_id is True

# ------------------------------------------
# 3. TESTING 'not' OPERATOR (Inverts the value)
# ------------------------------------------
print("\n--- Testing 'not' ---")
print("Is it raining?", is_raining)
print("Is it a sunny day?", not is_raining)  # Will print False
