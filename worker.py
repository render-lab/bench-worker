"""Seed background worker: a long-running loop with no HTTP server.

Stands in for a queue consumer / poller. Add real job logic, then ship it as a
long-running process. No deploy config on purpose.
"""

import os
import time

POLL_SECONDS = int(os.environ.get("POLL_SECONDS", "5"))


def process_next_job():
    # TODO: pull from a real queue (Redis/Postgres) and do work.
    print("worker: no jobs, sleeping", flush=True)


def main():
    print("worker: started", flush=True)
    while True:
        process_next_job()
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
