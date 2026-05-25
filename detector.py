def analyze_text(text):

    scam_keywords = scam_keywords = {
    "registration fee": 4,
    "processing fee": 4,
    "training fee": 4,
    "mandatory training fee": 5,
    "guaranteed placement": 5,
    "investment": 4,
    "telegram": 3,
    "whatsapp": 2,
    "otp": 6,
    "aadhaar": 5,
    "pan card": 5,
    "bank details": 6,
    "upi": 4,
    "send money": 5,
    "no interview": 4,
    "earn money": 3,
    "earn": 2,
    "daily": 2,
    "selected": 1,
    "salary": 1,
    "stipend": 1,
    "free iphone": 6,
    "work from home": 3,
    "urgent": 2,
    "limited slots": 2,
    "apply now": 2,
    "join today": 3,
    "click here": 3,
    "verification": 2,
    "shortlisted": 2,
    "reply within": 3,
    "offer cancelled": 3,
    "congratulations": 2
}

    text = text.lower()

    score = 0
    flags = []

    for word, weight in scam_keywords.items():

        if word in text:

            score += weight
            flags.append(f"{word} (+{weight})")

    if score >= 12:
        result = "EXTREME RISK"

    elif score >= 6:
        result = "HIGH RISK"

    elif score >= 4:
        result = "SUSPICIOUS"

    else:
        result = "SAFE"

    risk_percent = min(score * 10, 100)

    return result, flags, score, risk_percent