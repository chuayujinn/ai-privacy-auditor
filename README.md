# AI Privacy Auditor

A lightweight, local PII redaction layer for text destined for an LLM — built around the Singapore data protection context.

---

## The problem

Once text is sent to a cloud-based LLM, any personal data it contains is effectively out of your control — it can't reliably be "un-sent" or deleted from logs, caches, or training pipelines. A growing share of AI-related privacy incidents stem from exactly this: someone pastes a document, email, or set of notes containing personal data directly into a chat interface.

## What this does

This tool sits **before** the LLM call. It scans input text locally and redacts common categories of personal and sensitive data:

- **Singapore NRIC/FIN numbers** (e.g. `S1234567A`)
- **Singapore mobile numbers** (8-digit numbers starting with 8 or 9)
- **Email addresses**
- **Configurable sensitive terms** (e.g. medical conditions, medications — fully editable)

The redacted output is what gets sent onward — the original text never leaves the local environment.

This is a small, deliberately simple example of a **privacy-by-design technical control**: the kind of lightweight guardrail referenced under technical control requirements in frameworks like IMDA's Model AI Governance Framework for agentic AI systems, where organisations are expected to demonstrate that personal data exposure to AI systems is actively minimised.

---

## Project structure

```
.
├── app.py             # Streamlit interface
├── privacy_guard.py   # Core redaction logic (regex-based)
└── requirements.txt
```

---

## Usage

```bash
pip install -r requirements.txt
streamlit run app.py
```

Paste or type text into the input box, optionally edit the list of sensitive terms, and click **Redact** to see the output that would be safe to forward to an LLM.

### Using the redaction logic directly

```python
from privacy_guard import redact_pii

text = "Call me at 91234567 or email john@example.com. NRIC: S1234567A."
print(redact_pii(text))
# "Call me at [PHONE_REDACTED] or email [EMAIL_REDACTED]. NRIC: [ID_REDACTED]."
```

---

## Limitations

This is a proof-of-concept, not a production data loss prevention (DLP) tool. In particular:

- Detection is **regex-based** — it will miss PII that doesn't match these specific patterns (other countries' ID formats, names, addresses, free-text descriptions of identifiable individuals, etc.)
- NRIC/FIN regex matches the *format* (letter + 7 digits + letter) but does not validate the checksum, so it may also match non-NRIC strings that happen to fit the pattern
- No handling of PII embedded in structured data (tables, JSON, code blocks) beyond plain text matching
- Sensitive terms list is a simple substring match — not context-aware

For production use cases, this kind of pattern-matching layer would typically be one part of a broader DLP strategy, alongside context-aware NLP-based PII detection (e.g. Microsoft Presidio, AWS Comprehend PII detection) and policy controls at the application/infrastructure level.

---

## License

MIT
