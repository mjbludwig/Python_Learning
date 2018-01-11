def match_ends(words):
        wordlist = [words]
        totalwords = 0
	for stringin in wordlist:
		 if stringin >= 2 and stringin[0] == stringin[-1]:
                        totalwords += 1
                else:
                        continue
                        return totalwords
def main():
	match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
	match_ends(['', 'x', 'xy', 'xyx', 'xx'])
if __name__ == '__main__':
	main()
