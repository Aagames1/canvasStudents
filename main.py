from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
API_URL = "https://example.com"
API_KEY = "p@$$w0rd" 
canvas = Canvas(API_URL, API_KEY)

def getStudents(courseID):
  course = canvas.get_course(courseID)
  users = course.get_users(enrollment_type=['student'])
  studentsList = []
  
  for user in users:
    studentsList.append(user)
    
  return studentsList


print("Enter the course ID of the course you want to obtain a list of all students from: ")
ID = input()

try:
    getStudents(ID)
except CanvasException as e:
    print("An error has occured. Check to see if the ID was valid.")
