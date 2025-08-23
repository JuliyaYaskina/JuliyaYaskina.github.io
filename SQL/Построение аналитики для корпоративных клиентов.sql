-- Количество студентов компании
select
	distinct count(id)
from
	users
where
	company_id = 1
[[and date_joined between {{date1}} and {{date2}}]]

-- DAU - количество уникальных пользователей
select
	date(entry_at) as ymd,
	count(distinct user_id) as DAU
from
	userentry
left join users 
on
	userentry.user_id = users.id
left join company 
on
	users.company_id = company.id
where
	company_id = 1
 [[and entry_at between {{date1}} and {{date2}}]]
group by 1

-- MAU – количество уникальных пользователей за месяц
select
	date_trunc('month', entry_at) as month,
	count(distinct(user_id)) as MAU
from
	userentry
left join users 
on
	userentry.user_id = users.id
left join company 
on
	users.company_id = company.id
where
	company_id = 1
[[
	and entry_at between {{date1}} and {{date2}}]]
group by
	1
-- Rolling retention

with a as (
select
	u.user_id,
	date(u.entry_at) as entry_at,
	date(u2.date_joined) as date_joined,
	extract(days from u.entry_at - u2.date_joined) as diff,
	to_char(u2.date_joined, 'YYYY-MM') as cohort
from
	userentry u
join users u2
    on
	u.user_id = u2.id
where
	true 
[[
	and date_joined between {{date1}} and {{date2}}]]
[[
	and entry_at between {{date3}} and {{date4}}]]
	and company_id = 1
)
select
	cohort,
	round(count(distinct case when diff >= 0 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "0 (%)",
	round(count(distinct case when diff >= 1 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "1 (%)",
	round(count(distinct case when diff >= 3 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "3 (%)",
	round(count(distinct case when diff >= 7 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "7 (%)",
	round(count(distinct case when diff >= 14 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "14 (%)",
	round(count(distinct case when diff >= 30 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "30 (%)",
	round(count(distinct case when diff >= 60 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "60 (%)",
	round(count(distinct case when diff >= 90 then user_id end) * 100.0 / count(distinct case when diff >= 0 then user_id end), 2) as "90 (%)"
from
	a
group by
	cohort

-- Статистика прохождения курса 
with a0 as (
select
	problem_id
from
	problem_to_company
where
	company_id = 1
),
a as (
select
	email,
	created_at,
	1 as is_false,
	company_id,
	problem_id,
	date_joined
from
	coderun c
join users u 
	on
	c.user_id = u.id
where
	u.company_id = 1
	and problem_id in (
	select
		problem_id
	from
		a0)
union all
select
	email,
	created_at,
	is_false,
	company_id,
	problem_id,
	date_joined
from
	codesubmit c2
join users u 
	on
	c2.user_id = u.id
where
	u.company_id = 1
	and problem_id in (
	select
		problem_id
	from
		a0)
), 
b as (
select
	company_id,
	count(*) as all_amount
from
	problem_to_company
group by
	company_id
), 
c as (
select
		email, 
		min(date_joined) as date_joined,
		count(*) as all_atempts,
		count(*) - sum(is_false) as correct_attempts, 
		max(company_id) as company_id,
		count(distinct case when is_false = 0 then problem_id end) as correct_problems
from
	a
group by
	email
)
select
	c.email as "Почта",
	c.date_joined as "Дата регистрации",
	c.all_atempts as "Общее число попыток", 
	c.correct_attempts as "Правильных решений",
	c.correct_problems as "Правильно решенных задач",
	b.all_amount as "Всего задач на курсе",
	round(c.correct_problems * 100.0 / b.all_amount) as "Прогресс"
from
	c
join b
on
	c.company_id = b.company_id
join company c2 
on
	c.company_id = c2.id

-- Максимальное количество попыток решения задач 
with
  a0 as (
select
	problem_id
from
	problem_to_company
where
	company_id = 1
  )
select
	email,
	problem_id,
	p.name,
	count(created_at)
from
	coderun c
join users u on
	c.user_id = u.id
join problem p on
	c.problem_id = p.id
where
	u.company_id = 1
	and problem_id in (
	select
		problem_id
	from
		a0
  )
group by
	p.name,
	email,
	problem_id
union all
select
	email,
	problem_id,
	p.name,
	count(created_at)
from
	codesubmit c2
join users u on
	c2.user_id = u.id
join problem p on
	c2.problem_id = p.id
where
	u.company_id = 1
	and problem_id in (
	select
		problem_id
	from
		a0
  )
group by
	p.name,
	email,
	problem_id
order by
	count desc
limit 10
