USE [dynamics-reports-dev-01-db]

select * from [staging].[endv_skill] where [endv_skillid] = 'D9953F83-A0A3-EC11-983F-000D3ADF914B'

select *
from [dbo].[endv_person]
where endv_country = '106DAFC0-F283-E611-80CE-005056A82C24'

/*
retrieve active people fields for the Active People Report sheet
*/
select 
	P.endv_fullname as full_name,
	BU.[name] as current_bu,
	G.endv_name as grade,
	D.endv_name as discipline,
	S.endv_name as core_skill
from
	[dbo].[endv_person] as P
INNER JOIN
	[dbo].[businessunit] as BU
	ON BU.Id = P.endv_currentbu
INNER JOIN
	[staging].[endv_grade] as G
	ON G.endv_gradeid = P.endv_grade
INNER JOIN
	[staging].[endv_discipline] as D
	ON D.endv_disciplineid = P.endv_discipline
INNER JOIN
	[staging].[endv_skill] as S
	ON S.endv_skillid = P.endv_coreskill
WHERE
P.endv_country = '106DAFC0-F283-E611-80CE-005056A82C24' /* id of country romania*/


select * from [dbo].[businessunit] where Id = '9C06F767-D1C3-E411-80C3-00155D1EF506'
