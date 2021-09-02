-- script that creates
-- a trigger that resets the attribute valid_email

DELIMITER $$

DROP TRIGGER IF EXISTS resets;
CREATE TRIGGER resets BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;

END$$

DELIMITER ;
