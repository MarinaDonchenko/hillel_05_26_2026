class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
       # self.programming_language = programming_language
        self.team_size = team_size

# тест через звернення до поля
team_lead = TeamLead(
    name = "Violetta",
    salary = 5000,
    department = "Engineering",
    programming_language = "Python",
    team_size = 7
)
print(f"Name: {team_lead.name}")
print(f"Salary: {team_lead.salary}")
print(f"Department: {team_lead.department}")
print(f"Language: {team_lead.programming_language}")
print(f"Team size: {team_lead.team_size}")