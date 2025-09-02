import requests
import json
import pandas as pd
from jokeapi import Jokes # Import the Jokes class


def joking():
    joke=requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist,explicit")
    joke_json = joke.json()
    df = pd.json_normalize(joke_json)
    df = df.T
    print(df)
    print(df.loc["joke", 0])

joking()

### This python file queries and requests a joke and outputs a pd file that splits up the joke into all it's components and files
### Moreover I stopped it from providing anything NSFW including racist, sexist, and explicit jokes.
### The joke itself is stored in the "joke" section of the dictionary

### Output
#                                                                 0
#error                                                        False
#category                                               Programming
#type                                                        single
#joke                       ASCII silly question, get a silly ANSI.
#id                                                             220
#safe                                                          True
#lang                                                            en
#flags.nsfw                                                   False
#flags.religious                                              False
#flags.political                                              False
#flags.racist                                                 False
#flags.sexist                                                 False
#flags.explicit                                               False
# ASCII silly question, get a silly ANSI.