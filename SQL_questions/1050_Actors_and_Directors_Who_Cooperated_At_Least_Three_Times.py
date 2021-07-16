
# Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

# Solution A: group by + having count(*)
SELECT actor_id, director_id
FROM ActorDirector a1
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3
