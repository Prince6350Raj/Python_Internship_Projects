import pandas as pd
import numpy as np
def get_user_input():
    students = []
    grades = []
    
    while True:
        choice = input("Choose an option (1: Add Student, 2: Add Grades, 3: Calculate GPA, 4: Stop): ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            students.append({'Student ID': student_id, 'Name': name})
        
        elif choice == '2':
            student_id = input("Enter student ID: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade for {}: ".format(subject)))
            grades.append({'Student ID': student_id, 'Subject': subject, 'Grade': grade})
        
        elif choice == '3':
            student_df = pd.DataFrame(students)
            grades_df = pd.DataFrame(grades)
            merged_df = pd.merge(student_df, grades_df, on='Student ID')
            
            gpa_df = merged_df.groupby('Student ID')['Grade'].mean().reset_index()
            gpa_df = gpa_df.rename(columns={'Grade': 'GPA'})
            
            print("\nStudent GPA:")
            print(gpa_df)
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    return pd.DataFrame(students), pd.DataFrame(grades)
if __name__ == "__main__":
    students_df, grades_df = get_user_input()
