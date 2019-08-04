from application.salary import calculate_salary
from application.db.people import get_employees as ge

if __name__ == '__main__':
    calculate_salary()
    ge()
