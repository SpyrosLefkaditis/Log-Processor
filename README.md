# Log Processor

## Overview

The Log Processor is a Python script designed to analyze log files and identify suspicious activity based on specified criteria. It reads log entries, extracts IP addresses associated with "WARNING" messages, and generates a report of suspicious IPs found.

## Features

- **Log Analysis**: Processes log files to find entries with "WARNING" messages.
- **IP Extraction**: Uses regular expressions to extract IP addresses associated with warnings.
- **Report Generation**: Outputs a report (`report.log`) listing suspicious IP addresses.

## Example Log File

Here's an example of a log file (`log1.log`) that the script can analyze:

