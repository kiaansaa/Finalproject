import sys
import random


if len(sys.argv) < 2:
    print("Error: Missing command-line argument.")
    sys.exit(1)


try:
    with open(sys.argv[1], "r") as input_file:
        student_data = input_file.readlines()
except:
    print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
    sys.exit(1)


emails = []
domain = "@poppleton.ac.uk"
for student in student_data:
    
    student_id, name = student.strip().split(" ",1)

    
    last, first = name.split(", ")
    
    last=last.replace("-", "").replace("'", "").replace(" ","").lower()
    first=(name.split(", ")[1].lower().split(" "))
    

    # Get the initials
    initials = ".".join([name[0] for name in first])
    

    
    email =''
    email = f"{initials}.{last}"
    email += f"{random.randint(1000,9999)}{domain}"
    
    emails.append(f"{student_id} {email}")



with open("emails.txt", "w") as output_file:
    output_file.write("\n".join(emails))
