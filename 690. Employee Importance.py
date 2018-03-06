"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.importance = 0
        self.employees = dict()
        
        for e in employees:
            self.employees[e.id] = e
        
        self.addImportance(self.employees[id])
        return self.importance
    
    def addImportance(self, employee):
        self.importance = self.importance + employee.importance
        for s in employee.subordinates:
            self.addImportance(self.employees[s])
        
