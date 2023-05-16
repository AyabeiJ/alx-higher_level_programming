#!/bin/bash
# Script: update_score.sh
# Description: Updates the score of Bob to 10 in the table second_table

# Check if the database name is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <database_name>"
  exit 1
fi

# Retrieve the database name from the command-line argument
database_name=$1

# Connect to MySQL and execute the SQL query
mysql -u username -p -e "USE $database_name; UPDATE second_table SET score = 10 WHERE name = 'Bob';"
