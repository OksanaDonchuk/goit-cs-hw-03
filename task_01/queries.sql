--Отримати всі завдання певного користувача

select title, description  from tasks
where user_id = 2;

--Вибрати завдання за певним статусом

select id, title, description  from tasks
where status_id = (select id from status where name = 'new');

--Оновити статус конкретного завдання

update tasks
set status_id = (select id from status where name = 'in progress')
where id = 1;

--Отримати список користувачів, які не мають жодного завдання

select * from users
where id not in (select user_id from tasks);

--Додати нове завдання для конкретного користувача

insert into tasks (title, description, status_id, user_id)
values ('Урок 5', 'Прочитати конспект, попрактикувати код, подивитись урок з викладачем', 1, 4);

--Отримати всі завдання, які ще не завершено

select * from tasks
where status_id in (select id from status where name = 'new' or name = 'in progress');

--Видалити конкретне завдання

delete from tasks 
where id = 3;

--Знайти користувачів з певною електронною поштою

select * from users
where email like '%gmail%';

--Оновити ім'я користувача

update users
set fullname = 'Oksana'
where id = 1;

--Отримати кількість завдань для кожного статусу

select s.name, count(t.id) as task_count
from status as s 
join tasks as t on s.id = t.status_id 
group by s.name;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти

select t.*
from tasks as t
join users as u on t.user_id = u.id 
where email like '%gmail.com';

--Отримати список завдань, що не мають опису

select * from tasks t 
where description is null or description = '';

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'

select u.*, t.*
from users as u
join tasks as t on u.id = t.user_id
join status as s on s.id = t.status_id 
where s.name = 'in progress';

--Отримати користувачів та кількість їхніх завдань

select u.*, count(t.id) as task_count
from users as u
left join tasks as t on u.id = t.user_id
group by u.id;