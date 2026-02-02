"""
Employee Management System (EMS)
A simplified system to manage employee data using dictionaries and functions.
"""

# Initialize employee data with sample employees
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Ravi', 'age': 32, 'department': 'IT', 'salary': 60000},
    103: {'name': 'Priya', 'age': 29, 'department': 'Finance', 'salary': 55000}
}


def add_employee():
    """Add a new employee to the system."""
    print("\n--- Add Employee ---")
    
    # Get employee ID and validate uniqueness
    while True:
        try:
            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employees:
                print(f"Employee ID {emp_id} already exists. Please enter a unique ID.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric Employee ID.")
    
    # Get employee details
    while True:
        name = input("Enter Employee Name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please enter a valid name.")
    
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            if age <= 0:
                print("Age must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric age.")
    
    while True:
        department = input("Enter Employee Department: ").strip()
        if department:
            break
        print("Department cannot be empty. Please enter a valid department.")
    
    while True:
        try:
            salary = float(input("Enter Employee Salary: "))
            if salary <= 0:
                print("Salary must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric salary.")
    
    # Store employee in dictionary
    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    
    print(f"\nEmployee {name} (ID: {emp_id}) added successfully!")


def view_employees():
    """Display all employees in a table format."""
    print("\n--- All Employees ---")
    
    if not employees:
        print("No employees available.")
        return
    
    # Print table header
    print("-" * 80)
    print(f"{'ID':<10}{'Name':<20}{'Age':<10}{'Department':<20}{'Salary':<10}")
    print("-" * 80)
    
    # Print employee details
    for emp_id, details in employees.items():
        print(f"{emp_id:<10}{details['name']:<20}{details['age']:<10}"
              f"{details['department']:<20}{details['salary']:<10}")
    
    print("-" * 80)
    print(f"Total Employees: {len(employees)}")


def search_employee():
    """Search for an employee by ID."""
    print("\n--- Search Employee ---")
    
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid input. Please enter a numeric Employee ID.")
        return
    
    if emp_id in employees:
        details = employees[emp_id]
        print("\nEmployee Found:")
        print("-" * 50)
        print(f"ID:         {emp_id}")
        print(f"Name:       {details['name']}")
        print(f"Age:        {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary:     {details['salary']}")
        print("-" * 50)
    else:
        print("Employee not found.")


def main_menu():
    """Display the main menu and handle user choices."""
    while True:
        print("\n" + "=" * 40)
        print("Employee Management System")
        print("=" * 40)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("\nThank you for using the Employee Management System!")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main_menu()
