from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
import time
API_URL = "https://mcpsmd.instructure.com/"
API_KEY = "2873~KtJk8NXGQ9uL8chnTCT7xtJk88ZWUuWUKMN6zkxWXcTPTuZBQENuhU3mBQxttwrA" 
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

def getCourseName(courseID):
  course = canvas.get_course(courseID)
  return course.name

while True:
  print("\nEnter the course ID of the course you want to obtain a list of all students from: ")
  ID = input()

  try:
    nameList = getStudents(ID)
    
    with open('output.txt', 'w') as file:
      file.write(getCourseName(ID))
      file.write('\n')
      for item in nameList:
          file.write('%s\n' % item)
        
    print("\nStudent Data Saved!")
    exit()
  
  except CanvasException as e:
    print("\nAn error has occured. Check to see if the ID and API Key were valid.")
    exit()

