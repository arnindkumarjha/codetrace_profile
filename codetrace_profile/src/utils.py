def format_time(seconds):
    """Convert seconds to a formatted string."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def log_event(event):
    """Log a profiling event."""
    with open("profiling_log.txt", "a") as log_file:
        log_file.write(f"{event}\n")