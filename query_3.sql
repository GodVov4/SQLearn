SELECT gr.name, ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN groups gr ON s.group_id = gr.id
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = subject_id
GROUP BY s.group_id;
