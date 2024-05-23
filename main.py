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
    print("\nStudent Data Saved!")
    print("\nInput '1' to convert the list to a .txt file. Input anything else to end the program.")
    x = input()
    if(x == "1"):
      with open('output.txt', 'w') as file:
        for item in nameList:
            file.write('%s\n' % item)
    else:
      exit()
  
  except CanvasException as e:
    print("\nAn error has occured. Check to see if the ID and API Key were valid.")

