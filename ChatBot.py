#Written by Gemechis Elias https://t.me/official_gemechis


from tkinter import *                       
from random import choice                       
                                    

                                                                    
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
Label(root, text=" Python ChatBot ").pack()
Label(root, text="     ").pack()
Label(root, text="     ").pack()             
root.title(" Simple ChatBot ")                  
Label(root, text=" Say Something: ").pack()                
Entry(root, textvariable=user).pack()          
Label(root, text=" Bot : ").pack()                
Entry(root, textvariable=bot).pack()               
                            
                                
def main():
       question = user.get()     #assign user input to varianle "question"
       user_name = [ "Gemechis"] #you can define known person to bot :)
       known_person = ["hi, Gemechis  how are u "]   #bot reaction for define person
       user_first_input = ["hi", "hello"]   
       bot_ask_name = ["hi, what  is you name "]
       bot_greeting = ["Hello "+question, "Hi "+question, "How are you "+question]
       user_ans = ["fine", "good","am fine"]
       bot_ans = ["wow glad yo hear this :)"]
       error = ["what did you say ?"]

                             
       if question in user_first_input:                      
            bot.set(choice(bot_ask_name))
       elif question in user_name:
             bot.set(choice(known_person))
       elif question not in user_name:
       	user_name.append(question)
       	bot.set(choice(bot_greeting))
       	del user_name[1]
       	if question in user_ans:
       		bot.set(choice(bot_ans))
       else:
       	
       	bot.set(choice(error))
                           
                                
Label(root, text="     ").pack()
Button(root, text="Send", command=main).pack()        
                                    
mainloop()