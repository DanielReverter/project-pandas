# W2 Project - Data cleaning and wrangling
​
## Premise
​
In this project I assume that a large company is in the early stages of a new project. They want to hire me as a data analyst to collect information on whether a leg protection device would be appealing to surfers in places with a large number of shark attacks.
​
## Hypothesis
​
This project will attempt to prove whether a leg protection device is necessary for surfers, by checking the frequecy of surfing-related leg injuries versus other shark attacks. The data provided includes over 6,300 unique shark attacks ranging from fishing to standing in the water.  
​
## Project files
​
The main directory has 3 subdirectories:
* Input: Hidden in GitHub, the input folder has the data used to analyze our hypothesis. It is a file containing most recorded shark attacks (anywhere in the world and as far back in time as classic Greece). The file can be downloaded and seen at https://www.kaggle.com/teajay/global-shark-attacks
* Output: Contains files created from the original data (new datasets, plots, etc.) that are used multiple times through the project.
* src: Contains python files with all the functions created by myself.
​
In the root directory there are 4 jupyter notebook files that include all the code used in the project but the functions in src directory:
* eda: Stands for "Exploratory data analysis". In this file I just explore the data (how much data I have, how is it organized and the quality of it).
* Cleaning: In this file I get rid of some of the data that I won't use and I standarize the way that the data I use is written so it's easier to work with later. I also categorize some of the data in a useful way.
* Analysis: Here I check whether my hypothesis is true or not.
* Visualization: In the last file I create plots that help visualize the data used to check my hypothesis and a small market analysis in case that the company decides to move forward with its project.
​
## Conclusion
​
After analysing the data I conclude that a leg protection should be more appealing to surfers in places where there have been shark attacks than to non-surfers in those same places, and that this same data could be used to persuade those surfers into buying it. I also conclude that the market target for these devices should be young men (teens to mid thirties). There is no conclusion on whether this project would be ecoonomically viable or not, that should be explored as another hypothesis with an economic related set of data in a later stage of the companies project.