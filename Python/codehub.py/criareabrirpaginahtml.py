
# criar e abrir página html

import webbrowser

f = open('helloworld.html','wb')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')