from datetime import datetime

current_time = datetime.now().replace(microsecond=0)

print("Datetime without microseconds:", current_time)
