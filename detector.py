def analyze_text(text):

    scam_keywords = {
        "registration fee": 3,
        "mandatory training fee": 4,
        "guaranteed placement": 4,
        "investment": 3,
        "telegram": 2,
        "whatsapp": 2,
        "otp": 5,
        "aadhaar": 4,
        "pan card": 4,
        "bank details": 5,
        "no interview": 3,
        "earn money": 2,
        "daily": 1,
        "selected": 1,
        "salary": 1,
        "stipend": 1,
        "free iphone": 5
    }

    text = text.lower()

    score = 0
    flags = []

    for word, weight in scam_keywords.items():

        if word in text:

            score += weight
            flags.append(f"{word} (+{weight})")

    if score >= 15:
        result = "EXTREME RISK"

    elif score >= 8:
        result = "HIGH RISK"

    elif score >= 4:
        result = "SUSPICIOUS"

    else:
        result = "SAFE"

    risk_percent = min(score * 10, 100)

    return result, flags, score, risk_percent