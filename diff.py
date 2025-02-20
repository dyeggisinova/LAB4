from datetime import datetime

date1 = datetime(2025, 2, 18, 12, 0, 0)
date2 = datetime(2025, 2, 20, 14, 30, 0)

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)
