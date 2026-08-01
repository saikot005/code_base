create or replace function income(name in varchar2) return varchar2 is
ilevel varchar2(30);
monthly number;
salary number;
cursor income is select sal,ename, from emp where ename=name;
begin
for i in income loop
select sal into monthly from emp where ename=name;
salary:=i.sal;
if(salary<1000)then
ilevel:= 'low income';
else ilevel:='high level';
end if;
return ilevel;
exception
when no_data_found then
dbms_output.put_line('there is income');
end;
/