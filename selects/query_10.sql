SELECT sb.name
FROM subjects sb
JOIN grades g ON sb.id = g.subject_id
WHERE sb.teacher_id = 1
    AND g.student_id = 1
 GROUP BY sb.name;
