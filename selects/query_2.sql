SELECT s.id, s.fullname, sb.name, ROUND(AVG(g.grade), 2) as average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects sb ON sb.id = g.subject_id
WHERE g.subject_id = 1
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
