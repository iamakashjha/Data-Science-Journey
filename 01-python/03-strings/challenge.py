emails = [
    " alice@gmail.com ",
    "BOB@yahoo.com",
    "charlie@hotmail.com "
]

# Your task:

# Remove extra spaces
# Convert to lowercase
# Extract the email domain

# Expected output:

# gmail.com
# yahoo.com
# hotmail.com


for email in emails:
    # Remove extra spaces
    email = email.strip()
    
    # Convert to lowercase
    email = email.lower()
    
    # Extract the email domain
    domain = email.split('@')[1]
    
    print(domain)