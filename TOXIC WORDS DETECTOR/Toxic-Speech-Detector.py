import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as Source:
    print('Speak anything')
    audio = r.listen(Source)
    try:
      text=r.recognize_google(audio)
      print("You said:{}".format(text))
      list1 = list(text.split(" "))
      my_file=open("bad-words.txt","r")
      data=my_file.read()
      list2=data.split("\n")
      list = set(list1) & set(list2)
      lists=str(list)[1:-1]
      list3=[]
      for i in list1:
          if i[-1]=="*":
              list3.append(i)
      print("Google detected toxic words count:",len(list3))
      print("Matched bad-words:", lists)
      countlist = len(list)+len(list3)
      print("Words count:", countlist)
      print("Bad-Words %:",(countlist/len(list1))*100)
    except:
      print("Sorry!try again")


