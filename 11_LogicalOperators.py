# if applicant has high income AND good credit they are Eligible for a loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
        print("Eligible for loan")

# if applicant has high income OR good credit they are Eligible for a loan
has_higher_income = True
has_gooder_credit = False

if has_higher_income or has_gooder_credit:
        print("Eligibler for loan")

#if the applicant has good credit And doesn't have a criminal record they are eligible for a loan
has_highest_income = True
has_criminal_record = False

if has_highest_income and not has_criminal_record:
    print("Eligiblest for loan")


#AND:   both
#OR:    at leas one
#Not:   check for False Bolean