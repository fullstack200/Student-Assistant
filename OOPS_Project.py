# Python program that provides various functionalities which a college requires using OOPS concepts.
from select import select
import pandas as pd
import datetime
import csv
import time
# Admission class


class Admission:
    '''Admission class is the class which handles the process of admission of a student based on the eligibity criteria'''
    with open("C:\\Users\\2145644\\OOPS Project\\counts\\appln_count.txt", 'r') as f:
        counter = int(f.read())

    # Courses available in college.
    df = pd.read_csv("C:\\Users\\2145644\\OOPS Project\\Data\\seat_count.csv")
    courses = {"Science": [["BCA", df.loc[0][0], 100000], ["BCA in Analytics", df.loc[0][1], 120000], ["BSc(PMCS)", df.loc[0][2], 80000], ["BSc(PME)", df.loc[0][3], 80000]], "Commerce": [["BBA", df.loc[0][4], 100000], ["BBA in Aviation", df.loc[0][5], 120000], [
        "BCom", df.loc[0][6], 80000], ["BCom in Finance", df.loc[0][7], 100000], ["BCom in Tourism", df.loc[0][8], 100000]], "Arts": [["BA in English", df.loc[0][9], 80000], ["BA in Sociology", df.loc[0][10], 80000], ["BA in Economics", df.loc[0][11], 80000]]}

    def __init__(self, first_name, last_name, gender, dob, phone_no, email_id, address, father_name, father_occupation, mother_name, mother_occupation, category, tenth_score, twelveth_score, previous_stream, stream_opting_for, course_opting_for, achievements):
        # Personal details
        current = datetime.date.today()
        current_year = current.year
        self.__appno = str(current_year) + "APPLN" + str(Admission.counter)
        with open("C:\\Users\\2145644\\OOPS Project\\counts\\appln_count.txt", 'w') as f:
            Admission.counter += 1
            f.write(str(Admission.counter))

        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__dob = dob
        self.__phone_no = phone_no
        self.__email_id = email_id
        self.__address = address
        self.__father_name = father_name
        self.__father_occupation = father_occupation
        self.__mother_name = mother_name
        self.__mother_occupation = mother_occupation
        self.__category = category

        # Education details
        self.__tenth_score = tenth_score
        self.__twelveth_score = twelveth_score
        self.__previous_stream = previous_stream
        self.__stream_opting_for = stream_opting_for
        self.__course_opting_for = course_opting_for
        self.__achievements = achievements
        self.__status = None

        # Documents details
        self.__documents = {"10th_marks_card": None, "12th_marks_card": None,
                            "Aadhar_Card": None, "Code_of_conduct": None, "Transfer_certificate": None}

    # GET methods
    def get_app_no(self):
        return self.__appno

    def get_name(self):
        return self.__first_name + " " + self.__last_name

    def get_gender(self):
        return self.__gender

    def get_dob(self):
        return self.__dob

    def get_phone_no(self):
        return self.__phone_no

    def get_email_id(self):
        return self.__email_id

    def get_address(self):
        return self.__address

    def get_father_name(self):
        return self.__father_name

    def get_father_occupation(self):
        return self.__father_occupation

    def get_mother_name(self):
        return self.__mother_name

    def get_mother_occupation(self):
        return self.__mother_occupation

    def get_category(self):
        return self.__category

    def get_tenth_score(self):
        return self.__tenth_score

    def get_twelveth_score(self):
        return self.__twelveth_score

    def get_previous_stream_compelted(self):
        return self.__previous_stream

    def get_stream_opting_for(self):
        return self.__stream_opting_for

    def get_course_opting_for(self):
        return self.__course_opting_for

    def get_achievements(self):
        return self.__achievements

    def get_status(self):
        return self.__status

    def get_documents(self):
        return self.__documents

    # SET methods

    def set_fname(self, fname):
        self.__first_name = fname

    def set_lname(self, lname):
        self.__last_name = lname

    def set_gender(self, gender):
        self.__gender = gender

    def set_dob(self, dob):
        self.__dob = dob

    def set_phone_no(self, phoneno):
        self.__phone_no = phoneno

    def set_email_id(self, emailid):
        self.__email_id = emailid

    def set_address(self, address):
        self.__address = address

    def set_father_name(self, fathername):
        self.__father_name = fathername

    def set_father_occupation(self, fatheroccupation):
        self.__father_occupation = fatheroccupation

    def set_mother_name(self, mothername):
        self.__mother_name = mothername

    def set_mother_occupation(self, motheroccupation):
        self.__mother_occupation = motheroccupation

    def set_category(self, category):
        self.__category = category

    def set_tenth_score(self, tenthscore):
        self.__tenth_score = tenthscore

    def set_twelve_score(self, twelvescore):
        self.__twelveth_score = twelvescore

    def set_previous_stream(self, previousstream):
        self.__previous_stream = previousstream

    def set_opting_stream(self, optingstream):
        self.__stream_opting_for = optingstream

    def set_opting_course(self, optingcourse):
        self.__course_opting_for = optingcourse

    def set_achievements(self, achievements):
        self.__achievements = achievements

    def set_status(self, status):
        self.__status = status

    def set_documents(self, doc):
        self.__documents = doc

    # Checking if seats are available.
    def check_course_availability(self):
        status = 0
        stream_opted = self.__stream_opting_for
        course_opted = self.__course_opting_for
        for stream, course in Admission.courses.items():
            if stream != stream_opted:
                continue
            for course_name, seats, fee in course:
                if course_name == course_opted:
                    status = 1
                    if seats != 0:
                        return True
                    else:
                        return "Unfortunately, seats are not available."
                else:
                    continue
        if status == 0:
            return "Unfortunately, course you're looking for is not available."

    # Checking eligibility of the student based on his marks, previous stream and category.
    def check_eligibility(self):
        '''This function checks the eligibility of a student based on the course he/she has completed and the marks he has scored in his previous grade and the category he belongs to.'''
        marks_scored = self.get_twelveth_score()
        previous_stream = self.get_previous_stream_compelted()
        category = self.get_category()

        if previous_stream == "Science":
            if category == "General" and int(marks_scored) > 80:
                return True
            elif category == "SC|ST" or category == "2A" or category == "2B" or category == "3B":
                if int(marks_scored) > 70:
                    return True
                else:
                    return "Unfortunately, you are not eligible for this course based on the marks you have scored in your previous grade."

        elif previous_stream == "Commerce":
            if category == "General" and int(marks_scored) > 80:
                return True
            elif category == "SC|ST"  or category == "2A"  or category == "2B"  or category == "3B":
                if int(marks_scored) > 70:
                    return True
                else:
                    return "Unfortunately, you are not eligible for this course based on the marks you have scored in your previous grade."

        elif previous_stream == "Arts":
            if category == "General" and int(marks_scored) > 80:
                return True
            elif category == "SC|ST" or category == "2A" or category == "2B" or category == "3B":
                if int(marks_scored) > 70:
                    return True
                else:
                    return "Unfortunately, you are not eligible for this course based on the marks you have scored in your previous grade."
    

    # Collects documents input from the user.
    def document_submission(self):
        documents = self.get_documents()
    
        counter1 = 0
        while counter1 == 0:
            tenth_marks_card = input("\nDo you have your 10th marks card? Y/N - ")
            if tenth_marks_card.upper() == "Y":
                documents["10th_marks_card"] = "Submitted"
                counter1 = 1
            elif tenth_marks_card.upper() == "N":
                documents["10th_marks_card"] = "Not submitted"
                counter1 = 1
            else:
                print("\nInvalid input")
        counter2 = 0
        while counter2 == 0:
            twelveth_marks_card = input("\nDo you have your 12th marks card? Y/N - ")
            if twelveth_marks_card.upper() == "Y":
                documents["12th_marks_card"] = "Submitted"
                counter2 = 1
            elif twelveth_marks_card.upper() == "N":
                documents["12th_marks_card"] = "Not submitted"
                counter2 = 1
            else:
                print("\nInvalid input")
        counter3 = 0
        while counter3 == 0:
            aadhar_card = input("\nDo you have your Aadhar card? Y/N - ")
            if aadhar_card.upper() == "Y":
                documents["Aadhar_Card"] = "Submitted"
                counter3 = 1
            elif aadhar_card.upper() == "N":
                documents["Aadhar_Card"] = "Not submitted"
                counter3 = 1
            else:
                print("\nInvalid input")
        counter4 = 0
        while counter4 == 0:
            code_of_conduct = input("\nDo you have your code_of_conduct? Y/N - ")
            if code_of_conduct.upper() == "Y":
                documents["Code_of_conduct"] = "Submitted"
                counter4 = 1
            elif code_of_conduct.upper() == "N":
                documents["Code_of_conduct"] = "Not submitted"
                counter4 = 1
            else:
                print("\nInvalid input")
        counter5 = 0
        while counter5 == 0:
            transfer_cert = input("\nDo you have your transfer certificate? Y/N - ")
            if transfer_cert.upper() == "Y":
                documents["Transfer_certificate"] = "Submitted"
                counter5 = 1
            elif transfer_cert.upper() == "N":
                documents["Transfer_certificate"] = "Not submitted"
                counter5 = 1
            else:
                print("\nInvalid input")
        
        return documents

    # Collects fee payement input from the user.
    def fee_payment(self):
        fee_to_be_paid = 0
        df = pd.read_csv("C:\\Users\\2145644\\OOPS Project\\Data\\seat_count.csv")

        course_info = Admission.courses
        course_opted = self.get_course_opting_for()
        for stream, courses in course_info.items():
            for course_name, seats, fee in courses:
                if course_name == course_opted:
                    fee_to_be_paid = fee
                    counter = 0
                    while counter == 0:
                        answer = input(
                            f"\nPlease pay the {fee_to_be_paid} amount to get your admission done. Enter Y to complete the process - ")
                        if answer.upper() == "Y":
                            seats -= 1
                        # Reducing seat count by one after the completition of admission process.
                            if course_opted == "BCA":
                                df.loc[0][0] = seats
                            elif course_opted == "BCA with Analytics":
                                df.loc[0][1] = seats
                            elif course_opted == "BSc(PMCS)":
                                df.loc[0][2] = seats
                            elif course_opted == "BSc(PME)":
                                df.loc[0][3] = seats
                            elif course_opted == "BBA":
                                df.loc[0][4] = seats
                            elif course_opted == "BBA in Aviation":
                                df.loc[0][5] = seats
                            elif course_opted == "BCom":
                                df.loc[0][6] = seats
                            elif course_opted == "BCom in Finance":
                                df.loc[0][7] = seats
                            elif course_opted == "BCom in Tourism":
                                df.loc[0][8] = seats
                            elif course_opted == "BA in English":
                                df.loc[0][9] = seats
                            elif course_opted == "BA in Sociology":
                                df.loc[0][10] = seats
                            elif course_opted == "BA in Economics":
                                df.loc[0][11] = seats
                            counter = 1
                        else:
                            print("\nInvalid input")
                        df.to_csv("C:\\Users\\2145644\\OOPS Project\\Data\\seat_count.csv", index=False)
                    

# Student class
class Student():
    '''Create Student ID based on the details collected in application.'''
    def __init__(self,appno,name,dob,phoneno,address,stream,course):
        if course == "BCA":
           txtFile = "counts\\bca.txt"
           csvFile = "Data\\f_bca.csv"
           initial = "BCA"
        elif course == "BCA in Analytics":
            txtFile = "counts\\bca_in_analytics.txt"
            csvFile = "Data\\f_bca_ana.csv"
            initial = "BCAAN"
        elif course == "BSc(PMCS)":
            txtFile = "counts\\bscpmcs.txt"
            csvFile = "Data\\f_bsc(pmcs).csv"
            initial = "BSCPMCS"
        elif course == "BSc(PME)":
            txtFile = "counts\\bscpme.txt"
            csvFile = "Data\\f_bsc(pme).csv"
            initial = "BSCPME"
        elif course == "BBA":
            txtFile = "counts\\bba.txt"
            csvFile = "Data\\f_bba.csv"
            initial = "BBA"
        elif course == "BBA in Aviation":
            txtFile = "counts\\bba_aviation.txt"
            csvFile = "Data\\f_bba_ava.csv"
            initial = "BBAAV"
        elif course == "BCom":
            txtFile = "counts\\bcom.txt"
            csvFile = "Data\\f_bcom.csv"
            initial = "BCOM"
        elif course == "BCom in Finance":
            txtFile = "counts\\bcom_finance.txt"
            csvFile = "Data\\f_bcom_fin.csv"
            initial = "BCOMFI"
        elif course == "BCom in Tourism":
            txtFile = "counts\\bcom_tourism.txt"
            csvFile = "Data\\f_bcom_tou.csv"
            initial = "BCOMTU"
        elif course == "BA in English":
            txtFile = "counts\\ba_english.txt"
            csvFile = "Data\\f_ba_eng.csv"
            initial = "BAENG"
        elif course == "BA in Economics":
            txtFile = "counts\\ba_economics.txt"
            csvFile = "Data\\f_ba_eco.csv"
            initial = "BAECO"
        elif course == "BA in Sociology":
            txtFile = "counts\\ba_sociology.txt"
            csvFile = "Data\\f_ba_soc.csv"
            initial = "BASOC"
        
        with open(txtFile, 'r') as r:
            count = r.read()
            year = datetime.date.today().year
            self.__reg_no = str(year)[2] + str(year)[3] + initial + count
        
        with open(txtFile,'w') as w:
           count = str(int(count) + 1)
           w.write(count)

        self.__appno = appno 
        self.__name = name
        self.__dob = dob
        self.__emailid = self.__reg_no + "@kristujayanti.com"
        self.__phoneno = phoneno
        self.__address = address
        self.__stream = stream
        self.__course = course
        self.__csv = csvFile

    #GET methods
    def get_appno(self):
        return self.__appno

    def get_reg_no(self):
        return self.__reg_no

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob
    
    def get_emailid(self):
        return self.__emailid

    def get_phoneno(self):
        return self.__phoneno
    
    def get_address(self):
        return self.__address

    def get_stream(self):
        return self.__stream
        
    def get_course(self):
        return self.__course

    def display_ID(self):
        pass




    