# Project Name: Voice Assistant 🎤✨

## Overview

Welcome to the Voice Assistant project! This Python-based voice assistant allows users to perform various tasks using voice commands. The assistant leverages speech recognition, web scraping, and automation functionalities to provide a hands-free experience.

## Features

- **Speech Recognition:** Converts spoken words into text.
- **Text-to-Speech:** Reads out responses and information.
- **Web Actions:** Opens websites, performs searches, and interacts with web applications.
- **Application Control:** Opens and closes applications based on voice commands.
- **System Control:** Manages windows, tabs, and performs basic text editing commands.
- **Automation:** Sends WhatsApp messages, makes calls, captures screenshots, and more.
- **Information Retrieval:** Fetches information from Wikipedia, tells jokes, and provides the latest news.
- **Geolocation:** Finds the location of a place on Google Maps.

## Getting Started

### Prerequisites

- Python 3.x
- Install required packages

### Usage

1. Run the script: `voice-assistant.py`
2. Wait for the "Listening" prompt.
3. Give voice commands to perform various tasks.

## Dependencies

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [geopy](https://pypi.org/project/geopy/)
- [wikipedia-api](https://pypi.org/project/Wikipedia-API/)
- [AppOpener](https://pypi.org/project/appopener/)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [pyjokes](https://pypi.org/project/pyjokes/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)
  
## Code Explanation

Let's break down the key sections of the code:

### User Interface (UI)

The script initializes a simple PyQt5-based GUI to display the assistant's listening status.

### Speech Recognition

The script uses the speech recognizer library to instantiate the recognizer and microphone classes.

### Text to Speech

The code creates an engine using pyttsx3 module and the properties of the engine are set.

### App Control

The script uses the AppOpener library to open and close apps. The input can be 'open app app_name' or 'close app app_name'. The given commands will open or close a given app respectively.

### Keyboard Control

PyautoGui library is used to control the user's keyboard for performing functions such as closing windows,closing browser tabs,typing,copying,pasting,selecting text etc.

### Web browser control

The webbrowser library is used to open websites. The user can give a command such as 'open website_name' to open the website.

### Youtube access

The code uses the playonyt function in the pywhatkit library to directly access Youtube and play videos. The user can access the video by just saying 'youtube search video_name'.

### Texting and calling

The script can send whatsapp messages and call on whatsapp using the pywhatkit and pyautogui library respectively. The call functionality will not work for all laptops/monitors currently as it is designed to work for a specific aspect ratio.The ratio it is configured to work in is a 15.6 inch screen with a 16:10 aspect ratio.

### Wikipedia Access

The script can answer any question using Wikipedia. The user can simpky ask any question that starts with 'what is' or 'who is'.

### Location

The script can provide the location of any place using the geolocator library. We are passing the latitude and longitude to google maps to display the result. To know the location of the place the user can simply start the sentence with 'location of'.

### Latest News

The code can read the latest news out to the user. In this case the number of news headlines to be reaad has been set to 5 but can be changed based on the users need. To access the latest news, the user can just say 'latest news'.
