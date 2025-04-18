import re

RISKY_TERMS = [
    "indemnify", "liability", "arbitration", "termination", "confidentiality",
    "force majeure", "exclusion of liability", "non-compete", "liquidated damages"
]

def analyze_risks(text):
    risks = []
    for term in RISKY_TERMS:
        if re.search(rf"\b{term}\b", text, re.IGNORECASE):
            risks.append(term)
    return risks
