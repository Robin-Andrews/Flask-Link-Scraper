import csv


def process_data(data):
    with open('data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        # write title row
        writer.writerow(["href"])

        # Write data
        for link in data:
            writer.writerow([link])  # writerow expects a sequence, hence []
