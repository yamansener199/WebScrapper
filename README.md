# WebScrapper

██╗░░░██╗███╗░░░███╗███╗░░██╗░███████╗
╚██╗░██╔╝████╗░████║████╗░██║██╔██╔══╝
░╚████╔╝░██╔████╔██║██╔██╗██║╚██████╗░
░░╚██╔╝░░██║╚██╔╝██║██║╚████║░╚═██╔██╗
░░░██║░░░██║░╚═╝░██║██║░╚███║███████╔╝
░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚══════╝░
Basic Web Scrapping Tool Developed With Python And Javascript
🔗linkedin.com/in/yaman-şener-03b284200
Created by 👽 YamanŞener 24/05/2021
URL of the report :https://docs.google.com/spreadsheets/d/1vY6aAdGZ5wOF8peHqiS-qhmSjcesh_w9ER-IX0gApj8/edit#gid=0
I like to live with data 🥇
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Challenges](#paragraph1)  
* [What I Learned](#paragraph2)
* [Question Answers](#paragraph3)  

## General info 
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:
* Python 3.9 
* Javascript 
* Google Sheets 
* Google Apps Script
* Pandas Library
* Gspread Library
* BeautifulSoup Library

	
## Setup 🍸🍸🍸
To run this project, install it locally using npm:

```
$ cd "path_where_you_want_to_clone"
$ git clone "git_link"
$ pip install gspread
$ pip install pandas
$ pip install BeautifulSoup
$ pip install requests
$ pip install python-time
$ python3 main.py //run command can change depending on the Os 
```
## Challenges <a name="paragraph1"/>🩸🩸🩸
While I was developing the project , I faced with different problems such as request timeouts.First day of the project was very hard because I spend a few hours to decide which language I should use.I decided on using python because I already made a project with selenium for a different purpose.While I was sending requests , I faced with a timeout problem Error 404 which show that sometimes sending too many requests result with get banned from a site a short time.I changed my mac and ip adresses to continue parsing the proper links 2 times.I tried with a linux machine to get requests from another local network and then I continued to work with that.Due to firewall configurations (my interpretations) I migh catagorized as danger by the firewwall.I tried to make nmap scan to undertand if there is any.Because we have 1000 links, my compilation time took more than I expect.I already came up with a solution for it and I would like to implement the multi-threaded version of this project in the future.I was also facing with other problems such as idetifying the thml structure.Because of the size of html files displaying on the browser , I spend a lot of minutes identifying the needed components.

## What I Learned <a name="paragraph2"/>🩸🩸🩸
While I was developing this project , I learned how to use BeautifulSoup library.On purpose , I wanted to use another library having the same fucntionalities as selenium.I wanted to develop myself with a new library for self-development and I got a little bit surprised by the functionalities that Soup brings.It was awosome !.Moreover , I also learned taht sending request take so much time for huge amount of links.So I found a new solution to taht part as well by developing a upgraded version of this project with multi-threads.In addition to that , I already used the Google Sheets for forming .csv files for my ML and AI courses.But the most fascinating part was teh usage of Apps Script.I was my first time using it with an external code based project.I really liked the suage of apps script and I will be coninuing to use it after now !

## Question Answers <a name="paragraph3"/> 🩸🩸🩸
1. If I’d have 10.000 urls that I should visit, then it takes hours to finish.
What can we make to fasten this process?
🥇Answer:Shortly , we can use paralellism ideology to work more faster with these codes and it is also based on threads.A thread is essentially a separate execution flow. Multiple threads can be found in a single operation. Each thread in a program is responsible for completing a specific task. For example, when you play COD on your PC, the game as a whole is a single operation, but it is made up of several threads that are responsible for playing music, taking user feedback, synchronously running the opponent, and so on.In general, multitasking refers to the ability to complete several tasks at the same time. In technical terms, multitasking refers to an operating system's ability to execute several tasks at once. For example, suppose you're downloading something on your PC while still listening to music and playing a game. All of these functions are carried out by the same operating system and are in sync.So with this ideology we can built our program better and more efficient.In addition to that if we can be able to use a Db system it is going to be helping us to run the program faster becasue NoSql Db'S has a faster built-in based on a Bson Object.I might help :) !
2. What can we make or use to automate this process to run once a
day?Write your recommendations.
🥇Answer:So basically we can use this program to compile systematically depending on the time lapses we will be deciding.For this purpose , we can use cron jobs.I used cron jobs for aggregate tables to different Db's on my previous projects.Let's assume that we have 100.000 links , we first need to divide the big data into small chunks to work more faster.We need setup the cron job on a server or a computer(I used servers based on ISX OS on my projects).Then with small scripts we can run the program daily, weekly or monthly on the server.Cron jobs will be suiting perfectly for this kind of problems.
3. Please briefly explain what an API is and how it works.
🥇Answer:To describe an API it is better demonstrate it with an example.So ,consider yourself a customer, a bank teller as an API, and the bank as the device with which you communicate. When you wish to withdraw money from your account, you approach the teller(API) and tell them, "I'd like to take out  1,000 TL from this account".The teller (API) then goes to the back and informs the bank manager (the system) that "Mr/Ms.X would like 1,000 TL to account" and the bank manager (the system) sends the teller (API) 1,000 TL, which you finally get. If you will see, the API serves as a conduit between you and the machine.Same with the Google Sheets and Apps Script functionalities.We used thse two methods to easliy modify and process our datas with basic script language codes.
