from collections import deque

students = deque()

students.append("Student One")
students.append("Student Two")
students.append("Student Three")

while students:
    print("In progress: ", students.popleft())
else:
    print("Finished !")
