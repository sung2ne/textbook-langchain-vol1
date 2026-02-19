from bs4 import BeautifulSoup

html = """
<html>
<body>
    <h1>제목입니다</h1>
    <p class="content">내용입니다.</p>
    <p class="content">두 번째 내용입니다.</p>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# 태그로 찾기
title = soup.find("h1")
print(title.text)  # 제목입니다

# 클래스로 찾기
contents = soup.find_all("p", class_="content")
for p in contents:
    print(p.text)
