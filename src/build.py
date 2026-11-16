"""しおりを組み立てる。
- index.html            … GitHub Pages で公開するページ（HTML の外枠つき）
- .artifact/shiori.html … Claude のページ用（外枠なし。git には入れない）
"""
import pathlib
src = pathlib.Path(__file__).resolve().parent
root = src.parent
s = (src/"shiori.src.html").read_text().replace("/*LEAFLET_CSS*/", (src/"leaflet.css").read_text())
(root/".artifact").mkdir(exist_ok=True)
(root/".artifact"/"shiori.html").write_text(s)
i = s.index('<div class="wrap">')
head, body = s[:i], s[i:]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
out = ('<!doctype html>\n<html lang="ja">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       + head + '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
       '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(root/"index.html").write_text(out)
print("built index.html and .artifact/shiori.html")
