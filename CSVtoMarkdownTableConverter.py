import csv

def print_markdown_table(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        headers = rows[0]
        print('| ' + ' | '.join(headers) + ' |')
        print('| ' + ' | '.join(['---' for _ in headers]) + ' |')
        for row in rows[1:]:
            print('| ' + ' | '.join(row) + ' |')

if __name__ == '__main__':
    file_path = input('Enter the file path for the CSV file: ')
    print_markdown_table(file_path)
