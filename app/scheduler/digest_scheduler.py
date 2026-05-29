from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


def generate_daily_digest():

    print("\n")
    print("=" * 50)
    print("VEERA DAILY DIGEST JOB")
    print(f"Executed At: {datetime.now()}")
    print("=" * 50)
    print("\n")


scheduler = BackgroundScheduler()

scheduler.add_job(
    generate_daily_digest,
    trigger="interval",
    minutes=1
)