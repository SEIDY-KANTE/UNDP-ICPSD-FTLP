"""
                        🚀 Frontier Tech Leaders Programme
||||||||||||||||||||||||||||||||| ASSIGNMENT 5 ||||||||||||||||||||||||||||||||||

"""

import re

"""
    Exercise: Extracting email addresses from text

    Given a text below,write a regular expression pattern to extract all emails from a text.

    email_text = "Contact us at support@example.com or at helpdesk@mysite.org."

    Expected Output:
    ['support@example.com', 'helpdesk@mysite.org']

"""

def extract_email_adresses(email_text:str):
    pattern=r"[aA-zZ]+?[0-9]*?[.]*?[a-z]*?@[a-z]+?[a-z.]*?[.]+?[com|org|fr|tr]+"
    emails=re.findall(pattern,email_text)
    return emails

email_text = "Contact us at support@example.com or at helpdesk@mysite.org. This is a student email address: fname.lname@ogr.university.edu.tr"


email_list=extract_email_adresses(email_text)

if len(email_list):
    print(email_list)
else:
    print("No email found!")
