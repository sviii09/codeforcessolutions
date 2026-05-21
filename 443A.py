# Read the input line
line = input().strip()

# Remove the curly braces
content = line[1:-1]

# If the content is empty, there are no letters
if not content:
    print(0)
else:
    # Split by comma and space
    letters = content.split(", ")
    
    # Convert to set to get unique letters
    unique_letters = set(letters)
    
    # Print the count
    print(len(unique_letters))