import csv

input_file = open("love_quotes.csv", "r", encoding="utf-8-sig")
reader = csv.reader(input_file)

html_file = open("love_quotes.html", "w", encoding="utf-8")

html_file.write("""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Love Quotes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f8f8f8;
        }

        h1 {
            text-align: center;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background-color: white;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #eeeeee;
        }
    </style>
</head>
<body>
    <h1>Love Quotes</h1>
    <table>
""")

for row_index, row in enumerate(reader):
    html_file.write("<tr>")

    for data in row:
        if row_index == 0:
            html_file.write(f"<th>{data}</th>")
        else:
            html_file.write(f"<td>{data}</td>")

    html_file.write("</tr>\n")

html_file.write("""
    </table>
</body>
</html>
""")

input_file.close()
html_file.close()

print("love_quotes.html 저장 완료")