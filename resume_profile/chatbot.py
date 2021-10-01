f="""name : My name is Pallav Semwal
Age : What's in the age , just a number.
Location : I'm Indian .
Education : Pursing Btech
major/ branch / stream / department in Btech : Electronics and Communication
Hobbies\ Passtime : Listening to Music and Playing Football
Interest : I'm an enthusiastic learner, I taken interest in learning new things , developing and working on new projects.
About \ Bio :Strong in design and integration with intuitive problem-solving skills. Proficient in C++, PYTHON, JAVASCRIPT, and SQL. Passionate about implementing and launching new projects
Programming Languages: Python, C++, Javascript, SQl.
Looking for , work experience , job oppurtunities: software engineer"""

m="""Projects , development work , personal projects : worked on various projects in technical domains like web devlopment, Data Science , Machine learning . You can check all by navigating to projects.
Academics , score , marks : Marks are just numbers but you can them in my profile
skills , proficieny , competency : full stack web development , data science , machine learning & ai, finance enthusiast
courses and certificates : You can check my profile for the same or go through my resume 
Responsibilites , organizations , experience : active participant in college commitees and club events . You can learn more in my resume.
Social profile , achievement , record : you can check my profiles on hackerrank , github and linkedin where I have all my certificates and achievement mentioned 
Fintech , Finance ,Economics : I'm passionate about learning and working with fintech. I have some projects on the same and I'm passionate about integrating it with tech"""

import nltk
import warnings
import threading
warnings.filterwarnings("ignore")
# nltk.download() # for downloading packages
# import tensorflow as tf
import numpy as np
import random
import string  # to process standard python strings

# f = open('\stock_database_chatbot.txt', 'r', errors='ignore')
# m = open('\technical_database_chatbot.txt', 'r', errors='ignore')
checkpoint = "./chatbot_weights.ckpt"
# session = tf.InteractiveSession()
# session.run(tf.global_variables_initializer())
# saver = tf.train.Saver()
# saver.restore(session, checkpoint)

raw = f
rawone = m
raw = raw.lower()  # converts to lowercase
rawone = rawone.lower()  # converts to lowercase
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)# converts to list of sentences
word_tokensone = nltk.word_tokenize(rawone)  # converts to list of words


lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is Virav, I'm pallav's assisant", "My name is Virav you can called me vir, I assist pallav..", "Im Virav :), I manage all the work for pallav. ",
                 "My name is Virav and my nickname is vir, I assist Pallav and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("About you ", "Your education ")
Basic_Ans = "You can go through my profile and resume to have a clear idea"
Basic_Om = ("Your projects", "Your skills")
Basic_AnsM = ["I have worked on many real life and personal projects which can be seen on my social platforms. You can navigate to projects to check them","I my skilled in Full stack web development , data analytics , developing and working with ML & AI models"]

# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans


# Checking for Basic_QM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)


# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# Generating response
def responseone(user_response):
    robo_response = ''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokensone[idx]
        return robo_response


def chat(user_response):
    user_response = user_response.lower()
    keyword = " skills"
    keywordone = " skills "
    keywordsecond = "skills "
    eyword = " projects "
    eywordone = " projects"
    eywordsecond = "projects "

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            # print("ROBO: You are welcome..")
            return "You are welcome.."
        elif (basicM(user_response) != None):
            return basicM(user_response)
        else:
            if (user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(
                    keywordsecond) != -1 or user_response.find(eyword) != -1 or user_response.find(eywordone) != -1 or user_response.find(
                    eywordsecond) != -1):
                # print("ROBO: ",end="")
                # print(responseone(user_response))

                return responseone(user_response)

            elif (greeting(user_response) != None):
                # print("ROBO: "+greeting(user_response))
                return greeting(user_response)
            elif (user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find(
                    "your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif (basic(user_response) != None):
                return basic(user_response)
            else:
                # print("ROBO: ",end="")
                # print(response(user_response))

                return response(user_response)


    else:
        flag = False
        # print("ROBO: Bye! take care..")
        return "Bye! take care.."

if __name__ == "__main__":
    def receive():
        while True:
            x=input()
            if not x:
                break
            print(chat(x))
    receive_thread =threading.Thread(target=receive)
    receive_thread.start()