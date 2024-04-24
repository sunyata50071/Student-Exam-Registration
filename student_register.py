# This program makes a registration form for student exams.

# Get the number of students to be registered.
num_of_students = int(input("\nHow many students are registering?"))

# Ask ID for every student then write each to a file alongside space to sign. 
for i in range(num_of_students):
    student_id_num = input("Enter student ID number: ")
    with open("reg_form.txt", "a+", encoding="utf-8") as file:
            file.write("Student ID: " + student_id_num + ".............." + "\n")

# Leave loop. Add space for necessary exam details on the form.
with open("reg_form.txt", "a+", encoding="utf-8") as file:
      file.write("\nEXAM VENUE: ")
      file.write("\nCOURSE NAME: ")
      file.write("\nEXAM INVIGILATOR/S: ")
      file.write("\nDATE: ")
      
print("\nThe exam registration form is ready for printing. Go to the file.")
                  