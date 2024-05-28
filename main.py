import sys
from canvasapi import Canvas 
from canvasapi.exceptions import CanvasException
API_URL = "https://mcpsmd.instructure.com/"
API_KEY = "[API_KEY]" 
canvas = Canvas(API_URL, API_KEY)

def getStudents(courseID):
  course = canvas.get_course(courseID)
  users = course.get_users(enrollment_type=['student'])

  with open('students.txt', 'w') as file:
    file.write(getCourseName(courseID))
    file.write('\n')
    for user in users:
        file.write('%s\n' % user)

  print("Student names saved!")

def getCourseName(courseID):
  course = canvas.get_course(courseID)
  return course.name

# userID = 36343
def getCourses(userID):
  user = canvas.get_user(userID)
  courseList = user.get_courses(enrollment_status='active')
  with open('classes.txt', 'w') as file:
    try:
      for course in courseList:
        file.write('%s\n' % course)

      print("Courses saved!")
    except Exception as e:
      print("Courses saved!")


def generate_data(param1, param2):
  getCourses(param1)
  getStudents(param2)


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Invalid number of parameters. Usage: python main.py <param1> <param2>.")
    sys.exit(1)
  param1 = sys.argv[1]
  param2 = sys.argv[2]
  generate_data(param1, param2)

