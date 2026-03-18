from datetime import datetime

def generate_report():
    print(f"Report generated at {datetime.now()}")
    print("DAO Activity: Active")
    print("Top Contributors: user1, user2")

if __name__ == "__main__":
    generate_report()