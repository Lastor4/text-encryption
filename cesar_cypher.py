import re


#TODO: Check if we can improve this implementation
class bidict(dict):
    def __init__(self, *args, **kwargs):
        super(bidict, self).__init__(*args, **kwargs)
        self.inverse = {}
        for key, value in self.items():
            self.inverse.setdefault(value, []).append(key) 

    def __setitem__(self, key, value):
        if key in self:
            self.inverse[self[key]].remove(key) 
        super(bidict, self).__setitem__(key, value)
        self.inverse.setdefault(value, []).append(key)        

    def __delitem__(self, key):
        self.inverse.setdefault(self[key], []).remove(key)
        if self[key] in self.inverse and not self.inverse[self[key]]: 
            del self.inverse[self[key]]
        super(bidict, self).__delitem__(key)


cesar_cypher = bidict({
'A': 0, 
'B': 1, 
'C': 2,
'D': 3,
'E': 4,
'F': 5,
'G': 6,
'H': 7,
'I': 8,
'J': 9,
'K': 10,
'L': 11,
'M': 12,
'N': 13,
'O': 14,
'P': 15,
'Q': 16,
'R': 17,
'S': 18,
'T': 19,
'U': 20,
'V': 21,
'W': 22,
'X': 23,
'Y': 24,
'Z': 25,
})

def decrypt(plainText):
	cypher = list()

	for character in plainText:
		if (re.search(r"[A-Z]", character) is not None):
			cypher.append((cesar_cypher[character] - 23) % 26)
		else: 
			cypher.append(character)

	return cypher

def encrypt(plainText):
	cypher = list()

	for character in plainText:
		if (re.search(r"[A-Z]", character) is not None):
			cypher.append((cesar_cypher[character] + 23) % 26)
		else: 
			cypher.append(character)

	return cypher

def print_decypher(cypher):
	final_cypher = ''
	for character in cypher:
		if type(character) is int:		
			final_cypher += cesar_cypher.inverse[character][0]
		else: 
			final_cypher += character
	
	print('This is your cesar_cypher:')
	print(final_cypher)	

def print_cypher(cypher):
	final_cypher = ''
	for character in cypher:
	# TODO: Fix the type issue here. Probably not the best implementation		
		if type(character) is int:
			final_cypher += cesar_cypher.inverse[character][0]
		else:
		 final_cypher += character
	
	print('This is your cesar_cypher:')
	print(final_cypher)	


def get_text():
	print('Input your text: ')
	return input().upper()


def get_mode():
	print('Do you want to (E)ncrypt or (D)crypt?')
	return input().upper()

def main():
	correct_input = False
	
	while not correct_input:
		mode = get_mode()
		if (mode == 'E'):
			correct_input = True
			text = get_text()
			cypher = encrypt(text)
			print_cypher(cypher)
		elif (mode == 'D'):
			correct_input = True
			text = get_text()
			plainText = decrypt(text)
			print_decypher(plainText)
		else:
			print('Wrong input.')
	

if __name__ == "__main__":
    main()

