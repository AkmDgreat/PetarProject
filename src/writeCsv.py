import csv

# writes the data (a 2D array) to csv with name fileName
def writeCsv(fileName, data):
    with open(fileName, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f'Data has been successfully written to {fileName}.')
