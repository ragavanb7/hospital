patients = [
    {
        "name": "Ravi",
        "age": 60,
        "heart_rate": 80,
        "oxygen": 98
    },
    {
        "name": "Priya",
        "age": 72,
        "heart_rate": 110,
        "oxygen": 92
    },
    {
        "name": "Arun",
        "age": 50,
        "heart_rate": 90,
        "oxygen": 96
    },
    {
        "name": "Kumar",
        "age": 68,
        "heart_rate": 120,
        "oxygen": 88
    }
]

critical_ages = []

print("\nPatient Details\n")

for patient in patients:

    if patient["heart_rate"] < 60 or patient["heart_rate"] > 100:
        status = "Critical"

    elif patient["oxygen"] < 95:
        status = "Critical"

    else:
        status = "Normal"

    patient["status"] = status

    print(patient)

    if status == "Critical":
        critical_ages.append(patient["age"])

print("\nCritical Patients")

for patient in patients:
    if patient["status"] == "Critical":
        print(patient["name"])

if len(critical_ages) > 0:
    average = sum(critical_ages) / len(critical_ages)
    print("\nAverage Age of Critical Patients")
    print(average)

patients.sort(key=lambda x: x["oxygen"])

print("\nSorted by Oxygen")

for patient in patients:
    print(patient["name"], patient["oxygen"])
