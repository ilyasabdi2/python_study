text='  jOHn   ' # to jonh

text=text.strip().capitalize()
print(text)

sentence_one = "The Dog Breed is German Shepherd"
print(sentence_one[8:23]) 

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_two[16:30])


sentence = "The lazy dog; ran so fast; it hit the wall."

# Split the sentence using the semicolon as the delimiter
result = sentence.split(";")
print(len(result))

# Display the resulting list and its length


#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe

first_name = "  Joh.n"
last_name = "   Do,e"

first = first_name.strip().replace(".", "")
print(first)
last = last_name.strip().replace(",", "")
print(last)

full_name=first+" "+last
print(full_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC

r= ["E","W","C"]
r=text.replace(",","")
r=text.replace('"','')
r=text.replace("[]","")
print(r)






