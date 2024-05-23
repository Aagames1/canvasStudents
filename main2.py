from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
API_URL = "https://mcpsmd.instructure.com/"
API_KEY = "[INSERT KEY HERE]" 
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
  print("\nEnter the course ID of the course you want to obtain a list of all students from: ")
  ID = input()

  try:
    nameList = getStudents(ID)
    
    with open('output.txt', 'w') as file:
      for item in nameList:
          file.write('%s\n' % item)
        
    print("\nStudent Data Saved!")
    exit()
  
  except CanvasException as e:
    print("\nAn error has occured. Check to see if the ID and API Key were valid.")
    exit()

