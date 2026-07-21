SELECT name AS results
FROM (
  SELECT u.name
  FROM users u
  JOIN movierating mr ON u.user_id = mr.user_id
  GROUP BY u.name
  ORDER BY COUNT(*) DESC, u.name ASC
  LIMIT 1
) AS top_user

UNION ALL

SELECT title AS results
FROM (
  SELECT m.title
  FROM movies m
  JOIN movierating mr ON m.movie_id = mr.movie_id
  WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
  GROUP BY m.title
  ORDER BY AVG(mr.rating) DESC, m.title ASC
  LIMIT 1
) AS top_movie;