#!/usr/bin/env python3
"""Regex-ing"""

import re
import logging
import os
from typing import List
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone',
              'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """returns a logging.Logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    log = logging.StreamHandler()
    log.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(log)
    return logger


def filter_datum(fields: List[str],
                 redaction: str, message:
                 str, separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(field + '=.*?' + separator,
                         field + '=' + redaction + separator, message)
    return message


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function that returns a connector to the database"""
    cnx = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD'),
        host=os.getenv('PERSONAL_DATA_DB_HOST'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'))
    return cnx


def main() -> None:
    """obtain a database connection
    using get_db and retrieve all
    rows in the users table"""
    query = 'SELECT * FROM users'
    cnx = get_db()
    cursor = cnx.cursor()
    cursor.execute(query)
    logger = get_logger()
    for item in cursor:
        logger.log(logging.INFO, item[0])
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()
