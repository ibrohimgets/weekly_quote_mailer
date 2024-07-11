#email_info
my_email = "ibrohimuminov@gmail.com"
password="youcantcrackthispasswordcanyou?0090"
app_passwords = "xlnt tyxo wuyp ckac"


#setup 
if True:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=app_passwords)
    connection.sendmail(from_addr=my_email, to_addrs="iibrohimm.com@gmail.com", msg="Subject:Hey\n\Another email has been sent!")
    connection.close()
    print("The email has been sent successfully!")
