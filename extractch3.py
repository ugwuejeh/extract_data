# we import the necessary modules, such as `re` for regular expressions and `requests` to access the web page.

import re
import requests

def extract_data():
# we ask the user to enter the website url

 url = input("Enter the website url: ")


# we use the `requests` module to get the web page content.

 response = requests.get(url)
 content = response.text


# we use regular expressions to extract the phone number, email, and link.

 phone_pattern = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
 email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
 link_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
 phone_numbers = re.findall(phone_pattern, content)
 emails = re.findall(email_pattern, content)
 links = re.findall(link_pattern, content)


# we store the extracted email addresses in a separate file 

 output_filename = input("Enter the output file name: ")
 with open(output_filename, 'w') as f:
        for email in emails:
            f.write(email + '\n')
        with open(output_filename, 'w') as f:
            for phone_number in phone_numbers:
                f.write(phone_number + '\n')
            with open(output_filename, 'w') as f:
                for link in links:
                    f.write(link + '\n')
        print("Emails saved to file:", output_filename)
# Print the extracted information.

 print("Phone numbers:", phone_numbers)
 print("Emails:", emails)
 print("Links:", links)

extract_data()

