SELECT t.fullname, st.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
JOIN grades g ON s.id = g.subject_id
JOIN students st ON st.id = g.student_id
WHERE g.student_id = 1
    AND t.id = 1
GROUP BY g.student_id;
