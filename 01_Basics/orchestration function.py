"""
1. RECIEVE AN EMAIL FROM USER  
2. VALIDATE THE EMAIL
3. IF ITS INVALID, LOG THE ERROR IN A FILE
4. IF ITS VALID, CLEAN AND STRUCTURED THE EMAIL
5. LOG EACH STEP OF THE PROGRAM

"""

def write_log(message):
    with open("pipline.txt", "a") as file:
        file.write(message + "\n")

def is_valid_email(email):
    return "@" in email and "." in email

def clean_split_email(email):
    email = email.strip().lower()

    username, domain = email.split("@")

    return {"username" : username,
            "domain" : domain
    }

#ochestration function

def process_user_email(email):

    print("APP STARTED")
    # 1. RECIEVE AN EMAIL FROM USER

    # 2. VALIDATE THE EMAIL

    if not is_valid_email(email):
        write_log(f"Invalid email : {email}")
    else:
        clean_email = clean_split_email(email)
        write_log(f"PROCESSED: {clean_email}")

    # 3. IF ITS INVALID, LOG THE ERROR IN A FILE
    # 4. IF ITS VALID, CLEAN AND STRUCTURED THE EMAIL
    # 5. LOG EACH STEP OF THE PROGRAM

    print("APP STOPPED")


email = input("Please type a input: ")
process_user_email(email)

#calling the function


