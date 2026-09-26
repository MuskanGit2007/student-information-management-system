#menu based python program to manage stydent information in a college


import ast
FILE_NAME="students.txt"
def load_data():
    students={}
    try:
        with open(FILE_NAME, "r") as f:
            content = f.read().strip()
            if content:
                students = ast.literal_eval(content)
    except FileNotFoundError:
        pass
    return students


def save_data(students):
    with open(FILE_NAME, "w") as f:
        f.write(str(students))



#-------------------code of adding new sstudent--------------------------------------------------------
students={}
branch=['CSE', 'EEE', 'CIVIL', 'MECHENICAL','cse', 'eee', 'civil', 'mechenical']
def add_new_student(students):

    #------------------reg no----------------------------------
    while True:
        constant_part='24105129'
        # try:
        last_digits=input("Enter last three digit of your Registrestion Number: ")
            #last_digits2=str(last_digits)
            

        if last_digits.isdigit() and len(last_digits)==3:
            reg_no=constant_part + last_digits
            print(reg_no)
            if reg_no in students:
                print("This registration number already exist. Enter another registration number.")
                continue
            else:
                pass  
        else:
            print("Please enter exactly last 3 digit of your registation number.")
            continue   
        # except:
        #     print("Error: last digit must be integer.")
        #     continue
    #----------name-----------------------------------------------
        while True:
            try:
                name=input("Enter your Full name: ")
                #if name.isalpha()==True:
                name=" ".join(name.split())
                name=name.title()
                print(name)
                break
                # else:
                #     print("Name should only contain alphabet")
                #     continue
            except:
                print("Error: name only contain string")
                continue
    #----------branch-------------------------------------------------
        while True:
            
            try:
                your_branch=input(f"Enter your branch{branch}: ")
                if not your_branch in branch:
                    print("Error: Invalid branch!")
                    continue
                else:
                    break
            except:
                print(f"Branch must be from {branch}.")
                continue
    #---------------------admission year-----------------------------------------
        while True:
            try:
                admission_year=int(input("Enter your Admission year: "))
                if admission_year<2015 or admission_year>2025:
                    print("Invalid admission yearr!")
                    continue
                else:
                    break
            except:
                print("Error: Admission year must be an integer.")
                continue
    #-------------------phone no---------------------------------------------------
        while True:
            code='+91'
            try:
                phone=int(input("Enter your phone number: "))
                phone2=str(phone)
                if len(phone2)==10:
                    final_phone= code + phone2
                    print("Phone no: ",final_phone)
                    break
                else:
                    print("Phone number must have 10 digits.")
                    continue
            except:
                print("Phone number must be positive integer.")
                continue
    #----------------email----------------------------------------
        while True:
            const_email="@gmail.com"
            email=input("Enter first part of your email: ")
            email_id=email+const_email
            if email.isalnum():
                print("Email Id: ",email_id)
                break
            else:
                print("Email id only contain digit and string")
                continue
    #--------------------last semester----------------------------
        while True:
            try:
                last_coplate_sem=int(input("Enter last complated semester: "))
                if last_coplate_sem<0 or last_coplate_sem>8:
                    print("Invalid Input!")
                    continue
                else:
                    break
            except:
                print("Last semester must be an integer.")
                continue
    #--------------------cgpa-------------------------------------
        while True:
            try:
                cgpa=float(input("Enter cgpa: "))
                if cgpa<0 or cgpa>10:
                    print("Invalid Input!")
                    continue
                else:
                    break
            except:
                print("cgpa must be a float value.")
                continue

        current_sem_year=last_coplate_sem+1
        print("Current semester year: ", current_sem_year)
        print("Student added sucessfully!")

        students[reg_no]={
                "name": name,
                "branch": your_branch,
                "admission year": admission_year,
                "contact": (phone, email_id),
                "acedmic_history": (current_sem_year, cgpa, admission_year)
        }
        # main()
        save_data(students)
        break
    

#----------------code for Fetch and display student information----------------------------------------
def fetch_student_info(students):
    constant_part = '24105129'
    last_digits = input("Enter last three digits of Registration Number of student you want to fetch: ")

    if last_digits.isdigit() and len(last_digits) == 3:
        reg_no = constant_part + last_digits
        print("Searching: ", reg_no)

        if reg_no in students:
            print("Student found:", students[reg_no])
        else:
            print("Error: Student with this Registration Number not found.\n")
    else:
        print("Please enter exactly 3 digits.")

#-----------------code for update student details----------------------------------------------------
def update_student_details(students):
    while True:
        constant_part='24105129'
        try:
            last_digits=input("Enter last three digit of Registrestion Number of student you want to update student details: ")
            if last_digits.isdigit() and len(last_digits) == 3:
                reg_no = constant_part + last_digits
                print(reg_no)
            else:
                print("Please enter exactly last 3 digit of your registation number.")
                continue   
        except:
            print("Error: last digit must be integer.")
            continue
        if not reg_no in students:
            print("Registration number not found!")
        else:
            while True:
                print("Press 1. To update student's name: ")
                print("Press 2. To update branch: ")
                print("Press 3. To update admission year: ")
                print("Press 4. To update contact: ")
                print("Press 5. To update acedmic history: ")
                print("Press 6. Exit: ")
                try:
                    choice_update=int(input("Enter your choice for update: "))
                    if choice_update<1 or choice_update>6:
                        print("Error: Ivalid choice!")
                except:
                    print("Error: Choice must be an Integer.")
                    continue

                match choice_update:
    #----------------------update name-------------------------------------------------------------------------------
                    case 1:
                            try:
                                new_name=input("Enter new name: ")
                                new_name=" ".join(new_name.split())
                                new_name=new_name.title()
                                print(new_name)
                                students[reg_no]["name"]=new_name
                                print("Student name updated sucessfully.")
                            except:
                                print("Error: Name must be string!")
                            save_data(students)
    #-------------------------update branch----------------------------------------------------------------------------------
                    case 2:
                            while True:
                                try:
                                    your_new_branch=input(f"Enter your new branch{branch}: ")
                                    if not your_new_branch in branch:
                                        print("Error: Invalid branch!")
                                        continue
                                    else:
                                        break
                                except:
                                    print(f"Branch must be from {branch}.")
                                    continue
                                students[reg_no]["branch"]=your_new_branch
                                print("Student branch updated sucessfully.")
                                break
                            save_data(students)
    #--------------------------------------update admission year---------------------------------------------------------------------
                    case 3: 
                        try:
                            new_admission_year=int(input("Enter your Admission year: "))
                            if new_admission_year<2015 or admission_year>2025:
                                print("Invalid admission yearr!")
                                continue
                            else:
                                break
                        except:
                            print("Error: Admission year must be an integer.")
                            continue
                        students[reg_no]["admission_year"]=new_admission_year
                        print("Student branch updated sucessfully.")
                        save_data(students)
    #---------------------------------------update contact-----------------------------------------------------------------------------
                    case 4:
                            while True:
                                print("Press 1. To update phone number: ")
                                print("Press 2. To update email: ")
                                print("press 3. If you updated your contact")
                                try:
                                    choice_contact=int(input("Enter your choice: "))
                                    if choice_contact<1 or choice_contact>3:
                                        print("Error: Ivalid choice!")
                                except:
                                    print("Error: Choice must be an Integer.")
                                    continue
                                match choice_contact:
                                    case 1:
                                        phone=input("Enter new phone number: ")
                                        students[reg_no]["contact"] = (phone, students[reg_no]["contact"][1])
                                        print("Student phone number updated sucessfully.")
                                        
                                        continue
                                    case 2:
                                        email=input("Enter new phone email: ")
                                        students[reg_no]["contact"] = (students[reg_no]["contact"][0], email)
                                        print("Student email updated sucessfully.")
                                        # save_data(students)
                                    case 3:
                                        break
                                # students[reg_no]["contact"]=(phone, email)
                                save_data(students)

    #------------------------------update acedmic history--------------------------------------------------------------------------
                    case 5:
                        while True:
                            print("Press 1. To update current semester year: ")
                            print("Press 2. To update cgpa: ")
                            print("Press 3. To update admission year: ")
                            print("press 4. If you updated your contact")
                            try:
                                choice_acedmic_history=int(input("Enter your choice: "))
                                if choice_acedmic_history<1 or choice_acedmic_history>3:
                                    print("Error: Ivalid choice!")
                            except:
                                print("Error: Choice must be an Integer.")
                                continue
                            match choice_acedmic_history:
                                case 1:
                                    current_semester_year=int(input("Enter updated semester year: "))
                                    print("Student current semester year updated sucessfully.")
                                case 2:
                                    cgpa=float(input("Enter updated cgpa: "))
                                    print("Student cgpa updated sucessfully.")
                                case 2:
                                    admission_year=int(input("Enter updated admission year: "))
                                    print("Student admission year updated sucessfully.")
                                case 3:
                                        break
                            students[reg_no]["acedmic_history"]=(current_semester_year, cgpa, admission_year)
                            save_data(students)
                    case 6:
                        break
                        main()
        

#-----------------------code for display all student----------------------------------------------
def display_all_student(students):
    print("\n")
    print("*"*70)
    print("reg. no.        | Name            | Branch           | CGPA         ")
    for key, val in students.items():
        print(f"{key: <15} | {val["name"]:<15} | {val["branch"]:<15} | {val["acedmic_history"][1]:<15}")
    print("\n")
    print("*"*70)
    
#-------------------------code for find student by branch------------------------------------------------ 
def find_student_by_branch(students, branch):
    for key, val in students.items():
        if val["branch"]==branch:
            print(val)
        else:
            print("Student not found with this branch.")
#------------------------code to compare acedmic performance---------------------------------------------
def compare_acedmic_performance(students):
    reg_no1=input("Enter first student reg no: ")
    reg_no2=input("Enter second student reg no: ")
    if reg_no1 in students and reg_no2 in students:
        cgpa1=students[reg_no1]["acedmic_history"][1]
        cgpa2=students[reg_no2]["acedmic_history"][1]
        if cgpa1==cgpa2:
            print("Both students have equall cgpa.")
        elif cgpa1>cgpa2:
            print("First student having more cgpa than second.")
        else:
            print("Second student having more cgpa than first.")
    else:
        print("reg no not fund!")  
    
def main():
    students=load_data()
    while True:
        print("Press 1. Add new student: ")
        print("Press 2. Fetch and display student information: ")
        print("Press 3. Update student details: ")
        print("Press 4. Display all students: ")
        print("Press 5. Find students by branch: ")
        print("Press 6. Compare acedmic performance: ")
        print("Press 7. Exit: ")
        try:
            choice=int(input("Enter your choice: "))
            if choice>7:
                print("Error: Ivalid choice!")
        except:
            print("Error: Choice must be an Integer.")
            continue

        match choice:
            case 1:
                add_new_student(students)
                save_data(students)
            case 2:
                fetch_student_info(students)
            case 3:
                update_student_details(students)
            case 4: 
                display_all_student(students)
            case 5: 
                branch=input("Enter student's branch: ")
                find_student_by_branch(students, branch)
            case 6:
                compare_acedmic_performance(students)
            case 7: 
                print("By by by.....")
                break

if __name__ == "__main__":
    main()    
