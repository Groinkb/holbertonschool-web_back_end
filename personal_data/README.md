# Log Filtering Project

This project contains a Python script that connects to a MySQL database, retrieves user data, and logs it while redacting sensitive information.

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- MySQL
- Environment variables for database credentials:
  - `PERSONAL_DATA_DB_USERNAME`
  - `PERSONAL_DATA_DB_PASSWORD`
  - `PERSONAL_DATA_DB_HOST`
  - `PERSONAL_DATA_DB_NAME`

## Files
- `log_filter.py`: Main script for filtering log data.
- `README.md`: This file.

## Usage
Make sure to set the required environment variables before running the script. Then execute the script:

```sh
./log_filter.py
