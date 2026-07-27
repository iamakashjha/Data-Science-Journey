def clean_name(name):
    """Cleans a name string by stripping whitespace and capitalizing it."""
    return name.strip().title()

def clean_email(email):
    """Cleans an email string by stripping whitespace and converting it to lowercase."""
    return email.strip().lower()