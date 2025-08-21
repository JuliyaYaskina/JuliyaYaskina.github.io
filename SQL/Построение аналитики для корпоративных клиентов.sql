-- Количество студентов компании
SELECT
	distinct count(id)
FROM
	users
WHERE
	company_id = 1
[[and date_joined between {{date1}} and {{date2}}]]
