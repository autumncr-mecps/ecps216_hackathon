import re

def process_emails(emails):
    """
    it can accept a single email as a string or multiple emails as a list of strings
    validates and returns a clean list of your emails
    Args:
        emails as a string or list
    return:
        valid list of emails 
    """
    #normalize the list
    if isinstance(emails, str):
        emails = [emails]
    elif not isinstance(emails, list):
        raise TypeError("input must be a string or list of strings")
    #emial verification pattern
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$')
    
    valid_emails = []
    invalid_emails = []
    for email in emails:
        email = email.strip().lower()
        if email_pattern.match(emails):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)
    #there are issues
    if invalid_emails:
        print(f"invalid emails")
    print(f"valid emails")
    return valid_emails
