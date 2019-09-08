select a.id as artwork_id, a.accession_number, a.title, a.tombstone, ac.creator_id,c.role as creator_role,c.description, ad.department_id, d.name as department_name
from artwork a LEFT JOIN  artwork__creator ac on a.id=ac.artwork_id
Left Join (select DISTINCT id, role, description from creator) as c
on c.id = ac.creator_id
left join artwork__department ad on ad.artwork_id = a.id
Left join department d on d.id = ad.department_id





