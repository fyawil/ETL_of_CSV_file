import csv
from datetime import datetime

cleaned_employee_data = []

with open("employees.csv") as csv_file:

    non_cleaned_employee_data_list = list(csv.reader(csv_file))
    for i, line in enumerate(non_cleaned_employee_data_list):

        new_clean_line = line
        
        if "Femae" in line[5]:        
            new_clean_line[5] = "Female"

        if line[-1] != "" and i != 0:
            hire_date_string = line[-6]
            date_format = '%d/%m/%Y'
            hire_date = datetime.strptime(hire_date_string, date_format).date()

            exit_date_string = line[-1]
            exit_date = datetime.strptime(exit_date_string, date_format).date()

        if  line[-1] != "" and i != 0 and hire_date > exit_date:
                continue

        if line in cleaned_employee_data:
            continue    

        cleaned_employee_data.append(new_clean_line)

with open("cleaned_employees.csv", "w", newline="") as cleaned_csv_file:
    
    csv_writer = csv.writer(cleaned_csv_file)
    csv_writer.writerows(cleaned_employee_data)