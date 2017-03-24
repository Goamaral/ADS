import hashlib

def hashNumber(input):
	return int(hashlib.sha1(input).hexdigest(),16)
