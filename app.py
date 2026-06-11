"""
app.py

Streamlit interface for the AI Privacy Auditor — a local PII redaction
layer for text destined for an LLM.

Run with:
    streamlit run app.py
"""

import streamlit as st
from privacy_guard import redact_pii, DEFAULT_SENSITIVE_TERMS

st.set_page_config(page_title="AI Privacy Auditor", page_icon="🛡️")

st.title("🛡️ AI Privacy Auditor")
st.write(
    "Paste text below to see it redacted **locally**, before it would be "
    "sent to a cloud-based AI. Detects Singapore NRIC/FIN numbers, phone "
    "numbers, email addresses, and configurable sensitive terms."
)

with st.expander("Sensitive terms list (editable)"):
    terms_input = st.text_area(
        "One term per line",
        value="\n".join(DEFAULT_SENSITIVE_TERMS),
        height=120,
    )
    custom_terms = [t.strip() for t in terms_input.splitlines() if t.strip()]

default_text = (
    "Hi, I'm John (NRIC S9876543Z). You can reach me at 91234567 or "
    "john.doe@example.com. Patient was prescribed 50mg of Atenolol."
)

user_input = st.text_area("Input text:", value=default_text, height=120)

if st.button("Redact"):
    safe_text = redact_pii(user_input, sensitive_terms=custom_terms)

    st.subheader("Redacted output (safe to send to an LLM):")
    st.code(safe_text)

    if safe_text == user_input:
        st.info("No PII patterns matched — nothing was redacted.")
    else:
        st.success("Redaction applied. Review before sending downstream.")
