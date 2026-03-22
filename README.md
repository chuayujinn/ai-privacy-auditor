# ai-privacy-auditor
A Python-based tool to redact PII from AI prompts, ensuring compliance with data protection standards.

# 🛡️ AI Privacy Auditor: Agentic Guardrail v1.0
**A technical implementation for PII Redaction in LLM Workflows.**

---

## 👤 About the Architect
**Senior Data Protection & Cybersecurity Consultant**
* **FIP** (Fellow of Information Privacy, IAPP)
* **CIPM, CIPP/E, CIPP/A**
* **Certified in Cybersecurity (CC)**, ISC2

I specialize in bridging the gap between **AI Innovation** and **Regulatory Compliance**. This project demonstrates a practical "Privacy-by-Design" technical control for autonomous AI agents.

---

## 🚀 The Problem: The "LLM Data Leak"
In 2026, the leading cause of regulatory investigations in Singapore is the accidental leakage of **Personally Identifiable Information (PII)** into Large Language Models (LLMs). Once data is sent to a cloud-based AI, it is often impossible to "un-learn" or retrieve.

## 🛠️ The Solution: The Privacy Guardrail
This repository contains a Python-based **pre-processor** designed to sit between a user and an AI Agent. It automatically detects and redacts sensitive Singaporean data formats before they ever reach the AI engine.

### Key Features:
* **SG Phone Number Detection:** Identifies 8-digit numbers starting with 8/9.
* **Email Redaction:** Pattern-matching for corporate and personal email formats.
* **Regulatory Alignment:** Directly addresses **Section 3 (Technical Controls)** of the *2026 IMDA Model AI Governance Framework for Agentic AI*.

---

## 📂 Project Structure
* `privacy_guard.py`: The core logic for PII detection and redaction.
* `requirements.txt`: Necessary libraries for deployment.

## 💻 How It Works
The script uses Regular Expressions (Regex) to scan incoming prompts.

```python
# Example Usage:
user_input = "Call me at 91234567 or email john@example.com"
safe_output = redact_pii(user_input)
# Result: "Call me at [PHONE_REDACTED] or email [EMAIL_REDACTED]"
