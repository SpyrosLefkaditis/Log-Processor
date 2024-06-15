import re

def main():
    # Ask the user for the path to the log file
    log_file_path = input("Enter the path to the log file: ").strip()
    output_file_path = 'report.log'

    # Define a regular expression pattern to match WARNING log entries and extract IP addresses
    warning_pattern = re.compile(r'WARNING .* from (\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)')

    suspicious_ips = []

    # Read and process the log file
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = warning_pattern.search(line)
            if match:
                ip = match.group(1)
                suspicious_ips.append(ip)

    # Write the suspicious IPs to the report file
    with open(output_file_path, 'w') as report_file:
        if suspicious_ips:
            report_file.write("Suspicious activity IPs:\n\n")
            for ip in suspicious_ips:
                report_file.write(f"{ip}\n")
        else:
            report_file.write("No suspicious activity IPs found.\n")

    print(f"Report generated: {output_file_path}")

if __name__ == "__main__":
    main()
