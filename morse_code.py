encode_doc = {"a":".-",
		"b":"-...",
		"c":"-.-.",
		"d":"-..",
		"e":".",
		"f":"..-.",
		"g":"--.",
		"h":"....",
		"i":"..",
		"j":".---",
		"k":"-.-",
		"l":".-..",
		"m":"--",
		"n":"-.",
		"o":"---",
		"p":".--.",
		"q":"--.-",
		"r":".-.",
		"s":"...",
		"t":"-",
		"u":"..-",
		"v":"...-",
		"w":".--",
		"x":"-..-",
		"y":"-.--",
		"z":"--..",
		" ":" "
		}

decode_doc = {".-":"a",
			  "-...":"b",
			  "-.-.":"c",
			  "-..":"d",
		 	  ".":"e",
			  "..-.":"f",
			  "--.":"g",
			  "....":"h",
 	          "..":"i",
			  ".---":"j",
			  "-.-":"k",
			  ".-..":"l",
			  "--":"m",
		 	  "-.":"n",
			  "---":"o",
			  ".--.":"p",
			  "--.-":"q",
			  ".-.":"r",
			  "...":"s",
			  "-":"t",
			  "..-":"u",
			  "...-":"v",
			  ".--":"w",
			  "-..-":"x",
			  "-.--":"y",
			  "--..":"z",
			  " ":" "
			  }
def encoder():                      #type to morse
	word = input()
	for i in range(0,len(word)):
		print(encode_doc[word[i]])

def decoder():                      #morse to type
	print(decode_doc)
	word = []
	while True:
		code = input()
		if code == "0":
			break
		letter = decode_doc[code]
		word.append(letter)
	print(word)

def main():                          #select one of these and run, decode or encode
	option = input("Decode or Encode ?\n")
	if option == "Decode" or "decode" or "d":
		decoder()
	elif option == "Encode" or "encode" or "e":
		encoder()

main()

input("done\npress enter key to exit")

