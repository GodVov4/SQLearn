SELECT g.grade_date, gr.name, s.fullname, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN groups gr ON gr.id = s.group_id
WHERE gr.id = 1 AND g.subject_id = 1
ORDER BY g.grade_date DESC
LIMIT 1;
