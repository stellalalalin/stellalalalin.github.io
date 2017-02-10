'''
Names: Stella Lin and Spencer Wright
Project: Data Project (35)
'''

import os.path
import matplotlib.pyplot as plt

print("Please choose a crime") 
print("1. Murder")
print("2. Rape")
print("3. Robbery")
print("4. Assault")

# Asks user for specific crime
crime = int(input(""))

directory = os.path.dirname(os.path.abspath(__file__))  

# Initializes aggregators
murders = []
rapes = []
robberies = []
assaults = []
years = []
revenues = []

# Takes user input and shows data for murder
if crime == 1:
    
    # Open the file
    filename = os.path.join(directory, "Crime.csv")
    datafile = open(filename, 'r')
    data = datafile.readlines()
   
    for line in data: 

        year, murder, rape, robbery, assault, revenue = line.split(',')
        # Aggregate values to list based on user input for crime, in this case murder
        murders += [murder]
        years += [year]
        revenues += [revenue]

    # Plot on two sets of axes           
    fig, ax = plt.subplots(2,1)
    ax[0].plot(years, murders,'#FF0000')
    ax[1].plot(years, revenues,'#00FF00')
 
    ax[0].set_title('Murder Rate')
    ax[1].set_title('Video Game Market Revenue (In Billions)')
    fig.show() # Show graph

# Takes user input and shows data for rape        
if crime == 2:
    
    # Open the file
    filename = os.path.join(directory, "Crime.csv")
    datafile = open(filename, 'r')
    data = datafile.readlines()
   
    for line in data: 

        year, murder, rape, robbery, assault, revenue = line.split(',')
        # Aggregate values to list based on user input for crime, in this case rape
        rapes += [rape]
        years += [year]
        revenues += [revenue]
    
    # Plot on two sets of axes       
    fig, ax = plt.subplots(2,1)
    ax[0].plot(years, rapes,'#FF0000')
    ax[1].plot(years, revenues,'#00FF00')
    
    ax[0].set_title('Rate of Forcible Rape')
    ax[1].set_title('Video Game Market Revenue (In Billions)')
    fig.show() # Show graph
  
# Takes user input and shows data for robbery             
if crime == 3:
    
    # Open the file
    filename = os.path.join(directory, "Crime.csv")
    datafile = open(filename, 'r')
    data = datafile.readlines()
    
    for line in data: 

        year, murder, rape, robbery, assault, revenue = line.split(',')
        # Aggregate values to list based on user input for crime, in this case robbery
        robberies += [robbery]
        years += [year]
        revenues += [revenue]
       
    # Plot on two sets of axes        
    fig, ax = plt.subplots(2,1)
    ax[0].plot(years, robberies,'#FF0000')
    ax[1].plot(years, revenues,'#00FF00')
    
    ax[0].set_title('Robbery Rate')
    ax[1].set_title('Video Game Market Revenue (In Billions)')
    fig.show() # Show graph

# Takes user input and shows data for assault
if crime == 4:
    
    # Open the file
    filename = os.path.join(directory, "Crime.csv")
    datafile = open(filename, 'r')
    data = datafile.readlines()
   
    for line in data: 

        year, murder, rape, robbery, assault, revenue = line.split(',')
        # Aggregate values to list based on user input for crime, in this case assault
        assaults += [assault]
        years += [year]
        revenues += [revenue]
    
    # Plot on two sets of axes        
    fig, ax = plt.subplots(2,1)
    ax[0].plot(years, assaults,'#FF0000')
    ax[1].plot(years, revenues,'#00FF00')
    
    ax[0].set_title('Aggravated Assault Rate')
    ax[1].set_title('Video Game Market Revenue (In Billions)')
    fig.show() # Show graph