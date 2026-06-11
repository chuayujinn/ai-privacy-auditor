"""
privacy_guard.py

Core PII detection and redaction logic for the AI Privacy Auditor.

Provides regex-based redaction for common Singapore-context identifiers
(NRIC/FIN, local phone numbers), email addresses, and a configurable list
of sensitive terms (e.g. medical conditions or medications) that should
not be sent to a cloud-based LLM.

This is a local, deterministic pre-processing layer intended to sit between
a user and an AI agent — redaction happens before any text leaves the
local environment.
"""

import re

# --- Patterns -----------------------------------------------------------

EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

# Singapore mobile numbers: 8 digits starting with 8 or 9
SG_PHONE_PATTERN = re.compile(r'\b[89]\d{7}\b')

# Singapore NRIC/FIN: leading letter (S/T/F/G/M), 7 digits, trailing letter
NRIC_PATTERN = re.compile(r'\b[STFGMstfgm]\d{7}[A-Za-z]\b')

# Default list of sensitive terms (medical conditions, medications, etc.)
# Extend or replace this list as needed for your context.
DEFAULT_SENSITIVE_TERMS = [
    "Atenolol",
    "Insulin",
    "Cancer",
    "HIV",
]


# --- Redaction functions -------------------------------------------------

def redact_email(text: str) -> str:
    """Redact email addresses."""
    return EMAIL_PATTERN.sub("[EMAIL_REDACTED]", text)


def redact_sg_phone(text: str) -> str:
    """Redact Singapore mobile numbers (8 digits, starting 8 or 9)."""
    return SG_PHONE_PATTERN.sub("[PHONE_REDACTED]", text)


def redact_nric(text: str) -> str:
    """Redact Singapore NRIC/FIN numbers (e.g. S1234567A)."""
    return NRIC_PATTERN.sub("[ID_REDACTED]", text)


def redact_sensitive_terms(text: str, terms: list[str] | None = None) -> str:
    """
    Redact a configurable list of sensitive terms (case-insensitive).

    Args:
        text: The input text to scan.
        terms: Optional list of terms to redact. Defaults to
               DEFAULT_SENSITIVE_TERMS if not provided.
    """
    terms = terms if terms is not None else DEFAULT_SENSITIVE_TERMS
    for term in terms:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        text = pattern.sub("[SENSITIVE_TERM_REDACTED]", text)
    return text


def redact_pii(text: str, sensitive_terms: list[str] | None = None) -> str:
    """
    Apply all redaction layers to the input text, in order:
    NRIC/FIN -> email -> SG phone numbers -> sensitive terms.

    Args:
        text: The input text to scan.
        sensitive_terms: Optional custom list of sensitive terms.

    Returns:
        The redacted text, safe to forward to an LLM.
    """
    text = redact_nric(text)
    text = redact_email(text)
    text = redact_sg_phone(text)
    text = redact_sensitive_terms(text, sensitive_terms)
    return text


if __name__ == "__main__":
    # Quick manual test
    sample = (
        "Hello, my email is john.doe@example.com and my number is 91234567. "
        "Patient S9876543Z was prescribed 50mg of Atenolol."
    )
    print("Original:   ", sample)
    print("Redacted:   ", redact_pii(sample))
