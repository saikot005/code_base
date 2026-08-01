SET SERVEROUTPUT ON

declare
	cursor cur is select ename from emp;
	name emp.ename%type;
begin
	open cur;
	loop
	fetch cur into name;
	dbms_output.put_line(name);
	exit when cur %notfound;
	end loop;
	close cur;
end;
/
