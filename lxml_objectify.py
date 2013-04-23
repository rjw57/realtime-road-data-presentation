import lxml.objectify as lo
fobj = open('document.xml')
document = lo.parse(fobj)
script = document.getroot()
print(script.character[0].name)
# prints 'James Kirk'
print([c.actor for c in script.character])
# prints ['William Shatner', 'Leonard Nimoy']
