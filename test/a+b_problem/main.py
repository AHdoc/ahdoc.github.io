from pyscript import Element

def solve():
	a = int(Element('a').value)
	b = int(Element('b').value)
	display(str(a)+' + '+str(b)+' = '+str(a+b), target="c")
