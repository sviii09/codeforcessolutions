n = int(input())

# Dictionary to store count of each name
name_count = {}

for _ in range(n):
    name = input().strip()
    
    # If name doesn't exist in database
    if name not in name_count:
        name_count[name] = 1
        print("OK")
    else:
        # Name exists, find the smallest number to append
        count = name_count[name]
        new_name = name + str(count)
        
        # Keep incrementing count until we find an unused name
        while new_name in name_count:
            count += 1
            new_name = name + str(count)
        
        # Update the count for the original name and add the new name
        name_count[name] = count + 1
        name_count[new_name] = 1
        print(new_name)