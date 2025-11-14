#

#! Probability Object
probject = {
     "a": 8.2,
     "b": 1.5,
     "c": 2.8,
     "d": 4.3,
     "e": 12.7,
     "f": 2.2,
     "g": 2.0,
     "h": 6.1,
     "i": 7.0,
     "j": 0.16,
     "k": 0.77,
     "l": 4.0,
     "m": 2.4,
     "n": 6.7,
     "o": 7.5,
     "p": 1.9,
     "q": 0.12,
     "r": 6.0,
     "s": 6.3,
     "t": 9.1,
     "u": 2.8,
     "v": 0.98,
     "w": 2.4,
     "x": 0.15,
     "y": 2.0,
     "z": 0.074
}

#! Probabilistic Frequency Analysis Function
#* Helper functions
def shiftObject(obj, shift):
     """Gives n-th char of the input object (n - shift)th value in that same object
     
     Only works for uppercase chars"""

     newObject = {}
     for char in obj:
          newObject[char] = obj[chr((ord(char) + shift - 97) % 26 + 97)]
     return newObject

def ratePrecision(obj, shift):
     """Returns a confidence number that the text has been shifted by caesar cipher by {shift} amount of times

     (the scale has nothing to do with percentages or any otherknown scale)"""

     # porovnat procentuelní výskyt jednotlivých písmena z probject posunuté o shift s procentuélním výskytem v textFrequency
     shiftedLexicalObject = shiftObject(probject, shift)
     error = 0
     for char in shiftedLexicalObject:
          if char in obj:
               inTextAppearance = obj[char]
          else:
               inTextAppearance = 0

          error += abs(inTextAppearance - shiftedLexicalObject[char])
     return 100 - error

def findHighest(inputObject):
     """Finds highest value in an object (in Python dictionary) and returns it in the form of tuple ("key", value)"""

     highestValue = 0

     for char in inputObject:
          if inputObject[char] > highestValue:
               highestValue = inputObject[char]
               highestDuo = (str(char), inputObject[char])
     return highestDuo

def freq_analysis(text):
     frequencyObject = {}

     # frequency
     for char in text:
          lowerChar = char.lower()
          if not lowerChar.isalnum():
               continue
          if lowerChar in frequencyObject:
               frequencyObject[lowerChar] += 1
          else:
               frequencyObject[lowerChar] = 1

     # sort
     result = {}
     for i in range(len(frequencyObject)):
          highestTuple = findHighest(frequencyObject)
          result[highestTuple[0]] = highestTuple[1]
          frequencyObject.pop(highestTuple[0])

     # output
     return result

def caesar(text, shift):
     array = []
     for char in text:
          if char.islower():
               codedChar = chr((ord(char) + shift - 97) % 26 + 97)
          elif char.isupper():
               codedChar = chr((ord(char) + shift - 65) % 26 + 65)
          else:
               codedChar = char
          array.append(codedChar)
     return "".join(array)

#* Main function
def caesar_frequency_analysis(text):
     # find number of appearances of chars in text
     results = {}
     textFrequency = freq_analysis(text)

     # convert to %
     totalLetters = 0
     for char in text:
          if char.isalpha():
               totalLetters += 1

     for char in textFrequency:
          percentageValue = textFrequency[char] / totalLetters * 100
          textFrequency[char] = percentageValue

     # calculate confidence in each possible shift of the set of english letters
     for i in range(0, 26):
          results[i] = ratePrecision(textFrequency, i)

     mostProbable = findHighest(results)
     print(f"shift: {26 - int(mostProbable[0])}")
     print(f"confidence (not in %): {round(mostProbable[1], 1)}")
     print(f"Most probable outcome: {caesar(text, int(mostProbable[0]))}")
     return results

caesar_frequency_analysis("Wkh Looxplqdwl—dorqj zlwk Iuhhpdvrqub dqg rwkhu vhfuhw vrflhwlhv—zhuh rxwodzhg wkurxjk hglfw eb Fkduohv Wkhrgruh, Hohfwru ri Edyduld, zlwk wkh hqfrxudjhphqw ri wkh Fdwkrolf Fkxufk, lq 1784, 1785, 1787 dqg 1790.[3] Gxulqj vxevhtxhqw bhduv, wkh jurxs zdv jhqhudoob ylolilhg eb frqvhuydwlyh dqg uholjlrxv fulwlfv, zkr fodlphg wkdw wkh Looxplqdwl frqwlqxhg xqghujurxqg dqg zhuh uhvsrqvleoh iru wkh Iuhqfk Uhyroxwlrq. Lw dwwudfwhg olwhudub phq vxfk dv Mrkdqq Zroijdqj yrq Jrhwkh dqg Mrkdqq Jrwwiulhg Khughu dqg wkh uhljqlqj Gxnh ri Jrwkd dqg ri Zhlpdu.")
caesar_frequency_analysis("Clguba vf n irel hfrshy cebtenzzvat ynathntr. Naq ubj fvzcyr vg vf... V ybir vg!")
caesar_frequency_analysis("Aopz pz h zptwsl alza tlzzhnl av joljr fvby Jhlzhy zvslly.")
caesar_frequency_analysis("Yizxnlrxh uhthbcr hp ocq rholxkoxl yhk uyltdbfz lnbmshlzngf vbgylkl.")
caesar_frequency_analysis("Rsxlmrk mw qsvi jyr xler xiwxmrk csyv hibvctxmsr epkvsmlq.")