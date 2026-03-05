import argparse
from collections import defaultdict
from colorama import Fore, Style

def analyze_logs(log_file, threshold):

    failed_attempts = defaultdict(int)

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()
                ip = parts[-1]
                failed_attempts[ip] += 1

    print(f"\n{Fore.CYAN}Log Analysis Results{Style.RESET_ALL}\n")

    suspicious_found = False

    for ip, count in failed_attempts.items():
        if count >= threshold:
            suspicious_found = True
            print(f"{Fore.RED}{ip}{Style.RESET_ALL} -> {count} failed login attempts")

    if not suspicious_found:
        print(f"{Fore.GREEN}No suspicious activity detected.{Style.RESET_ALL}")


def main():

    parser = argparse.ArgumentParser(description="Detect suspicious login attempts in authentication logs")

    parser.add_argument(
        "-f",
        "--file",
        default="logs/auth.log",
        help="Path to log file"
    )

    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        default=3,
        help="Number of failed attempts required to flag an IP"
    )

    args = parser.parse_args()

    analyze_logs(args.file, args.threshold)


if __name__ == "__main__":
    main()
