from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
API_URL = "https://mcpsmd.instructure.com/"
API_KEY = "[insert key here]" # obviously needs to be changed when used
canvas = Canvas(API_URL, API_KEY)

def getStudents(courseID):
  course = canvas.get_course(courseID)
  users = course.get_users(enrollment_type=['student'])
  studentsList = []
  
  for user in users:
    studentsList.append(user.name)
    
  return studentsList


# this part will likely be changed to eliminate the need for manual input
print("Enter the course ID of the course you want to obtain a list of all students from: ")
ID = input()

try:
    print(getStudents(ID))
except CanvasException as e:
    print("An error has occured. Check to see if the ID was valid.")

