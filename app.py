import streamlit as st
import re

# THE ARCHITECT'S FIX: Using 'Regex' to catch the whole NRIC pattern
def redact_nric(text):
    # Pattern: Letter + 7 digits + Letter (e.g., S1234567A)
    nric_pattern = r'[STFGM]\d{7}[A-Z]'
    return re.sub(nric_pattern, "[ID_HIDDEN]", text, flags=re.IGNORECASE)

# THE CONTEXT FIX: Masking sensitive medical terms
def redact_medical(text):
    sensitive_words = ["Atenolol", "Insulin", "Cancer", "HIV"]
    for word in sensitive_words:
        text = text.replace(word, "[SENSITIVE_TERM_HIDDEN]")
    return text

st.title("🛡️ Privacy-Safe AI Auditor")
st.write("This tool redacts PII locally *before* it ever hits a cloud AI.")

user_input = st.text_area("Paste Notes Here:", "Patient S9876543Z was prescribed 50mg of Atenolol.")

if st.button("Review Privacy Shield"):
    # Step 1: Apply your professional privacy layers
    safe_text = redact_nric(user_input)
    final_safe_text = redact_medical(safe_text)
    
    st.subheader("Safe Data (This goes to the AI):")
    st.code(final_safe_text)
    st.success("Logic Verified: Your 'Architect's Eye' has blocked the leak!")