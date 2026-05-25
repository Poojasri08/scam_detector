from detector import analyze_text


def scan_jobs():

    with open("jobs.txt", "r", encoding="utf-8") as file:
        jobs = file.read().split("\n\n")

    report_lines = []

    report_lines.append("--- SCAN REPORT ---\n\n")

    for i, job in enumerate(jobs, 1):

        job = job.strip()

        if not job:
            continue

        result, flags, score, risk_percent = analyze_text(job)

        line = f"{i}. {job}\n"
        line += f"Result: {result}\n"
        line += f"Risk Score: {score}\n"
        line += f"Risk Percentage: {risk_percent}%\n"

        if flags:

            line += "Flags:\n"

            for f in flags:
                line += f"- {f}\n"

        line += "\n"

        print(line)

        report_lines.append(line)

    with open("report.txt", "w", encoding="utf-8") as report:

        for item in report_lines:
            report.write(item)

    print("Report generated successfully.")


def view_report():

    try:

        with open("report.txt", "r", encoding="utf-8") as report:

            print(report.read())

    except FileNotFoundError:

        print("No report found.")


while True:

    print("\n=== SCAM DETECTOR MENU ===")
    print("1. Scan Jobs")
    print("2. View Report")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        scan_jobs()

    elif choice == "2":

        view_report()

    elif choice == "3":

        print("Exiting...")
        break

    else:

        print("Invalid choice")
        