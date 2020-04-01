import json
import smtplib

s= smtplib.SMTP()
s.connect("Enter Server Name",587)
s.starttls()
s.login('Enter Secret Key','Enter Password')

 
def lambda_handler(event, context):
        msg = 'From: SES_registered_email_ID\nTo: xyz@gmail.com\nSubject: Test Email\n\nType message here'
        s.sendmail('SES_registered_email_ID','xyz@gmail.com', msg)

   
   
    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully")
    }
