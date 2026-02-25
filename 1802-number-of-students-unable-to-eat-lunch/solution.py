class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students preferring each type of sandwich (0 or 1)
        student_preferences = Counter(students)
      
        # Process sandwiches from top to bottom
        for sandwich_type in sandwiches:
            # If no students want the current sandwich type, we're stuck
            if student_preferences[sandwich_type] == 0:
                # Return the count of students wanting the other type (XOR flips 0->1, 1->0)
                return student_preferences[sandwich_type ^ 1]
          
            # A student takes the sandwich, decrease the count
            student_preferences[sandwich_type] -= 1
      
        # All sandwiches were taken, no students left waiting
        return 0
     
        
