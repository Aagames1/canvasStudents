from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
API_URL = "https://mcpsmd.instructure.com/"
API_KEY = "[INSERT API KEY]" 
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


def getCourses(userID):
  user = canvas.get_user(userID)
  courseList = user.get_courses(enrollment_status='active')
  return courseList
  
while True:
  print("Enter your Canvas ID: ")
  ID = input()

  try:
    courseList = getCourses(ID)
    try:
      for course in courseList:
         print("\n")
         print(course)
    except Exception as e:
      
      print("\n*****************************************" + 
      "\n\nEnter the ID of the class you want a list of: ")
      ID = input()

      try:
        nameList = getStudents(ID)
        with open('output.txt', 'w') as file:
          file.write(getCourseName(ID))
          file.write('\n')
          for item in nameList:
              file.write('%s\n' % item)
            
        print("Student list saved!")
        exit()

      except CanvasException as e:
        print("\nAn error has occured. Either the ID was invalid, or the course doesn't give permissions to view all students.")
        exit()
  
  except CanvasException as e:
    print("\nAn error has occured. Check to see if the ID and API Key were valid.")
    exit()

