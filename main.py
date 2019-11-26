import csv

# returns a list of dictionaries from csv file

def reader(fref):

    rows = []

    with open(fref) as csvfile:

        reader = csv.DictReader(csvfile)

        for row in reader:

            rows.append(row)

    return rows


def filter_by_job(rows, job):

    result = []

    for row in rows:

        if row["fjobno"] == job:

            result.append(row)

    return result

def get_work_centers(filtered_rows):

    results = []

    for row in filtered_rows:

        if not row['fpro_id'] in results:

            results.append(row['fpro_id'])

    return results

def convert_elapsed_time(formatted_time):

    delim = formatted_time.split(":")

    hours = int(delim[0])

    minutes = int(delim[1])

    return round(float(hours) + float(minutes/60), 2)


rows = reader("sample.csv")

job06634 = filter_by_job(rows, "06634-0000")

work_centers = get_work_centers(job06634)

print(work_centers)

print(convert_elapsed_time("0:00"))
