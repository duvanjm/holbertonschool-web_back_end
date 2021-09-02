-- stored procedure AddBonus
-- that adds a new correction for a student

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INTEGER, IN project_name VARCHAR(255), IN score INTEGER)
BEGIN
    INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$

DELIMITER ;
