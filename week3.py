import csv
import math
import statistics as st
from sorting_algorithms import bubble_sort

def get_maximum_value(list):
    '''
    given a list of numbers this function will return the greatest value
    
        :param list: the list of numbers given as input
        :return: the maximum value in the list 
    '''
    maximum = list[0] 
    for l in list:
        if l > maximum: 
            maximum = l
    return maximum

def get_minimum_value(list): 
    '''
    given a list of numbers this function will return the minimum value
    
        :param list: the list of numbers given as input
        :return: the minimum value in the list 
    '''
    minimum = list[0]
    for l in list:
        if l < minimum:
            minimum = l
    return minimum

def get_average(list): 
    """
    Given a list of numbers as input this function will return the numerical average.
    
        :param list: the list of numbers given as input
        :return: the numerical average of the list 
    """
    total = 0
    for l in list:
        total += l
    average = total / len(list) 
    return average

def get_median_value(list):
    '''
    given a list of numbers this function will return the median value
    
        :param list: the list of numbers given as input
        :return: the median value in the list 
    '''
    list1 = list.copy() 
    bubble_sort(list1)
    median = list1[int(len(list1)/2)] 
    return median

def bubble_sort(list1):
    for i in range(0,len(list1)-1): 
        for j in range(len(list1)-1):
            if(list1[j]>list1[j+1]): 
                temp = list1[j]
                list1[j] = list1[j+1] 
                list1[j+1] = temp

def get_mode(list):
    '''
    given a list of numbers this function will return the mode value
    
        :param list: the list of numbers given as input
        :return: the mode of the list 
    '''
    highest_freq = 0 
    mode = scores[0]
    for score in scores:
        frequency = 0
        for score2 in scores: 
            if score == score2:
                frequency += 1
        if frequency > highest_freq:
            mode = score 
            highest_freq = frequency
    return mode

def read_scores_from_csv(filename): 
    scores = []
    with open(filename , mode ="r") as file: 
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            score = int(lines["Score"]) 
            scores.append(score)
    print(scores)
    return scores

def read_student_number_from_csv(filename):
    student_nos = []
    with open(filename , mode ="r") as file: 
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            student_no = int(lines["Student Number"]) 
            student_nos.append(student_no)
    return student_nos

if __name__ == "__main__":
    scores = read_scores_from_csv("example.csv")
    student_nos = read_student_number_from_csv("example.csv")
    average = st.mean(scores)
    minimum = min(scores)
    maximum = max(scores) 
    median = st.median(scores)
    mode = st.mode(scores)
    
    print(f"Student Numbers = {student_nos}")
    print(f"Average: {average} Median: {median} Smallest: {minimum} Largest: {maximum} mode: {mode}")