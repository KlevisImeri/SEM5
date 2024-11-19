```sql
is null
is not null
outer join

'string' - \' not \"

update <alias>
set <field> =...
from <table> <alias>w
where ...

select top 1

desc - deseding from the biggest

NVARCHAR(50)

 @PCategory NVARCHAR(50) = NULL //Defautl value

exec procedurname 'input', 'input2';

create or alter trigger <name>
on <table>
for <updage|insert|delete>
as
//Triger does not need begint tran cause its atomic
inserted
deleted

ISNULL(@Total, 0)

set c.Total = ISNULL(c.Total, 0) + sum(oi.Price*oi.Amount)

DATEADD(YEAR,1,GETDATE())


declare cursorname cursor
for select c.ID from Category c;

open cursorname
declare @fetchHere int;
fetch next cursorname into @feachHere
while @@FETCH_STATUS = 0 begin;
  -- do your thing
  fetch next cursorname into @feachHere
end
close cursorname
deallocate cursorname
```
