import re
scam_keywords=["pay fee","registration fee","advance payment","quick money","guaranteed income","work from home","no experience required","limited time offer","act now","click here","free trial","risk-free","money back guarantee","investment opportunity","get rich quick","easy money","make money fast","earn while you sleep","passive income","secret to success","exclusive deal","urgent response needed","winner","congratulations","you've been selected","limited spots available","don't miss out","once in a lifetime","too good to be true","no risk","100% free","no obligation","call now","instant access","limited time only","special promotion","exclusive offer","free gift","bonus offer","act fast","last chance","final notice"]
payment_words=['pay','fee','payment','advance','investment','money','income','earn','get rich','make money','passive income','send','transfer','deposit','withdraw','cash','bank','account','credit card','paypal','venmo','cryptocurrency','bitcoin','ethereum','upi','net banking','mobile payment','digital wallet','wire transfer','money order','check','cheque','western union','moneygram','cash app','zelle','square cash','google pay','apple pay','samsung pay']
def analyze_text(text):
    text = text.lower()
    score=0
    flags=[]

    for word in scam_keywords:
        if word in text:
            score+=1
            flags.append(f"keyword: {word}")

    numbers=re.findall(r'\b\d{10}\b', text)
    if numbers:
        for word in payment_words:
            if word in text:
                score+=2
                flags.append(f"payment number detected: {numbers} ")

    print("\n---SCAM ANALYSIS REPORT--- ")

    if flags:
        print("Suspicious patterns found:")
        for f in flags:
            print(" -",f)
    print("Score:",score)


    if score>=3:
        print("HIGH RISK SCAM")
    elif score==1 or score==2:
        print("SUSPICIOUS")
    else:
        print("LOOKS SAFE (still verify manually)")
    
text=input("Enter job/internship text:")
analyze_text(text)
