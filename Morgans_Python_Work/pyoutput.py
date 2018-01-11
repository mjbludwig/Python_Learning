def main():
	outputfile = open('pyoutput.txt', 'a')
	for i in range(100):
		thisnum = i
		outputfile.write('%d \n' % i)
	outputfile.close()

if __name__ == '__main__':
	main()
