# A university has a Person class with a method introduce() that prints "I am a person."
# A subclass Student overrides this method to print "I am a student." Write the Python
# code demonstrating this behavior.


class Person():

    # Defining introduce() function of Person class
    def introduce(self):
        print("I am a person")


class Student(Person):

    # Defining introduce() function of Student class
    def introduce(self):
        print("I am a student")


student_obj = Student() # Creating an object of Student() class
student_obj.introduce() # introduce() of Student() class is called. It will override the