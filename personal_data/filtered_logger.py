
### `log_filter.py`

#!/usr/bin/env python3
"""
This module connects to a MySQL database, retrieves user data, and logs it while
obfuscating sensitive information.
"""

import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection

PII_FIELDS = ("name", "email", "password", "phone", "ssn")

LOG_FILE = 'filtered_user_data.log'


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class for logging obfuscated messages."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with a list of fields to redact.

        Args:
            fields (List[str]): The fields to obfuscate in the log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with sensitive fields redacted.
        """
        original_message = super(RedactingFormatter, self).format(record)
        redacted_message = filter_datum(self.fields, self.REDACTION,
                                        original_message, self.SEPARATOR)
        return redacted_message


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Obfuscate log messages by redacting specified fields.

    Args:
        fields (List[str]): Fields to obfuscate.
        redaction (str): Redaction string.
        message (str): Original log message.
        separator (str): Field separator in log message.

    Returns:
        str: Obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group().split('=')[0]}={redaction}",
                  message)


def get_logger() -> logging.Logger:
    """Create and configure a logger with RedactingFormatter.

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))
    ch.setFormatter(formatter)

    logger.addHandler(ch)

    return logger


def get_db() -> connection.MySQLConnection:
    """Connect to a MySQL database using environment variables.

    Returns:
        MySQLConnection: Database connection object.
    """
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    conn = mysql.connector.connect(
        user=db_username,
        password=db_password,
        host=db_host,
        database=db_name
    )

    return conn


def main():
    """Main function to set up logging, connect to the database, and log user data."""
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
    logger = get_logger()

    try:
        db = get_db()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        for row in rows:
            log_message = "; ".join(f"{key}={value}" for key, value in zip(cursor.column_names, row))
            logger.info(log_message)

        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        logger.error(f"Error connecting to MySQL: {err}")

    logger.info("Filtered fields:\n" + "\n".join(PII_FIELDS))


if __name__ == "__main__":
    main()
