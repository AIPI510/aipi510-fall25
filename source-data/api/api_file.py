import requests 
import json
import pandas as pd 

#make get request for joke api
#loop through the responses and create dataframe
jokes = []
for _ in range(5):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke = json.loads(response.text)
    jokes.append(joke)

#parse the json response
for joke in jokes:
    print(f"{joke['setup']} - {joke['punchline']}")
print("="*50)

#create dataframe with all jokes
df = pd.DataFrame(jokes)
print("\nAll jokes in DataFrame:")
print(df)

#essentially what this code does is it retreives random jokes from the joke api, converts the json response into a python dictionary,
#prints the response in a way that its just the setup followed by the punchline
#and then also stores the 5 jokes we retrieve in a dataframe with type, setup, punchline, and ID


