# JTSK-350112
# a2 1.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de



"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
   """Represents a student."""

   def __init__(self, name, number):
      """All scores are initially 0."""
      self._name = name
      self._scores = []
      print('Constructor being called')
      for count in range(number):
         self._scores.append(0)

   def getName(self):
      """Returns the student's name."""
      return self._name
      
  
   def setScore(self, i, score):
      """Resets the ith score, counting from 1."""
      self._scores[i - 1] = score
      

   def getScore(self, i):
      """Returns the ith score, counting from 1."""
      return self._scores[i - 1]
   
   def getAverage(self):
      """Returns the average score."""
      return sum(self._scores) / len(self._scores)
    
   def getHighScore(self):
      """Returns the highest score."""
      return max(self._scores)
 
   def __str__(self):
      """Returns the string representation of the student."""
      return "Name: " + self._name  + "\nScores: " + \
             " ".join(map(str, self._scores))

  
   

obj1 = Student('Jenny', 2)
obj1.setScore(1,95)
obj1.setScore(2,90)


obj2 = Student('Steve', 2)
obj2.setScore(1,95)
obj2.setScore(2,90)


obj3 = Student('Celine', 2)
obj3.setScore(1,95)
obj3.setScore(2,95)

