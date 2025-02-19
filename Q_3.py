# A teacher maintains a list of students in a class. The list is ["Alice", "Bob", "Charlie",
# "David", "Eve"]. Write a Python program to print the names of students whose names start
# with "A" or "D".

if __name__== "__main__":

    student_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

    for i in range(len(student_list)):
        if student_list[i].startswith("A") or student_list[i].startswith("D"):
            print(student_list[i])


