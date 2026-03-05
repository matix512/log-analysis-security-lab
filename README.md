# Log Analysis - Suspicious Authentication Detection

## Overview

This project simulates a basic **SOC analyst task**: analyzing authentication logs to detect suspicious login attempts.

The goal is to demonstrate practical skills in:

- Log analysis
- Basic threat detection
- Python scripting
- Security-focused data parsing

The script processes authentication logs and identifies IP addresses with an excessive number of failed login attempts.

---

## Project Structure


log-analysis-suspicious-auth/
│
├── sample_logs/
│ └── auth.log
│
├── scripts/
│ └── analyze_auth.py
│
├── results/
│ └── suspicious_ips.txt
│
└── README.md


---

## Detection Logic

The script analyzes authentication logs and:

1. Searches for **failed login attempts**
2. Extracts the **source IP address**
3. Counts the number of failures per IP
4. Flags IPs with more than **5 failed attempts**

This is a simplified version of detection logic often implemented in:

- SIEM platforms
- IDS systems
- SOC monitoring pipelines

---

## Example Log Entry


Mar 10 10:12:44 server sshd[1234]: Failed password for root from 192.168.1.50 port 22 ssh2


The script extracts:


IP Address: 192.168.1.50


---

## How to Run

Clone the repository:


git clone [https://github.com/yourusername/log-analysis-suspicious-auth.git


Navigate to the project folder:


cd log-analysis-suspicious-auth


Run the script:


python scripts/analyze_auth.py


Output:


Suspicious IP detected: 192.168.1.50 (7 failed attempts)


---

## Output Example


192.168.1.50 - 7 failed login attempts
10.0.0.22 - 9 failed login attempts


Results are saved in:


results/suspicious_ips.txt


---

## Skills Demonstrated

- Security log analysis
- Python scripting
- Pattern detection
- Basic threat detection logic
- Security documentation

---

## Future Improvements

Possible extensions:

- Detect **brute force patterns**
- Integrate with **Elastic Stack**
- Parse **multiple log formats**
- Visualize results with dashboards
- Add **real-time log monitoring**

---

## Author

Diogo Morais

Aspiring **SOC Analyst / Cybersecurity Professional**


