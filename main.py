from OOPS_Project import Admission, Student, Result, Library
import os
import re
import csv
from csv import writer
import time
import pandas as pd
from datetime import datetime


def clear(): return os.system('cls')


message = ""

# Names of all CSV files to access
data = {"BCA": ["Data\\f_bca.csv", "Data\\s_bca.csv", "Data\\t_bca.csv"], "BCA in Analytics": ["Data\\f_bca_ana.csv", "Data\\s_bca_ana.csv", "Data\\t_bca_ana.csv"], "BSc(PMCS)": ["Data\\f_bsc(pmcs).csv", "Data\\s_bsc(pmcs).csv", "Data\\t_bsc(pmcs).csv"], "BSc(PME)": ["Data\\f_bsc(pme).csv", "Data\\s_bsc(pme).csv", "Data\\t_bsc(pme).csv"], "BBA": ["Data\\f_bba.csv", "Data\\s_bba.csv", "Data\\t_bba.csv"], "BBA in Aviation": ["Data\\f_bba_ava.csv", "Data\\s_bba_ava.csv", "Data\\t_bba_ava.csv"], "BCom": [
    "Data\\f_bcom.csv", "Data\\s_bcom.csv", "Data\\t_bcom.csv"], "BCom in Finance": ["Data\\f_bcom_fin.csv", "Data\\s_bcom_fin.csv", "Data\\t_bcom_fin.csv"], "BCom in Tourism": ["Data\\f_bcom_tou.csv", "Data\\s_bcom_tou.csv", "Data\\t_bcom_tou.csv"], "BA in English": ["Data\\f_ba_eng.csv", "Data\\s_ba_eng.csv", "Data\\t_ba_eng.csv"], "BA in Sociology": ["Data\\f_ba_soc.csv", "Data\\s_ba_soc.csv", "Data\\t_ba_soc.csv"], "BA in Economics": ["Data\\f_ba_eco.csv", "Data\\s_ba_eco.csv", "Data\\t_ba_eco.csv"]}
count = ["counts\\bca.txt", "counts\\bca_in_analytics.txt", "counts\\bscpmcs.txt", "counts\\bscpme.txt", "counts\\bba.txt", "counts\\bba_aviation.txt",
         "counts\\bcom.txt", "counts\\bcom_finance.txt", "counts\\bcom_tourism.txt", "counts\\ba_english.txt", "counts\\ba_economics.txt", "counts\\ba_sociology.txt"]
timeTable = {"BCA": ["time_table\\f_bca_tt.csv", "time_table\\s_bca_tt.csv", "time_table\\t_bca_tt.csv"], "BCA in Analytics": ["time_table\\f_bcaana_tt.csv", "time_table\\s_bcaana_tt.csv", "time_table\\t_bcaana_tt.csv"], "BSc(PMCS)": ["time_table\\f_bsc(pmcs)_tt.csv", "time_table\\s_bsc(pmcs)_tt.csv", "time_table\\t_bsc(pmcs)_tt.csv"], "BSc(PME)": ["time_table\\f_bsc(pme)_tt.csv", "time_table\\s_bsc(pme)_tt.csv", "time_table\\t_bsc(pme)_tt.csv"], "BBA": ["time_table\\f_bba_tt.csv", "time_table\\s_bba_tt.csv", "time_table\\t_bba_tt.csv"], "BBA in Aviation": ["time_table\\f_bbaava_tt.csv", "time_table\\s_bbaava_tt.csv", "time_table\\t_bbaava_tt.csv"], "BCom": [
    "time_table\\f_bcom_tt.csv", "time_table\\s_bcom_tt.csv", "time_table\\t_bcom_tt.csv"], "BCom in Finance": ["time_table\\f_bcomfin_tt.csv", "time_table\\s_bcomfin_tt.csv", "time_table\\t_bcomfin_tt.csv"], "BCom in Tourism": ["time_table\\f_bcomtou_tt.csv", "time_table\\s_bcomtou_tt.csv", "time_table\\t_bcomtou_tt.csv"], "BA in English": ["time_table\\f_baeng_tt.csv", "time_table\\s_baeng_tt.csv", "time_table\\t_baeng_tt.csv"], "BA in Sociology": ["time_table\\f_basoc_tt.csv", "time_table\\s_basoc_tt.csv", "time_table\\t_basoc_tt.csv"], "BA in Economics": ["time_table\\f_baeco_tt.csv", "time_table\\s_baeco_tt.csv", "time_table\\t_baeco_tt.csv"]}
results = {"BCA": ["results\\f_bca_results.csv", "results\\s_bca_results.csv", "results\\t_bca_results.csv"], "BCA in Analytics": ["results\\f_bcaana_results.csv", "results\\s_bcaana_results.csv", "results\\t_bcaana_results.csv"], "BSc(PMCS)": ["results\\f_bsc(pmcs)_results.csv", "results\\s_bsc(pmcs)_results.csv", "results\\t_bsc(pmcs)_results.csv"], "BSc(PME)": ["results\\f_bsc(pme)_results.csv", "results\\s_bsc(pme)_results.csv", "results\\t_bsc(pme)_results.csv"], "BBA": ["results\\f_bba_results.csv", "results\\s_bba_results.csv", "results\\t_bba_results.csv"], "BBA in Aviation": ["results\\f_bbaava_results.csv", "results\\s_bbaava_results.csv", "results\\t_bbaava_results.csv"], "BCom": [
    "results\\f_bcom_results.csv", "results\\s_bcom_results.csv", "results\\t_bcom_results.csv"], "BCom in Finance": ["results\\f_bcomfin_results.csv", "results\\s_bcomfin_results.csv", "results\\t_bcomfin_results.csv"], "BCom in Tourism": ["results\\f_bcomtou_results.csv", "results\\s_bcomtou_results.csv", "results\\t_bcomtou_results.csv"], "BA in English": ["results\\f_baeng_results.csv", "results\\s_baeng_results.csv", "results\\t_baeng_results.csv"], "BA in Sociology": ["results\\f_basoc_results.csv", "results\\s_basoc_results.csv", "results\\t_basoc_results.csv"], "BA in Economics": ["results\\f_baeco_results.csv", "results\\s_baeco_results.csv", "results\\t_baeco_results.csv"]}
attendance = {"BCA": ["attendance\\f_bca_attendance.csv", "attendance\\s_bca_attendance.csv", "attendance\\t_bca_attendance.csv"], "BCA in Analytics": ["attendance\\f_bcaana_attendance.csv", "attendance\\s_bcaana_attendance.csv", "attendance\\t_bcaana_attendance.csv"], "BSc(PMCS)": ["attendance\\f_bsc(pmcs)_attendance.csv", "attendance\\s_bsc(pmcs)_attendance.csv", "attendance\\t_bsc(pmcs)_attendance.csv"], "BSc(PME)": ["attendance\\f_bsc(pme)_attendance.csv", "attendance\\s_bsc(pme)_attendance.csv", "attendance\\t_bsc(pme)_attendance.csv"], "BBA": ["attendance\\f_bba_attendance.csv", "attendance\\s_bba_attendance.csv", "attendance\\t_bba_attendance.csv"], "BBA in Aviation": ["attendance\\f_bbaava_attendance.csv", "attendance\\s_bbaava_attendance.csv", "attendance\\t_bbaava_attendance.csv"], "BCom": [
    "attendance\\f_bcom_attendance.csv", "attendance\\s_bcom_attendance.csv", "attendance\\t_bcom_attendance.csv"], "BCom in Finance": ["attendance\\f_bcomfin_attendance.csv", "attendance\\s_bcomfin_attendance.csv", "attendance\\t_bcomfin_attendance.csv"], "BCom in Tourism": ["attendance\\f_bcomtou_attendance.csv", "attendance\\s_bcomtou_attendance.csv", "attendance\\t_bcomtou_attendance.csv"], "BA in English": ["attendance\\f_baeng_attendance.csv", "attendance\\s_baeng_attendance.csv", "attendance\\t_baeng_attendance.csv"], "BA in Sociology": ["attendance\\f_basoc_attendance.csv", "attendance\\s_basoc_attendance.csv", "attendance\\t_basoc_attendance.csv"], "BA in Economics": ["attendance\\f_baeco_attendance.csv", "attendance\\s_baeco_attendance.csv", "attendance\\t_baeco_attendance.csv"]}

# The first function to be executed in program.


def main_menu():
    counter = 0
    while counter == 0:
        clear()
        print(" Kristu Jayanti College ".center(146, '-'))
        print("\nWelcome to our Student_Buddy - Interface.")
        ans = input("\nPlease enter the option number you desrire to continue with\n\n1. Admissions\n2. ID Card\n3. Examinations\n4. Attendence\n5. Library\n6. Co-Curricular Activities\n7. Exit\n\nEnter your option: ")

        if ans.isdigit() and ans not in "890`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\" and int(ans) < 8:
            response(ans)
        else:
            print("Invalid input")
            time.sleep(3)

# Function which captures response and calls the appropriate function name.


def response(n):
    if n == "1":
        admission()
    elif n == "2":
        idcard()
    elif n == "3":
        exam()
    elif n == "4":
        attendence()
    elif n == "5":
        library()
    elif n == "6":
        coCurricular()
    elif n == "7":
        exit()


def admission():
    # First step of admission process.
    def apply():
        clear()
        print(" Application Form ".center(133, '-'))
        print("\nPress 0 to go back to Admission main menu")
        fname = input("Enter your first name : ").title()
        if fname == "0":
            admission()

        lname = input("\nEnter your last name : ").title()
        if lname == "0":
            admission()

        ag = 0
        while (ag == 0):
            ans1 = input(
                "\nEnter your gender \n1. Male \n2. Female\nEnter the option number : ")
            if ans1 == "1":
                gender = "Male"
                ag = 1
            elif ans1 == "2":
                gender = "Female"
                ag = 1
            elif ans1 == "0":
                admission()
            else:
                print("\nEnter a valid option number")

        adob = 0
        while (adob == 0):
            dob = input("\nEnter your DOB in DD/MM/YYYY format : ")
            p = r"^(3[01]|[1-2][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(([0-9]{4}))$"
            result = re.findall(p, dob)
            if len(result) > 0:
                adob = 1
            elif dob == "0":
                admission()
            else:
                print("\nInvalid format !")

        phoneno = input("\nEnter your Phone No. : ")
        if phoneno == "0":
            admission()

        while (len(phoneno) != 10 or phoneno.isdigit() == False):
            print("\nEnter a valid phome number")
            phoneno = input("\nEnter your Phone No. : ")

        emailid = input("\nEnter your Email-ID : ")
        if emailid == "0":
            admission()

        while (emailid.endswith(".com") == False or "@" not in emailid):
            print("\nPlease enter a valid Email ID")
            emailid = input("\nEnter your Email ID : ")

        address = input("\nEnter your address : ").title()
        if address == "0":
            admission()

        father_name = input("\nEnter your Father's name : ").title()
        if father_name == "0":
            admission()

        father_occupation = input(
            "\nEnter your Father's occupation : ").title()
        if father_occupation == "0":
            admission()

        mother_name = input("\nEnter your Mother's name : ").title()
        if mother_name == "0":
            admission()

        mother_occupation = input(
            "\nEnter your Mother's occupation : ").title()
        if mother_occupation == "0":
            admission()

        ac = 0
        while (ac == 0):
            ans2 = input(
                "\nSelect your Category \n1. General\n2. SC|ST\n3. 2B\n4. 3B\nEnter option number :  ")
            if ans2 == "0":
                admission()
            elif ans2 == "1":
                category = "General"
                ac = 1
            elif ans2 == "2":
                category = "SC|ST"
                ac = 1
            elif ans2 == "3":
                category = "2B"
                ac = 1
            elif ans2 == "4":
                category = "3B"
                ac = 1
            else:
                print("\nEnter a valid option number")

        ts = 0
        while ts == 0:
            tenth_score = input(
                "\nEnter your 10th grade marks (in percentage %) : ")
            if tenth_score.isdigit() == False or tenth_score in '`~!@#$%^&*()-_+={\}[]|\:;"\'<,>.?/' or int(tenth_score) > 100:
                print("\nEnter marks ranging from 1 to 100")
            elif tenth_score == "0":
                admission()
            elif tenth_score.isdigit():
                ts = 1

        tws = 0
        while tws == 0:
            twelveth_score = input(
                "\nEnter your 12th grade marks (in percentage %) : ")
            if twelveth_score.isdigit() == False or twelveth_score in '`~!@#$%^&*()-_+={\}[]|\:;"\'<,>.?/' or int(twelveth_score) > 100:
                print("\nEnter marks ranging from 1 to 100")
            elif twelveth_score == "0":
                admission()
            elif tenth_score.isdigit():
                tws = 1

        aps = 0
        while (aps == 0):
            ans3 = input(
                "\nSelect your previous stream \n1. Science\n2. Commerce\n3. Arts\nEnter option number : ")
            if ans3 == "0":
                admission()
            elif ans3 == "1":
                previous_stream = "Science"
                aps = 1
            elif ans3 == "2":
                previous_stream = "Commerce"
                aps = 1
            elif ans3 == "3":
                previous_stream = "Arts"
                aps = 1
            else:
                print("\nEnter a valid option")

        aos = 0
        while (aos == 0):
            if previous_stream == "Science":
                ans4 = input(
                    "\nSelect the stream you want to opt for \n1. Science\n2. Commerce\n3. Arts\nEnter option number : ")
                if ans4 == "0":
                    admission()
                elif ans4 == "1":
                    stream_opting_for = "Science"
                    aos = 1
                elif ans4 == "2":
                    stream_opting_for = "Commerce"
                    aos = 1
                elif ans4 == "3":
                    stream_opting_for = "Arts"
                    aos = 1
                else:
                    print("\nEnter a valid option")

            elif previous_stream == "Commerce":
                ans4 = input(
                    "\nSelect the stream you want to opt for \n1. Commerce\n2. Arts \nEnter option number : ")
                if ans4 == "0":
                    admission()
                elif ans4 == "1":
                    stream_opting_for = "Commerce"
                    aos = 1
                elif ans4 == "2":
                    stream_opting_for = "Arts"
                    aos = 1
                else:
                    print("\nEnter a valid option")

            elif previous_stream == "Arts":
                ans4 = input(
                    "\nSelect the stream you want to opt for \n1. Arts\nEnter option number : ")
                if ans4 == "0":
                    admission()
                elif ans4 == "1":
                    stream_opting_for = "Arts"
                    aos = 1
                else:
                    print("\nEnter a valid option")

        if stream_opting_for == "Science":
            asc = 0
            while (asc == 0):
                ans5 = input(
                    "\nSelect the course your opting for : \n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\nEnter option number : ")
                if ans5 == "0":
                    admission()
                elif ans5 == "1":
                    course_opting_for = "BCA"
                    asc = 1
                elif ans5 == "2":
                    course_opting_for = "BCA in Analytics"
                    asc = 1
                elif ans5 == "3":
                    course_opting_for = "BSc(PMCS)"
                    asc = 1
                elif ans5 == "4":
                    course_opting_for = "BSc(PME)"
                    asc = 1
                else:
                    print("\nEnter a valid option")

        elif stream_opting_for == "Commerce":
            aco = 0
            while (aco == 0):
                ans6 = input(
                    "\nSelect the course your opting for : \n1. BBA\n2. BBA in Aviation\n3. BCom\n4. BCom in Finance\n5. BCom in Tourism\nEnter option number : ")
                if ans6 == "0":
                    admission()
                elif ans6 == "1":
                    course_opting_for = "BBA"
                    aco = 1
                elif ans6 == "2":
                    course_opting_for = "BBA in Aviation"
                    aco = 1
                elif ans6 == "3":
                    course_opting_for = "BCom"
                    aco = 1
                elif ans6 == "4":
                    course_opting_for = "BCom in Finance"
                    aco = 1
                elif ans6 == "5":
                    course_opting_for = "BCom in Tourism"
                    aco = 1
                else:
                    print("Enter a valid option")

        elif stream_opting_for == "Arts":
            aar = 0
            while (aar == 0):
                ans7 = input(
                    "\nSelect the course your opting for : \n1. BA in Sociology\n2. BA in Economics\n3. BA in English\nEnter option number : ")
                if ans7 == "0":
                    admission()
                elif ans7 == "1":
                    course_opting_for = "BA in Sociology"
                    aar = 1
                elif ans7 == "2":
                    course_opting_for = "BA in Economics"
                    aar = 1
                elif ans7 == "3":
                    course_opting_for = "BA in English"
                    aar = 1
                else:
                    print("\nEnter a valid option")

        achievements = input(
            "\nEnter any achievements achieved : ").capitalize()
        if achievements == "0":
            admission()

        a = Admission(fname, lname, gender, dob, phoneno, emailid, address, father_name, father_occupation, mother_name,
                      mother_occupation, category, tenth_score, twelveth_score, previous_stream, stream_opting_for, course_opting_for, achievements)
        print(
            f"\nThank you for applying. Your application number is {a.get_app_no()} \nPlease note down the application number for future reference and wait as we process your application and check your eligibility for the chosen course.\nIf any changes/updates has to be made, go to update option in the main menu.\n\n")
        time.sleep(10)
        selection_process(a)

    # Second step of admission process.

    def selection_process(a):
        # Importing methods from Admission class
        # Checking course availability
        if Admission.check_course_availability(a) == True:
            # Checking eligibility
            if Admission.check_eligibility(a) == True:
                a.set_status("Selected")
                message = "Selected"
            else:
                a.set_status("Not selected")
                message = Admission.check_eligibility(a)
        else:
            message = Admission.check_course_availability(a)
        review(message, a)

    # Third step of admission process.
    def review(m, a):
        print("Applicant's result".center(146, '-'))
        if m == "Selected":
            print("\n\nCongratulations on getting selected ! Please proceed with document submission and fee payment process to end the admission formalities.\n\n")

        elif a.get_status() == "Not selected":
            print(f"\n{m}")
            time.sleep(10)

        else:
            print(f"\n{m}")
            time.sleep(10)
            with open("C:\\Users\\2145644\\OOPSProject\\counts\\appln_count.txt", 'r') as r:
                count = int(r.read())
                count -= 1
            with open("C:\\Users\\2145644\\OOPSProject\\counts\\appln_count.txt", 'w+') as w:
                w.write(str(count))
            admission()
        document_submission(m, a)

    # Forth step of admission process.
    def document_submission(m, a):
        if m == "Selected":
            time.sleep(3)
            print("Document Submission".center(146, '-'))
            Admission.document_submission(a)
            fee_process(a)
        else:
            Admission.set_documents(a, "NA")
            save_data(a)

    # Fifth step of admission process.
    def fee_process(a):
        print("\n")
        print("Fee Payment".center(146, '-'))
        Admission.fee_payment(a)
        print("\nThanks for taking admission in our college. We wish you all the best on your journey with us.")
        time.sleep(5)
        save_data(a)

    def save_data(a):
        old_info = a.__dict__
        new_info = {}
        for i, j in old_info.items():
            key = i.replace("_Admission__", "")
            new_info[key] = j
            data = [new_info]

        fields = ["appno", "first_name", "last_name", "gender", "dob", "phone_no", "email_id", "address", "father_name", "father_occupation", "mother_name",
                  "mother_occupation", "category", "tenth_score", "twelveth_score", "previous_stream", "stream_opting_for", "course_opting_for", "achievements", "status", "documents"]

        with open('Data\\applications.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writerows(data)
            admission()

    # Updating applicant's information
    def update_app():
        clear()
        appln_no = []
        csv_file_reader = csv.reader(
            open("C:\\Users\\2145644\\OOPSProject\\Data\\applications.csv", "r"))
        for row1 in csv_file_reader:
            if row1[0] == 'appno':
                continue
            appln_no.append(row1[0])

        print(" Update Application ".center(146, '-'))
        print("\nPress 0 to go back to main menu")
        status = 0
        while (status == 0):
            appno = input("\nEnter your application number : ")
            if appno == "0":
                admission()
            elif appno in appln_no:
                status = 1
            else:
                print(
                    "\nApplication entered is incorrect. Please enter the right application number.")

        columns = ["Application No.", "First name", "Last name", "Gender", "DOB", "Phone Number", "Email-ID", "Address", "Father name", "Father occupation",
                   "Mother name", "Mother occupation", "Category", "10th score", "12th score", "Previous stream", "Opting stream", "Opting course", "Achievements", "Status", "Documents"]
        row_pos = 0
        index = 0
        csv_file_reader2 = csv.reader(
            open("C:\\Users\\2145644\\OOPSProject\\Data\\applications.csv", "r"))
        for row in csv_file_reader2:
            if row[0] == appno:
                for i in range(len(row)):
                    if i == 15 or i == 16 or i == 17:
                        print(
                            f"\n{index} . {columns[i]} : {row[i]} - Cannot be updated/changed.")
                        index += 1
                        continue
                    if i == 19:
                        continue
                    if i == 20:
                        str_docs = eval(row[i])
                        print(f"\n{index} . Documents")
                        print("---------------------")
                        for doc, stats in str_docs.items():
                            print(f" {doc.strip()} : {stats.strip()}")
                        continue
                    print(f"\n{index} . {columns[i]} : {row[i]}")
                    index += 1
                break
            else:
                row_pos += 1

        counter = 0
        df = pd.read_csv("Data\\applications.csv")
        while (counter == 0):
            option = input("\nEnter the option number to change : ")
            if option.isdigit() == False or option in '`~!@#$%^&*()-_+={\}[]|\:;"\'<,>.?/':
                print("Invalid input")
                time.sleep(3)

            elif int(option) > 19:
                print("Invalid input")
                time.sleep(3)

            elif option == "0":
                counter = 1
                admission()

            elif option == "1":
                u_fname = input("\nEnter your first name : ").title()
                df.loc[(row_pos - 1), 'first_name'] = u_fname

            elif option == "2":
                u_lname = input("\nEnter your last name : ").title()
                df.loc[(row_pos - 1), 'last_name'] = u_lname

            elif option == "3":
                counter1 = 0
                while counter1 == 0:
                    ans1 = input(
                        "\nEnter your gender \n1. Male \n2. Female\nEnter the option number : ")
                    if ans1 == "1":
                        u_gender = "Male"
                        counter1 = 1
                    elif ans1 == "2":
                        u_gender = "Female"
                        counter1 = 1
                    else:
                        print("\nInvalid input")
                df.loc[(row_pos - 1), 'gender'] = u_gender

            elif option == "4":
                u_dob = input("\nEnter your DOB in DD/MM/YYYY format : ")
                condition = True
                while (condition):
                    p = r"^(3[01]|[1-2][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(([0-9]{4}))$"
                    result = re.findall(p, u_dob)
                    if len(result) > 0:
                        break
                    else:
                        print("\nInvalid format !")

                df.loc[(row_pos - 1), 'dob'] = u_dob

            elif option == "5":
                u_phoneno = input("\nEnter your Phone No. : ")
                while (len(u_phoneno) != 10 or u_phoneno.isdigit() == False):
                    print("\nEnter a valid phome number")
                    u_phoneno = input("\nEnter your Phone No. : ")
                df.loc[(row_pos - 1), 'phone_no'] = u_phoneno

            elif option == "6":
                u_emailid = input("\nEnter your Email-ID: ")
                while (u_emailid.endswith(".com") == False or "@" not in u_emailid):
                    print("\nPlease enter a valid Email-ID")
                    u_emailid = input("\nEnter your Email-ID : ")
                df.loc[(row_pos - 1), 'email_id'] = u_emailid

            elif option == "7":
                u_address = input("\nEnter your address : ").title()
                df.loc[(row_pos - 1), 'address'] = u_address

            elif option == "8":
                u_fathername = input("\nEnter your Father's name : ").title()
                df.loc[(row_pos - 1), 'father_name'] = u_fathername

            elif option == "9":
                u_fatheroccupation = input(
                    "\nEnter your Father's occupation: ").title()
                df.loc[(row_pos - 1), 'father_occupation'] = u_fatheroccupation

            elif option == "10":
                u_mothername = input("\nEnter your Mother's name : ").title()
                df.loc[(row_pos - 1), 'mother_name'] = u_mothername

            elif option == "11":
                u_motheroccupation = input(
                    "\nEnter your Mother's occupation: ").title()
                df.loc[(row_pos - 1), 'mother_occupation'] = u_motheroccupation

            elif option == "12":
                a = 0
                while (a == 0):
                    ans2 = input(
                        "\nSelect your Category \n1. General\n2. SC|ST\n3. 2B\n4. 3B\nEnter option number :  ")
                    if ans2 == "1":
                        u_category = "General"
                        a = 1
                    elif ans2 == "2":
                        u_category = "SC|ST"
                        a = 1
                    elif ans2 == "3":
                        u_category = "2B"
                        a = 1
                    elif ans2 == "4":
                        u_category = "3B"
                        a = 1
                    else:
                        print("\nEnter a valid option number")

                df.loc[(row_pos - 1), 'category'] = u_category

            elif option == "13":
                ts = 0
                while ts == 0:
                    u_tenth = input("\nEnter your 10th grade marks : ")
                    if u_tenth.isdigit() == False or u_tenth in '`~!@#$%^&*()-_+={\}[]|\:;"\'<,>.?/' or int(u_tenth) > 100:
                        print("\nEnter marks ranging from 1 to 100")
                    elif u_tenth == "0":
                        ts = 1
                    elif u_tenth.isdigit():
                        ts = 1
                df.loc[(row_pos - 1), 'tenth_score'] = u_tenth

            elif option == "14":
                tws = 0
                while tws == 0:
                    u_twelve = input("\nEnter your 12th grade marks : ")
                    if u_twelve.isdigit() == False or u_twelve in '`~!@#$%^&*()-_+={\}[]|\:;"\'<,>.?/' or int(u_twelve) > 100:
                        print("\nEnter marks ranging from 1 to 100")
                    elif u_twelve == "0":
                        tws = 1
                    elif u_twelve.isdigit():
                        tws = 1

                df.loc[(row_pos - 1), 'twelveth_score'] = u_twelve

            elif option == "15":
                print("\nThis option cannot be changed")

            elif option == "16":
                print("\nThis option cannot be changed")

            elif option == "17":
                print("\nThis option cannot be changed")

            elif option == "18":
                u_achievements = input(
                    "\nEnter your achievements : ").capitalize()
                df.loc[(row_pos - 1), 'achievements'] = u_achievements

            elif option == "19":
                docs = df.loc[(row_pos - 1), 'documents']
                dictDocs = eval(docs)
                for document, status in dictDocs.items():
                    if status.strip() == "Not submitted":
                        resp = input(
                            f"Do you have your {document.strip()}? Y/N : ")
                        if resp.upper() == "Y":
                            dictDocs[document] = "Submitted"
                print("Document submission status updated")
                df.loc[(row_pos - 1), 'documents'] = str(dictDocs)

            df.to_csv("Data\\applications.csv", index=False)

    counter = 0
    while counter == 0:
        clear()
        print(" Admissions Department ".center(146, '-')+"\n")
        print("Welcome to the Admissions Department.".center(150))
        print("Please select an option to proceed.\n\n1. Apply\n2. Update your application\n3. Go back")
        ans = input("\nEnter the option number : ")
        if ans.isdigit() and ans not in "`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\" and int(ans) <= 3:
            counter = 1
        else:
            print("Invalid input")
            time.sleep(3)

    if ans == "1":
        apply()
    elif ans == "2":
        update_app()
    elif ans == "3":
        main_menu()


def idcard():
    def register():
        year = datetime.today().year
        appln_no = []
        csv_file_reader = csv.reader(
            open("C:\\Users\\2145644\\OOPSProject\\Data\\applications.csv", "r"))
        for row1 in csv_file_reader:
            appln_no.append(row1[0])

        status = 0
        while (status == 0):
            clear()
            print(" ID Card Registration ".center(146, '-'))
            appno = input("Enter 0 to back\nEnter your application number : ")
            if appno == "0":
                idcard()
            elif appno in appln_no:
                if appno.startswith(str(year)):
                    status = 1
                else:
                    print(
                        "\nApplication number is already registerd. Please go to View ID card option to see your ID card.")
                    time.sleep(5)
                    idcard()
            else:
                print(
                    "\nApplication entered is incorrect. Please enter the right application number.")
                time.sleep(5)

        print("Please wait as we retrieve your details from our database...")
        time.sleep(5)

        csv_file_reader3 = csv.reader(
            open("C:\\Users\\2145644\\OOPSProject\\Data\\applications.csv", "r"))
        details = []
        details.append(appno)
        for row in csv_file_reader3:
            if row[0] == appno:
                for i in range(1, 8):
                    if i == 3 or i == 6:
                        continue
                    details.append(row[i])
                for i in range(16, 18):
                    details.append(row[i])

        applno, fname, lname, dob, phoneno, address, stream, course = details
        name = fname + " " + lname
        a = Student(applno, name, dob, phoneno, address, stream, course)
        student_info = a.__dict__
        new_info = {}
        for i, j in student_info.items():
            key = i.replace("_Student__", "")
            if key == 'csv':
                csvFile = j
                continue
            new_info[key] = j
            data = [new_info]

            # Writing the info dictionary to a csv file.
        fields = ["appno", "reg_no", "name", "dob", "emailid",
                  "phoneno", "address", "stream", "course"]

        applnos = []
        csv_file_reader = csv.reader(open(csvFile, "r"))
        for row in csv_file_reader:
            for i in row:
                applnos.append(i)
                break

        if applno in applnos:
            print("\nApplication number is already registered. Please go to View ID Card option to see the ID card details")
            time.sleep(5)
            idcard()
        else:
            with open(csvFile, 'a', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writerows(data)
                print(f'''\n\nID card generated
----------------------------------------
Name : {a.get_name()}

Register No. : {a.get_reg_no()}

Class : {a.get_course()}

Phone : {a.get_phoneno()}

Email : {a.get_emailid()}
----------------------------------------''')
            time.sleep(20)
            main_menu()

    def view_ID():
        clear()
        print(" ID Card  ".center(146, '-'))
        print("Enter 0 to go back\n")
        print("Select your stream\n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\n5. BBA\n6. BBA in Aviation\n7. BCom\n8. BCom in Finance\n9. BCom in Tourism\n10. BA in English\n11. BA in Sociology\n12. BA in Economics")
        co = 0
        while co == 0:
            inp1 = input("Enter option number : ")
            if inp1 == "0":
                idcard()
            elif inp1 == "1":
                course = "BCA"
                co = 1
            elif inp1 == "2":
                course = "BCA in Analytics"
                co = 1
            elif inp1 == "3":
                course = "BSc(PMCS)"
                co = 1
            elif inp1 == "4":
                course = "BSc(PME)"
                co = 1
            elif inp1 == "5":
                course = "BBA"
                co = 1
            elif inp1 == "6":
                course = "BBA in Aviation"
                co = 1
            elif inp1 == "7":
                course = "BCom"
                co = 1
            elif inp1 == "8":
                course = "BCom in Finance"
                co = 1
            elif inp1 == "9":
                course = "BCom in Tourism"
                co = 1
            elif inp1 == "10":
                course = "BA in English"
                co = 1
            elif inp1 == "11":
                course = "BA in Sociology"
                co = 1
            elif inp1 == "12":
                course = "BA in Economics"
                co = 1
            else:
                print("Invalid input\n")
        print("\nEnter your current year\n1. 1st year\n2. 2nd year\n3. 3rd year")
        year = 0
        while year == 0:
            inp2 = input("Enter option number : ")
            if inp2 == "1":
                csvFile = data[course][0]
                year = 1
            elif inp2 == "2":
                csvFile = data[course][1]
                year = 1
            elif inp2 == "3":
                csvFile = data[course][2]
                year = 1
            else:
                print("\nInvalid input")

        appno = input("\nEnter your application number : ")
        csvFilereader = csv.reader(open(csvFile, "r"))
        details = []
        for row in csvFilereader:
            for i in row:
                if i == appno:
                    details = row
                    break

        if len(details) == 0:
            print(
                "Application number doesn't exist. Please enter the right application number.")
            time.sleep(5)
            idcard()
        else:
            print(f'''\n\nID card
----------------------------------------
Name : {details[2]}

Register No. : {details[1]}

Class : {details[8]}

Phone : {details[5]}

Email : {details[4]}
----------------------------------------''')
            time.sleep(20)
            idcard()

    counter = 0
    while counter == 0:
        clear()
        print(" ID Card Center ".center(146, '-'))
        print("\nPlease select an option to proceed:\n\n1. Register for ID card (For First years only)\n2. View ID card\n3. Go back\n")
        inp = input("Enter the option number : ")
        if inp.isdigit() and inp not in "`~!@#$%^&*()-_=+\{\}[]\|:;'\"<>,.?/\\" and int(inp) <= 3:
            counter = 1
        else:
            print("Invalid input\n")
            time.sleep(3)

    if inp == "1":
        register()

    elif inp == "2":
        view_ID()

    elif inp == "3":
        main_menu()


def exam():
    def check_time_table():
        clear()
        tt = 0
        print("Enter 0 to go back\nSelect your stream\n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\n5. BBA\n6. BBA in Aviation\n7. BCom\n8. BCom in Finance\n9. BCom in Tourism\n10. BA in English\n11. BA in Sociology\n12. BA in Economics")
        while tt == 0:
            stream = input("\nEnter option number: ")
            if stream == "0":
                exam()
            elif stream == "1":
                course = "BCA"
                tt = 1
            elif stream == "2":
                course = "BCA in Analytics"
                tt = 1
            elif stream == "3":
                course = "BSc(PMCS)"
                tt = 1
            elif stream == "4":
                course = "BSc(PME)"
                tt = 1
            elif stream == "5":
                course = "BBA"
                tt = 1
            elif stream == "6":
                course = "BBA in Aviation"
                tt = 1
            elif stream == "7":
                course = "Bcom"
                tt = 1
            elif stream == "8":
                course = "Bcom in Finance"
                tt = 1
            elif stream == "9":
                course = "Bcom in Tourism"
                tt = 1
            elif stream == "10":
                course = "BA in English"
                tt = 1
            elif stream == "11":
                course = "BA in Sociology"
                tt = 1
            elif stream == "12":
                course = "BA in Ettnomics"
                tt = 1
            else:
                print("Invalid input")

        print("\nEnter your current year\n1. 1st year\n2. 2nd year\n3. 3rd year")
        year = 0
        while year == 0:
            inp2 = input("Enter option number : ")
            if inp2 == "0":
                exam()
            elif inp2 == "1":
                csvFile = timeTable[course][0]
                year = 1
            elif inp2 == "2":
                csvFile = timeTable[course][1]
                year = 1
            elif inp2 == "3":
                csvFile = timeTable[course][2]
                year = 1
            else:
                print("\nInvalid input")

        csv_file_reader4 = csv.reader(open(csvFile, "r"))
        exam_code = []
        exam_name = []
        exam_type = []
        exam_date = []
        exam_duration = []
        exam_marks = []

        for rows in csv_file_reader4:
            exam_code.append(rows[0])
            exam_name.append(rows[1])
            exam_type.append(rows[2])
            exam_date.append(rows[3])
            exam_duration.append(rows[4])
            exam_marks.append(rows[5])

        print('''\n\n   Date    | Exam Code |  Exam Type  |  Exam Duration |  Total Marks  | Exam Name
--------------------------------------------------------------------------------------------''')
        for i in range(1, len(exam_code)):
            print(
                f"{exam_date[i]} |  {exam_code[i]}   |     {exam_type[i]}       |   {exam_duration[i]}   |      {exam_marks[i]}      | {exam_name[i]}                  ")
        print("\nT - Theory\nP - Practical")
        time.sleep(20)
        exam()

    def check_results():
        clear()
        re = 0
        print("Enter 0 to go back\nSelect your stream\n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\n5. BBA\n6. BBA in Aviation\n7. BCom\n8. BCom in Finance\n9. BCom in Tourism\n10. BA in English\n11. BA in Sociology\n12. BA in Economics")
        while re == 0:
            stream = input("\nEnter option number: ")
            if stream == "0":
                exam()
            elif stream == "1":
                course = "BCA"
                re = 1
            elif stream == "2":
                course = "BCA in Analytics"
                re = 1
            elif stream == "3":
                course = "BSc(PMCS)"
                re = 1
            elif stream == "4":
                course = "BSc(PME)"
                re = 1
            elif stream == "5":
                course = "BBA"
                re = 1
            elif stream == "6":
                course = "BBA in Aviation"
                re = 1
            elif stream == "7":
                course = "BCom"
                re = 1
            elif stream == "8":
                course = "BCom in Finance"
                re = 1
            elif stream == "9":
                course = "BCom in Tourism"
                re = 1
            elif stream == "10":
                course = "BA in English"
                re = 1
            elif stream == "11":
                course = "BA in Sociology"
                re = 1
            elif stream == "12":
                course = "BA in Erenomics"
                re = 1
            else:
                print("Invalid input")

        print("\nEnter your current year\n1. 1st year\n2. 2nd year\n3. 3rd year")
        year = 0
        while year == 0:
            inp2 = input("Enter option number : ")
            if inp2 == "0":
                exam()
            elif inp2 == "1":
                csvFile = results[course][0]
                year = 1
            elif inp2 == "2":
                csvFile = results[course][1]
                year = 1
            elif inp2 == "3":
                csvFile = results[course][2]
                year = 1
            else:
                print("\nInvalid input")
        register_no = input("\nEnter your register number: ")

        csv_file_reader5 = csv.reader(open(csvFile, "r"))
        subjects = []
        for row in csv_file_reader5:
            subjects = row
            break

        marks = []
        for row in csv_file_reader5:
            if register_no == "0":
                exam()
            elif row[0] == register_no:
                marks = row
                break

        if len(marks) == 0:
            print("\nRegisted Number doesn't exist.")
            time.sleep(10)
            exam()

        result = Result(subjects, marks)
        detailedInfo = result.get_subjectsAndScoredMarks()
        totalMarksList = result.get_total_marks_list()
        totalMarks = result.get_total_marks()
        scoredMarks = result.get_scoredMarks()
        result.calculateNGrade()
        percentage = result.get_percentatage()
        grade = result.get_grade()

        index = 0
        clear()
        print("Your Result".center(133, "-"))
        print("\n{:<40} {:<21} {:<23} {}".format(
            'Subject', 'Marks Scored', 'Total Marks', 'Result'))
        print("------------------------------------------------------------------------------------------------------------------------------")
        for s, ms in detailedInfo.items():
            print("{:<45} {:<20} {:<20} {}".format(
                s, ms[0], totalMarksList[index], ms[1]))
            index += 1
        print("\nTotal Marks Scored - {} / {}".format(scoredMarks, totalMarks))
        print("\nPercentage - {}".format(percentage))
        print("\nGrade - {}".format(grade))
        time.sleep(30)
        exam()

    status = 0
    while status == 0:
        clear()
        print("Examination Section".center(133, '-'))
        print("Please select an option to proceed. \n\n1. Examination Time Table\n2. Check results\n3. Go back")
        ans = input("\nEnter the option number : ")
        if ans == "1":
            check_time_table()
        elif ans == "2":
            check_results()
        elif ans == "3":
            main_menu()
        else:
            print("Invalid input")
            time.sleep(3)


def attendence():
    clear()
    print(" Attendence Page ".center(133, '-'))
    at = 0
    print("Enter 0 to go back\nSelect your stream\n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\n5. BBA\n6. BBA in Aviation\n7. BCom\n8. BCom in Finance\n9. BCom in Tourism\n10. BA in English\n11. BA in Sociology\n12. BA in Economics")
    while at == 0:
        stream = input("\nEnter option number: ")
        if stream == "0":
            main_menu()
        elif stream == "1":
            course = "BCA"
            at = 1
        elif stream == "2":
            course = "BCA in Analytics"
            at = 1
        elif stream == "3":
            course = "BSc(PMCS)"
            at = 1
        elif stream == "4":
            course = "BSc(PME)"
            at = 1
        elif stream == "5":
            course = "BBA"
            at = 1
        elif stream == "6":
            course = "BBA in Aviation"
            at = 1
        elif stream == "7":
            course = "BCom"
            at = 1
        elif stream == "8":
            course = "BCom in Finance"
            at = 1
        elif stream == "9":
            course = "BCom in Tourism"
            at = 1
        elif stream == "10":
            course = "BA in English"
            at = 1
        elif stream == "11":
            course = "BA in Sociology"
            at = 1
        elif stream == "12":
            course = "BA in Eatnomics"
            at = 1
        else:
            print("Invalid input")
    print("\nEnter your current year\n1. 1st year\n2. 2nd year\n3. 3rd year")
    year = 0
    while year == 0:
        inp2 = input("Enter option number : ")
        if inp2 == "0":
            main_menu()
        elif inp2 == "1":
            csvFile = attendance[course][0]
            year = 1
        elif inp2 == "2":
            csvFile = attendance[course][1]
            year = 1
        elif inp2 == "3":
            csvFile = attendance[course][2]
            year = 1
        else:
            print("\nInvalid input")

    register_no = input("\nEnter your register number: ")
    csv_file_reader6 = csv.reader(open(csvFile, "r"))

    noOfClasses = []
    for row in csv_file_reader6:
        if register_no == "0":
            main_menu()
        elif row[0] == register_no:
            noOfClasses = row
            break

    if len(noOfClasses) == 0:
        print("\nRegisted Number doesn't exist.")
        time.sleep(10)
        main_menu()
    else:
        noOfClasses.pop(0)
        presentDays = noOfClasses[0]
        absentDays = noOfClasses[1]
        totalNoOfDays = noOfClasses[2]
    clear()
    print("Your Attendance".center(146, "-"))
    print("\n{:<20} {:<20} {:<23}".format(
        'Present Days', 'Absent Days', 'Total No. of Days'))
    print("-----------------------------------------------------------")
    print("{:<20} {:<20} {:<23}".format(
        presentDays, absentDays, totalNoOfDays))
    percentage = int(presentDays) / int(totalNoOfDays) * 100
    print("\nPercentage - {}".format(percentage))
    if percentage >= 85:
        print("\nAttendance percentage is maintained.")
    elif percentage < 85 and percentage > 75:
        print("\nPlease maintain your attendance percentage to avoid remidial classes.")
    elif percentage < 75:
        print("\nAttendance percentage doesn't meet the eligiblility criteria to appear for examinations.")
    time.sleep(20)
    main_menu()


def library():
    def borrow():
        clear()
        print("Welcome to our Library".center(100, "-"))
        l1 = 0
        print("Enter 0 to go back\nSelect your stream\n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\n5. BBA\n6. BBA in Aviation\n7. BCom\n8. BCom in Finance\n9. BCom in Tourism\n10. BA in English\n11. BA in Sociology\n12. BA in Economics")
        while l1 == 0:
            stream = input("\nEnter option number: ")
            if stream == "0":
                main_menu()
            elif stream == "1":
                course = "BCA"
                l1 = 1
            elif stream == "2":
                course = "BCA in Analytics"
                l1 = 1
            elif stream == "3":
                course = "BSc(PMCS)"
                l1 = 1
            elif stream == "4":
                course = "BSc(PME)"
                l1 = 1
            elif stream == "5":
                course = "BBA"
                l1 = 1
            elif stream == "6":
                course = "BBA in Aviation"
                l1 = 1
            elif stream == "7":
                course = "BCom"
                l1 = 1
            elif stream == "8":
                course = "BCom in Finance"
                l1 = 1
            elif stream == "9":
                course = "BCom in Tourism"
                l1 = 1
            elif stream == "10":
                course = "BA in English"
                l1 = 1
            elif stream == "11":
                course = "BA in Sociology"
                l1 = 1
            elif stream == "12":
                course = "BA in Eatnomics"
                l1 = 1
            else:
                print("Invalid input")
        print("\nEnter your current year\n1. 1st year\n2. 2nd year\n3. 3rd year")
        year = 0
        while year == 0:
            inp2 = input("Enter option number : ")
            if inp2 == "0":
                library()
            elif inp2 == "1":
                csvFile = data[course][0]
                year = 1
            elif inp2 == "2":
                csvFile = data[course][1]
                year = 1
            elif inp2 == "3":
                csvFile = data[course][2]
                year = 1
            else:
                print("\nInvalid input")

        regNo = input("\nEnter your Register Number : ")
        csv_file_reader6 = csv.reader(open(csvFile, "r"))
        for row in csv_file_reader6:
            if row[1] == regNo:
                break
        else:
            print("\nRegister Number doesn't exist.")
            time.sleep(5)
            borrow()

        bookNo = input("\nEnter the book ISBN Number : ")
        print("\nPlease wait as we process your request...")
        time.sleep(5)
        csv_file_reader7 = csv.reader(open("library/library.csv", "r"))
        booksTaken = []
        for row in csv_file_reader7:
            booksTaken.append(row[1])
        if bookNo not in booksTaken:
            libBor = Library(regNo, bookNo)
            if libBor.bookName == None:
                print("\nEntered Book number is wrong. Please re-check.")
                time.sleep(5)
                library()
            else:
                libBor.enterData()
                print("\nPlease note the details given below")
                print("\n\nRegister Number : {}\nBook ISBN Number : {}\nBook Name : {}\nBorrow Date : {}\nReturn Date : {}".format(
                    libBor.regNo, libBor.bookNo, libBor.bookName, libBor.borrowDate, libBor.returnDate))
                print("\nDo return the book before due date to avoid late fee charges. Thank you for availing the library services. Do visit next time.")
                time.sleep(10)
                library()
        else:
            print("\nBook is already been taken by other student.")
            time.sleep(5)
            library()

    def returnBook():
        clear()
        l2 = 0
        print("Enter 0 to go back\nSelect your stream\n1. BCA\n2. BCA in Analytics\n3. BSc(PMCS)\n4. BSc(PME)\n5. BBA\n6. BBA in Aviation\n7. BCom\n8. BCom in Finance\n9. BCom in Tourism\n10. BA in English\n11. BA in Sociology\n12. BA in Economics")
        while l2 == 0:
            stream = input("Enter option number : ")
            if stream == "0":
                library()
            elif stream == "1":
                course = "BCA"
                l2 = 1
            elif stream == "2":
                course = "BCA in Analytics"
                l2 = 1
            elif stream == "3":
                course = "BSc(PMCS)"
                l2 = 1
            elif stream == "4":
                course = "BSc(PME)"
                l2 = 1
            elif stream == "5":
                course = "BBA"
                l2 = 1
            elif stream == "6":
                course = "BBA in Aviation"
                l2 = 1
            elif stream == "7":
                course = "BCom"
                l2 = 1
            elif stream == "8":
                course = "BCom in Finance"
                l2 = 1
            elif stream == "9":
                course = "BCom in Tourism"
                l2 = 1
            elif stream == "10":
                course = "BA in English"
                l2 = 1
            elif stream == "11":
                course = "BA in Sociology"
                l2 = 1
            elif stream == "12":
                course = "BA in Economics"
                l2 = 1
            else:
                print("Invalid input")
        year = 0
        print("\nEnter your current year\n1. 1st year\n2. 2nd year\n3. 3rd year")
        while year == 0:
            inp2 = input("Enter option number : ")
            if inp2 == "0":
                library()
            elif inp2 == "1":
                csvFile = data[course][0]
                year = 1
            elif inp2 == "2":
                csvFile = data[course][1]
                year = 1
            elif inp2 == "3":
                csvFile = data[course][2]
                year = 1
            else:
                print("\nInvalid input")

        regNo = input("\nEnter your Register Number : ")
        csv_file_reader6 = csv.reader(open(csvFile, "r"))
        for row in csv_file_reader6:
            if row[1] == regNo:
                break
        else:
            print("\nRegister Number doesn't exist.")
            time.sleep(5)
            library()

        bookNo = input("\nEnter the book ISBN number : ")
        csv_file_reader6 = csv.reader(open("library\libraryBooks.csv", "r"))
        for row in csv_file_reader6:
            if row[0] == bookNo:
                break
        else:
            print(f"\nBook with ISBN number {bookNo} doesn't exist.")
            time.sleep(5)
            library()

        csv_file_reader7 = csv.reader(open("library\library.csv"))
        for row in csv_file_reader7:
            if row[0] == regNo and row[1] == bookNo:
                libRet = Library(regNo, row[1])
                borrowDate = datetime.strptime(row[3], "%Y-%m-%d")
                returnDate = datetime.strptime(row[4], "%Y-%m-%d")
                libRet.setBorrowDate(borrowDate)
                libRet.setReturnDate(returnDate)
                libRet.calculateDays()
                library()
        else:
            print("\nWe cannot find any record of your Register Number. Please re-check.")
            time.sleep(5)
            library()

    clear()
    print(" Library Center ".center(133, '-'))
    print("Please select an option to proceed\n\n1. Borrow a book\n2. Return a book\n3. Go back")
    lib = 0
    while lib == 0:
        resp = input("\nEnter the option number : ")
        if resp == "1":
            lib = 1
            borrow()
        elif resp == "2":
            lib = 1
            returnBook()
        elif resp == "3":
            lib = 1
            main_menu()
        else:
            print("\nInvalid input")
            time.sleep(2)


def coCurricular():
    clear()
    print("Events".center(130, "-"))
    print("\nHere's a list of upcoming events in college")
    print("\n{:<30} {:<40} {:<13} {:<18} {}".format(
        'Event Name', 'Event Location', 'Event Date', 'Event Timings', 'Event Coordinators'))
    print("------------------------------------------------------------------------------------------------------------------------------")
    csvFilereader = csv.reader(open("coCurricular\coCurricularList.csv", "r"))
    i = 1
    for row in csvFilereader:
        if i == 1:
            i += 1
            continue
        else:
            print("{:<30} {:<40} {:<13} {:<18} {}".format(
                row[0], row[1], row[2], row[3], row[4]))

    time.sleep(20)


def update_data():
    current = datetime.now()
    u_month = current.month
    u_date = current.day
    if u_month == 2 and u_date == 8:

        # Updating the count.txt files which contain counts of student in each course.
        for i in count:
            with open(i, 'w') as w:
                w.write("1")

        # Updating the total number of seats available to full capacity.
        filename = "C:\\Users\\2145644\\OOPSProject\\Data\\seat_count.csv"
        f = open(filename, "w+")
        f.close()

        columns = ["BCA", "BCA(Analytics)", "BSC(PMCS),", "BSC(PME)", "BBA", "BBA(Aviation)", "Bcom",
                   "Bcom(Finance)", "Bcom(Tourism)", "BA in English", "BA in Sociology", "BA in Economics"]
        updated_seat_count = [100, 70, 60, 60,
                              100, 70, 100, 70, 70, 70, 70, 70]

        with open("C:\\Users\\2145644\\OOPSProject\\Data\\seat_count.csv", "a", newline="") as fp:
            wr = writer(fp)
            wr.writerow(columns)
            wr.writerow(updated_seat_count)

        # Shifting data from year to year csv file
        for stream in data.keys():
            first = data[stream][0]
            second = data[stream][1]
            third = data[stream][2]

            # Opening third year csv file and deleting the existing data and copying the data from second year csv file
            f = open(third, "w+")
            f.close()

            with open(second, "r") as r:
                lines = r.readlines()

            with open(third, 'a') as w:
                w.writelines(lines)

            # Opening second year csv file and deleting the existing data and copying the data from first year csv file
            f = open(second, "w+")
            f.close()

            with open(first, "r") as r:
                lines = r.readlines()

            with open(second, 'a') as w:
                w.writelines(lines)

            # Deleting the existing data and adding data of new applicants
            f = open(first, "w+")
            f.close()

            List = ["appno", "reg_no", "name", "dob", "emailid",
                    "phoneno", "address", "stream", "course"]

            with open(first, "a") as w:
                writer_object = writer(w)
                writer_object.writerow(List)
                w.close()


update_data()
main_menu()
