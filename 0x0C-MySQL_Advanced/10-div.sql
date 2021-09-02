-- function SafeDiv that divides
-- (and returns) the first by the second number

DELIMITER //

CREATE FUNCTION SafeDiv(a INTEGER, b INTEGER)
RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END //

DELIMITER ;
