"""
Please implement these stub functions to match the documentation.
"""

def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements. If any requirements
    are not met, prints which requirements were not met.

    Requirements:
    1. Password must be at least 8 characters long
    2. Must contain at least one uppercase letter
    3. Must contain at least one lowercase letter
    4. Must contain at least one digit
    5. Must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """
    pass

def main() -> None:
    """
    1. Ask the user to input a password
    2. If it is not valid, print the requirements which are not met, and go back to step 1.
    3. If it is valid, print "Valid password!"
    """
    pass

if __name__ == '__main__':
    main()
