import random
from datetime import datetime, timedelta

def generate_class_data(num_records):
    data = []
    base_date = datetime(2024, 11, 12, 8, 0)

    for i in range(num_records):
        class_code = f"20.4B.04.{str(i+1).zfill(3)}"

        random_minutes = random.randint(0, 60 * 24 * 7)
        class_datetime = base_date + timedelta(minutes=random_minutes)
        class_datetime_str = class_datetime.strftime("%A %d %B %Y, %H:%M")

        status = random.choice(["Tersedia", "Tidak Tersedia"])

        data.append((class_code, class_datetime_str, status))

    return data

class_data = generate_class_data(10)

print(class_data)