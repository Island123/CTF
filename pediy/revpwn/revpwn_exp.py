target = [0x09,0x00,0x00,0x00,0x0D,0x00,0x00,0x00,0x0B,0x00,0x00,0x00,0x00,0x00,0x00,0x00,\
0x08,0x00,0x00,0x00,0x04,0x00,0x00,0x00,0x0A,0x00,0x00,0x00,0x0C,0x00,0x00,0x00]
i=0

def cal(sum):
	a = [0,1]
	for a0 in a:
		for a1 in a:
			for a2 in a:
				for a3 in a:
					if 8*a0+4*a1+2*a2+a3 == sum:
						return a0,a1,a2,a3

for num in target:
	i+=1
	print num
	a0,a1,a2,a3 = cal(num)
	if i%2==1:		
		print [a0,a1,a2,a3]