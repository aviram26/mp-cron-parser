import time

from cron_parser import Cron


def cron_to_text(expr):
    try:
        cron = Cron(expr)
        now = time.time()
        n = cron.next_run(now)
        if n is None:
            return "never"
        tm = time.localtime(n)
        return "%04d-%02d-%02d %02d:%02d" % (tm[0], tm[1], tm[2], tm[3], tm[4])
    except Exception as e:
        return "Error: %s" % e


if __name__ == "__main__":
    tests = [
        "0 17 */2 * *",
        "* * * * *",
        "15 6 * * 1",
        "0 0 1 * *",
        "0 */6 * * *",
        "0-45/5 17 * * *",
        "0 0 * * 6,0",
        "0 0 * * FRI",
        "0 0 L * *",  # This and below are not standard syntax, so won't match; will show "Error:"
        "0 0 15W * *",
        "0 0 * * 5L",
        "0 0 * * 1#2",
        "@yearly",
        "@monthly",
        "@weekly",
        "@daily",
        "@hourly",
        "0 0 * * 0,7",
    ]
    print("Testing cron parser:")
    for expr in tests:
        print(f"{expr:18}: {cron_to_text(expr)}")
