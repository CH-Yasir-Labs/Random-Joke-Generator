#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      chyas
#
# Created:     14/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        data = response.json()

        if data.get("error"):
            print("Sorry, no joke available at the moment.")
        else:
            print(f"Joke: {data['joke']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

def main():
    print("Welcome to the Random Joke Generator!")
    get_joke()

if __name__ == "__main__":
    main()
