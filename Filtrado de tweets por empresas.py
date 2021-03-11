# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:28:55 2021

@author: pallo
"""
import pandas as pd

df= pd.read_csv("Tweet.csv")

def keyword(mensaje):
    key1="amazon"
    palabras=set((mensaje).lower().split())
    if key1 in palabras:
        return 1
    else:
        return 0
    
df["keyword"]=df["body"].apply(keyword)

df= df[df["keyword"] > 0]

df.to_csv("amazon_tweets.csv")

input()
