from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
import time
# to be used
API_URL = "https://mcpsmd.instructure.com/"
API_KEY = "[API_KEY HERE]" 
canvas = Canvas(API_URL, API_KEY)

def getStudents(courseID):
  course = canvas.get_course(courseID)
  users = course.get_users(enrollment_type=['student'])
  studentsList = []
  
  for user in users:
    name = user.name
    name = name[:-10]
    studentsList.append(name)
    
  return studentsList


while True:
  print("Enter the course ID of the course you want to obtain a list of all students from: ")
  ID = input()

  try:
    nameList = getStudents(ID)
    print("Student Data Saved!")
    print("Input '1' to print the list. Input '2' to convert the list to a .txt file. Input anything else to end the program.")
    x = input()
    if(x == "1"):
      print(nameList)
    elif (x == "2"):
      with open('output.txt', 'w') as file:
        for item in nameList:
            file.write('%s\n' % item)
    else:
      exit()
  
  except CanvasException as e:
    print("An error has occured. Check to see if the ID and API Key were valid.")

