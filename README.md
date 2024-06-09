# port-scanner
## Overview
This is a simple port scanner written in Python. It allows users to specify an IP address and select target ports to scan. The scanner checks for open ports on the specified IP address.

## Features
- **IP Address Validation**: Ensures the provided IP address is valid.
- **Port Selection**: Allows users to select from common ports, well-known ports, or specify custom ports.
- **Port Scanning**: Scans the specified ports and lists the ones that are open.

## Usage
1. **Run the Script**: Execute the script from the command line.
    ```bash
    python port_scanner.py
    ```

2. **Enter Target IP Address**: When prompted, enter the IP address of the target.
    ```
    Enter Target IP address: 192.168.1.1
    ```

3. **Select Target Ports**: Choose the type of ports to scan.
    ```
    Select target ports
    1 - Common ports
    2 - Well-known ports
    3 - Custom
    ```

    - **Option 1**: Scans common ports (20, 53, 143, 443).
    - **Option 2**: Scans well-known ports (1-1024).
    - **Option 3**: Allows you to enter custom ports separated by commas.
        ```
        Enter custom ports separated by commas: 80, 8080, 3306
        ```

4. **View Results**: The script will display open ports.
    ```
    open port: 80
    open port: 443
    ```
## Notes
- Ensure you have the necessary permissions to scan the target IP address.
- Scanning ports without permission can be illegal and unethical. Use this tool responsibly.