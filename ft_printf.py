code = """++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>.>---.++++++++++++.++.+++
+++.--.<<++.>>------.------------.+++++++++++++.<<.>>++++++.------------
.-------. +++++++++++++++++++.<<.>>----------------.+++++.+++++++++.---
----------.--.+ ++++++++++++++++.--------.+++++++++++++.<<.>>----------
-------------.+++.+++ ++++.---.----.+++++++++++++++++.---------------
--.-.<<.>>+++++.+++++.<<.>-------..."""

SIZE = 10000

memory = [0 for i in range(SIZE)]
mem_ptr = 0
p = 0
len = len(code)
while p < len:
	if code[p] == '+':
		memory[mem_ptr] += 1
		memory[mem_ptr] %= 256
		p += 1
	elif code[p] == '-':
		memory[mem_ptr] -= 1
		memory[mem_ptr] %= 256
		p += 1
	elif code[p] == '<':
		mem_ptr = (mem_ptr - 1) % SIZE
		p += 1
	elif code[p] == '>':
		mem_ptr = (mem_ptr + 1) % SIZE
		p += 1
	elif code[p] == '.':
		print(chr(memory[mem_ptr]), end = "")
		p += 1
	elif code[p] == '[':
		if memory[mem_ptr] == 0:
			idx = -1
			count = 0
			for i in range(p + 1, SIZE):
				if code[i] == '[':
					count += 1
				elif code[i] == ']':
					if count == 0:
						idx = i
						break
					else:
						count -= 1
			if idx == -1:
				print(f"error missing closing bracket pos {p}")
				exit(1)
			p = idx + 1
		else:
			p += 1
	elif code[p] == ']':
		if memory[mem_ptr] != 0:
			idx = -1
			count = 0
			for i in range(p - 1, -1, -1):
				if code[i] == ']':
					count += 1
				elif code[i] == '[':
					if count == 0:
						idx = i
						break
					else:
						count -= 1
			if idx == -1:
				print(f"error missing opening bracket pos {p}")
				exit(1)
			p = idx + 1
		else:
			p += 1
	else:
		p += 1
print()
