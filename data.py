import csv
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_file.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_file:
            csv_writer.writerow(line)