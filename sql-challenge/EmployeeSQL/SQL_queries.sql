-- List the employee number, last name, first name, sex, and salary of each employee.
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM employee e
JOIN salaries s 
ON e.emp_no = s.emp_no
LIMIT 100;

-- List the first name, last name, and hire date for the employees who were hired in 1986.
SELECT e.emp_no, e.last_name, e.first_name, e.hire_date
FROM employee e
WHERE hire_date >= '1986-01-01' AND hire_date <= '1986-12-31'
LIMIT 100;

-- List the manager of each department along with their department number, department name, employee number, last name, and first name.
SELECT dm.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name
FROM dept_managers dm
JOIN departments d
ON dm.dept_no = d.dept_no
JOIN employee e
ON dm.emp_no = e.emp_no
LIMIT 100;

-- List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
SELECT de.dept_no, de.emp_no, e.last_name, e.first_name, d.dept_name
FROM department_employees de 
JOIN employee e
ON de.emp_no = e.emp_no
JOIN departments d
ON de.dept_no = d.dept_no
LIMIT 100;

-- List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
SELECT e.first_name, e.last_name, e.sex
FROM employee e
WHERE first_name = 'Hercules' and last_name LIKE 'B%'
LIMIT 100;

-- List each employee in the Sales department, including their employee number, last name, and first name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employee e
JOIN department_employees de
ON e.emp_no = de.emp_no
JOIN departments d
ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Sales'
LIMIT 100;

-- List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name
FROM employee e
JOIN department_employees de
ON e.emp_no = de.emp_no
JOIN departments d
ON de.dept_no = d.dept_no
WHERE d.dept_name IN ('Sales', 'Development')
LIMIT 100;

-- List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).
SELECT last_name, COUNT(*) AS name_count
FROM employee
GROUP BY last_name
ORDER BY name_count DESC;
