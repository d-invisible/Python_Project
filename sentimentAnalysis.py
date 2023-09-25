from textblob import TextBlob
import pyttsx3
review=TextBlob(input("Enter review : " ))
value=review.sentiment.polarity
print(f"positivity : {round(value,2)}")

if value>0:
    print("Great, Thanks for your response !")
    pyttsx3.speak("I will speak this text,Thanks for your response ! We will continue deliver the same good work")
else:
    print("Okay, Thanks for your response !")
    pyttsx3.speak("I will speak this text,Thanks for your response ! We will try to deliver service better")
