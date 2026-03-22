import re

def redact_pii(text):
    # 1. Redact Email addresses
    text = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[EMAIL_REDACTED]', text)
    
    # 2. Redact Singapore phone numbers (8 or 9 followed by 7 digits)
    text = re.sub(r'\b[89]\d{7}\b', '[PHONE_REDACTED]', text)
    
    return text

# Test it out
user_input = "Hello, my email is john.doe@example.com and my number is 91234567."
print("Original:", user_input)
print("Safe Version:", redact_pii(user_input))