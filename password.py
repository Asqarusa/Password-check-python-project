import re

def check_password_strength(password):
    """Checks the strength of a password."""
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
    
    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")
    
    # Evaluate strength
    if strength == 4:
        return "Strong", feedback
    elif strength == 3:
        return "Medium", feedback
    else:
        return "Weak", feedback


# Main function
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
