# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:05:40 2020

@author: uasmt
"""


import requests

api_key = "<apikey>"

class theMovieDb:
    def __init__(self,api_key):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = api_key
        
    def getPopulerMovies(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def nowPlaying(self):
        response = requests.get(f"{self.api_url}/movie/now_playing?api_key={self.api_key}&language=en-US&page=1")
        return response.json()
    
    def search(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&language=en-US&page=1")
        return response.json()
    
movieApi = theMovieDb(api_key)

while True:
    
    choice = input(" 1- Populer Movies\n 2 - Now Playing Movies \n 3 - Search \n Enter any number to exit \n Choice:")
    
    if choice=="1":
        result = movieApi.getPopulerMovies()
        for movie in result['results']:
            print(movie['title'])
        
    elif choice=="2":
        result = movieApi.nowPlaying()
        for movie in result['results']:
            print(movie['title'])
    elif choice=="3":
        keyword = input("Keyword : ")
        result = movieApi.search(keyword)
        for movie in result['results']:
            print(movie['name']) 
    else:
        print("Exited")
        break