SELECT sb.name
FROM students s
JOIN grades g ON s.id = g.subject_id
JOIN subjects sb ON g.subject_id = sb.id
WHERE g.student_id = 1
GROUP BY sb.id;


