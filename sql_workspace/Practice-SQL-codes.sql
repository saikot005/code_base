-- Q1.Find all the airlines where the total salary of all pilots in that airline more than the average of total salary of all pilots in the database is

CREATE TABLE Pilot (
    EmployeeID INT PRIMARY KEY,
    Airline VARCHAR(50),
    Name VARCHAR(50),
    Salary DECIMAL(10, 2)
);

INSERT INTO Pilot (EmployeeID, Airline, Name, Salary) VALUES
(70007, 'Airbus 380', 'Kim', 60000.00),
(70002, 'Boeing', 'Laura', 20000.00),
(10027, 'Airbus 380', 'Will', 80050.00),
(10778, 'Airbus 380', 'Warren', 80780.00),
(115585, 'Boeing', 'Smith', 25000.00),
(114070, 'Airbus 380', 'Katy', 78000.00);

SELECT AIRLINE
FROM PILOT
GROUP BY AIRLINE
HAVING SUM(SALARY) > (SELECT AVG(SALARY) FROM PILOT);

------------------------------------------------------------------------------------------------------

-- Q2.Find top 10 salary earner (multiple ways)
SELECT * FROM EMPLOYEES ORDER BY SALARY DESC LIMIT 10;
SELECT * FROM EMPLOYEES QUALIFY DENSE_RANK() OVER (ORDER BY SALARY DESC) <= 10;
SELECT * FROM ( SELECT *,ROW_NUMBER() OVER (ORDER BY SALARY DESC) AS RNK FROM EMPLOYEES ORDER BY SALARY DESC ) WHERE RNK <=10;
SELECT * FROM EMPLOYEES OQ WHERE 10-1 >= (SELECT COUNT(EMPLOYEE_ID) FROM EMPLOYEES WHERE OQ.SALARY < IQ.SALARY) ORDER BY SALARY DESC;
SELECT * FROM EMPLOYEES ORDER BY SALARY DESC FETCH FIRST 10 ROWS ONLY;

------------------------------------------------------------------------------------------------------

-- Q3.Find 3RD higrst salary earner (multiple ways)
SELECT * FROM EMPLOYEES QUALIFY DENSE_RANK() OVER (PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) = 3 ;
SELECT * FROM ( SELECT *,ROW_NUMBER() OVER (PARTITION BY DEPARTMENT_ID ORDER BY SALARY DESC) AS RNK FROM EMPLOYEES ORDER BY SALARY DESC ) WHERE RNK =3;
SELECT * FROM EMPLOYEES OQ WHERE 3-1 = (SELECT COUNT(EMPLOYEE_ID) FROM EMPLOYEES WHERE OQ.SALARY < IQ.SALARY AND OQ.DEPARTMENT_ID=IQ.DEPARTMENT_ID) ORDER BY SALARY DESC;

------------------------------------------------------------------------------------------------------

-- Q4/5.Delete duplicate record (multiple ways)
DELETE FROM EMPLOYEES WHERE ROWID NOT IN (SELECT MAX(ROWID) FROM EMPLOYEES GROUP BY EMPLOYEE_ID);
DELETE FROM EMPLOYEES WHERE ROWID NOT IN (SELECT MIN(ROWID) FROM EMPLOYEES GROUP BY EMPLOYEE_ID);

CREATE OR REPLACE TEMPORARY TABLE TEST AS 
SELECT * FROM EMPLOYEES QUALIFY ROW_NUMBER() OVER (PARTITION BY EMPLOYEE_ID ORDER BY EMPLOYEE_ID)=1;

------------------------------------------------------------------------------------------------------

-- Q6.Select unique records (multiple ways)
SELECT * FROM EMPLOYEES UNION SELECT * FROM EMPLOYEES;
SELECT * FROM EMPLOYEES INTERSECT SELECT * FROM EMPLOYEES;
SELECT * FROM EMPLOYEES GROUP BY ALL;
SELECT * FROM EMPLOYEES QUALIFY ROW_NUMBER(PARTITION BY EMPLOYEE_ID ORDER BY EMPLOYEE_ID) = 1;
SELECT DISTINCT COLNAMES FROM EMPLOYEES;

------------------------------------------------------------------------------------------------------

-- Q8.Select duplicate records (multiple ways)
SELECT EMPLOYEE_ID FROM EMPLOYEES GROUP BY EMPLOYEE_ID HAVING COUNT(*) > 1;
SELECT * FROM EMPLOYEES QUALIFY ROW_NUMBER(PARTITION BY EMPLOYEE_ID ORDER BY EMPLOYEE_ID) <> 1;

------------------------------------------------------------------------------------------------------

-- Q9.Same salary earner
SELECT * FROM EMP WHERE SALARY IN (SELECT SALARY FROM EMPLOYEES GROUP BY SALARY HAVING COUNT(SALARY)>1);

------------------------------------------------------------------------------------------------------

-- Q9.Employees working more than 10 years
select * from hr.employees where hire_date < add_months(sysdate,-20);
-- Employees joining on year 2003
select * from hr.employees where to_char(hire_date,'YY') = '03';
-- Employees joining on january month
select * from hr.employees where to_char(hire_date,'MM') = '01';
-- Employees joining on 13th of each month
select * from hr.employees where to_char(hire_date,'DD') = '13';
-- Employees joining on 13th of january month
select * from hr.employees where to_char(hire_date,'MM-DD') = '01-13';

------------------------------------------------------------------------------------------------------