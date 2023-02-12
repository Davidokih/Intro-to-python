def compute_grade(points):
  check = 100
  if points >= 70:
    return "A"
  elif points >= 50:
    return "B"
  elif points >= 30:
    return "C"
  elif points >= 0:
    return "F"
  
compute_grade(39)

def student_grade(name, point):
  grade = compute_grade(point)
  myPoint = str(point)
  result = name + " scored " + myPoint + "/100 points in Chemistry and got the grade " + grade
  return result

student_grade("Zach",51)

#Creat a text file for Zach's report card and write the message inside
report_card = open("zach_report.txt","w")

report_card.write(student_grade("Zach",51))
report_card.close()

#Check if there is already a report card for Sophie and print a message in case there is
try:
  report_card = open("sophie_report.txt","r")
  report_card.read()
  report_card.close()
#If there is none, create one and write the message inside
except:
  report_card = open("sophie_report.txt","w")
  report_card.write(student_grade("Sophie",78))
  report_card.close()

#Define a function that takes the student name and the points as an argument and returns them as specified in the instructions
def student_grade(name, point):
  try:

  #return name:grade
    grade = compute_grade(point)
    myPoint = str(point)
    return name +" : "+ grade

  #or return a message if the student was missing
  except:
    return (name + " was not present")

#Run the list of all students and their points
student_list = [('Zach', 51), ('Sophie', 78), ('Fred', 29), ('Belina','missing'), ('Markus','missing')]

#Write a for loop to access each student one at a time and unpack the tuple
for element in student_list:
  names, points = element
  #print the message returned by student_grade
  print(student_grade(names,points))

#Create the grades.txt file
student_grade_file = open("grades.txt","w")

#Use the for loop to write the name and grade of each student in the file 
for element in student_list:
  names,points = element
  grades = student_grade(names,points)
  #Write the message returned by student_grade into the file
  student_grade_file.write(grades + "\n")

#Close the file
student_grade_file.close()