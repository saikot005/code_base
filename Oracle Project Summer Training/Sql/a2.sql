SET SERVEROUTPUT ON
declare
	cursor cs is select ename from emp;
	name emp.ename%type;
begin
	open cs;
	loop;
	fetch cs into name;
	dbms_output.put_line(name);
	end loop;
	close cs;
end;
/
