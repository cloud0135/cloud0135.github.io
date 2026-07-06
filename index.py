import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"

url1 = "https://quotes.toscrape.com/tag/love/"
url2 = "https://quotes.toscrape.com/tag/love/page/2/"

urls = [url1, url2]

# 1. CSV 파일 만들기
output_file = open("love_quotes.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(output_file)
writer.writerow(["명언", "저자", "저자 생년월일", "저자 출생지"])

for url in urls:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    quotes = soup.select("div.quote")

    for quote in quotes:
        text = quote.select_one("span.text").get_text(strip=True)
        author = quote.select_one("small.author").get_text(strip=True)

        about_link = quote.select_one("a").get("href")

        author_req = requests.get(base_url + about_link)
        author_soup = BeautifulSoup(author_req.text, "html.parser")

        birth_date = author_soup.select_one("span.author-born-date").get_text(strip=True)
        birth_place = author_soup.select_one("span.author-born-location").get_text(strip=True)

        writer.writerow([text, author, birth_date, birth_place])

output_file.close()


# 2. CSV 파일을 HTML 파일로 변환하기
input_file = open("love_quotes.csv", "r", encoding="utf-8-sig")
reader = csv.reader(input_file)

html_file = open("index.html", "w", encoding="utf-8")

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

        td {
            vertical-align: top;
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

print("love_quotes.csv 저장 완료")
print("index.html 저장 완료")