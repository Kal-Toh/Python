print("Welcome to LEET Translator. Please type in lowercase: ")
Transdata = input("Enter text: \n")
Trans_a = (Transdata.replace('a', '@'))
Trans_c = (Trans_a.replace('c', '('))
Trans_e = (Trans_c.replace('e', '3'))
Trans_h = (Trans_e.replace('h', '#'))
Trans_i = (Trans_h.replace('i', '1'))
Trans_o = (Trans_i.replace('o', '0'))
Trans_s = (Trans_o.replace('s', '5'))
Trans_t = (Trans_s.replace('t', '7'))
Trans_v = (Trans_t.replace('v','\/'))
print(Trans_v.upper())
