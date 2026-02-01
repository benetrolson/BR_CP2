#BHR 2nd morse code translator
#Add the morse code key
morse_code = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  " ": "|",
  " ": "/"
}

#Create the main section of the code
def main(morse_code):
  while True:
    check = input("Do you want to: \n1. Translate the Morse Code to English \n2. Translate English to Morse Code \n3. Quit \n")
    if check == "1":
      morse_to_english({value: key for key, value in morse_code.items()})
    elif check == "2":
      english_to_morse(morse_code)
    elif check == "3":
      break
    else:
      print("You did not input an option. Please try again. ")

#Create the function for translating from morse to english
def morse_to_english(morse_code):
  message = ""
  code = input("Could you please input the morse code using periods and dashes? Please use '|' as spaces. There will be no punctuation. ")
  words = code.strip().split("|")
  for word in words:
    letters = word.strip().split(" ")
    for letter in letters:
      if letter in morse_code:
        message += morse_code[letter]
    message += " "
  print(message.strip())

#Create the function for translating from english to morse
def english_to_morse(morse_code):
  english = input("What is the code you need translated? Please don't use punctuation. ").lower()
  code = ""
  for letter in english:
    if letter in morse_code:
      code += morse_code[letter] + " "
  print(code.strip())

main(morse_code)
