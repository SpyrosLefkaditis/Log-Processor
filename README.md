# Log Processor

## Overview

The Log Processor is a Python script designed to analyze log files and identify suspicious activity based on specified criteria. It reads log entries, extracts IP addresses associated with "WARNING" messages, and generates a report of suspicious IPs found.

## Features

- **Log Analysis**: Processes log files to find entries with "WARNING" messages.
- **IP Extraction**: Uses regular expressions to extract IP addresses associated with warnings.
- **Report Generation**: Outputs a report (`report.log`) listing suspicious IP addresses.

## Example Log File

Here's an example of a log file :

2024-06-15 12:34:56 INFO User logged in from 192.168.1.1
2024-06-15 12:35:00 ERROR Failed login attempt from 192.168.1.2
2024-06-15 12:35:10 WARNING Suspicious activity from 192.168.1.3
2024-06-15 12:35:20 WARNING Potential breach from 192.168.1.4
2024-06-15 12:35:30 WARNING Unauthorized access from 192.168.1.5
2024-06-15 12:35:40 INFO User logged in from 192.168.1.6

