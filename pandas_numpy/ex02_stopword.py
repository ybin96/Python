import re

data = '''<div>
            <p>안녕</p>
            <p>좋아요</p>
    </div>'''
data = re.sub('<.+?>', '', data)

# data = data.replace(".","")
# data = re.sub('<','',data)
# data = re.sub('>','',data)
# data = re.sub('[A-Za-z]','',data)
# data = re.sub(r'<div>','',data)
# data = re.sub('<.+?>','',data)
# data = re.sub(r'[~!@#$%^&*()+{}<>?/]+','',data)
# data = data.replace(".","")

print(data)