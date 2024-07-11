import smtplib
import datetime as dt
import random

# Get current datetime
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:  # Check if today is Thursday (Thursday is index 3)
    # Read quotes from file
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes).strip()  # Choose a random quote and strip any extra whitespace

    # Email setup
    my_email = "ibrohimuminov@gmail.com"
    app_passwords = "xlnt tyxo wuyp ckac"  # Replace with your generated app password

    # Establish connection to SMTP server
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_passwords)

            # Compose the email
            subject = "Thursday, I launched this app using PYTHON."
            body = f"You receive the same email every week with a different quote!\n\n{random_quote}"
            message = f"Subject: {subject}\n\n{body}"

            # Send email
            to_addrs = ["iibrohimm.com@gmail.com", "961972398@qq.com"]
            connection.sendmail(from_addr=my_email, to_addrs=to_addrs, msg=message)
            print("The email has been sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")
