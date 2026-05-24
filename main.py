def analyze_text(text):
    scam_keywords = [
        "pay fee",
        "registration fee",
        "advance payment",
        "quick money",
        "guaranteed income"
    ]

    text = text.lower()
    score = 0
    flags = []

    for word in scam_keywords:
        if word in text:
            score += 1
            flags.append(word)

    if score >= 2:
        result = "HIGH RISK"
    elif score == 1:
        result = "SUSPICIOUS"
    else:
        result = "SAFE"

    return result, flags


# Read input file
with open("jobs.txt", "r") as file:
    jobs = file.readlines()

print("\n--- SCAN REPORT ---")

# Analyze each job
for i, job in enumerate(jobs, 1):
    result, flags = analyze_text(job.strip())

    print(f"\n{i}. {job.strip()}")
    print("Result:", result)

    if flags:
        print("Flags:")
        for f in flags:
            print("-", f)

# Save report to file
with open("report.txt", "w") as report:
    report.write("--- SCAN REPORT ---\n\n")

    for i, job in enumerate(jobs, 1):
        result, flags = analyze_text(job.strip())

        report.write(f"\n{i}. {job.strip()}\n")
        report.write(f"Result: {result}\n")

        if flags:
            report.write("Flags:\n")
            for f in flags:
                report.write(f"- {f}\n")

        report.write("\n")
