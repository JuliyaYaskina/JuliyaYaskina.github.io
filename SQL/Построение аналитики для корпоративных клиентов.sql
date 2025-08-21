-- Количество студентов компании
SELECT
	distinct count(id)
FROM
	users
WHERE
	company_id = 1
[[and date_joined between {{date1}} and {{date2}}]]

-- DAU - количество уникальных пользователей
SELECT
	date(entry_at) as ymd,
	count(distinct user_id) as DAU
FROM
	userentry
left join users 
on
	userentry.user_id = users.id
left join company 
on
	users.company_id = company.id
WHERE
	company_id = 1
 [[and entry_at between {{date1}} and {{date2}}]]
group by 1
