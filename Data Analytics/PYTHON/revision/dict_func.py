#1)setdefault
student={"name":"John","class":"6th","roll_no":23}

#Scenario A: The key already exists (It just returns the existing value and does nothing to the dictionary).
# Looking for 'name', which already exists
val = student.setdefault("name", "Unknown")
print(val)      # Output: John
print(student)  # Output: {"name": "John", "class": "6th", "roll_no": 23} (Unchanged)

#Scenario B: The key does NOT exist (It adds the key-value pair to the dictionary).
# Looking for 'section', which doesn't exist
val = student.setdefault("section", "A")
print(val)      # Output: A
print(student)  # Output: {"name": "John", "class": "6th", "roll_no": 23, "section": "A"}

#__________________________________________________________________________

#2)update
student = {"name": "John", "class": "6th", "roll_no": 23}

# Update existing 'class' and add a new 'marks' key
student.update({"class": "7th", "marks": 85})
print(student)  
# Output: {'name': 'John', 'class': '7th', 'roll_no': 23, 'marks': 85}

#________________________________________________________________________

#3)pop
student = {"name": "John", "class": "6th", "roll_no": 23}

#Scenario A: Removing an existing key
removed_value = student.pop("roll_no")
print(removed_value) # Output: 23
print(student)       # Output: {'name': 'John', 'class': '6th'}

#Scenario B: Safely removing a missing key with a default value
# 'age' doesn't exist, but providing a default prevents an error
removed_value = student.pop("age", "Not Found")
print(removed_value) # Output: Not Found

#__________________________________________________________________

#4)popitem
student = {"name": "John", "class": "6th", "roll_no": 23}

last_item = student.popitem()
print(last_item) # Output: ('roll_no', 23)
print(student)   # Output: {'name': 'John', 'class': '6th'}

#___________________________________________________

#5)clear
student = {"name": "John", "class": "6th", "roll_no": 23}

student.clear()
print(student) # Output: {}

#______________________________________________________