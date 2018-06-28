#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:39:03 2018

@author: oanainel
"""

import os


def compute_P(tp, fp):
    if tp == 0:
        return 0
    return float(tp) / float(tp + fp)


def compute_R(tp, fn):
    if tp == 0:
        return 0
    return float(tp) / float(tp + fn)

def compute_A(tp, tn, fp, fn):
    if tp + tn == 0:
        return 0
    return float(tp + tn) / float(tp + tn + fp + fn)

def compute_F1(p, r):
    if p * r == 0:
        return 0
    return float(2 * p * r) / float(p + r)
    


def compute_crowd_performance(crowd_results, output_directory, crowd_score):
    rows = []
    header = ["Thresh", "TP", "TN", "FP", "FN", "Precision", "Recall", "Accuracy", "F1-score"]
    rows.append(header)
    
    for i in range(5, 101, 5):
        row = []
        thresh = i / 100.0

        if not os.path.exists(output_directory + str(thresh) + "-pairs-directionality"):
            os.makedirs(output_directory + str(thresh) + "-pairs-directionality")
                    
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        
        for j in range(len(crowd_results.index)):
            if crowd_results["event-event_pair"].iloc[j] != "no_relation": # and crowd_results["no_of_annotations"].iloc[j] >= 7:
                if crowd_results[crowd_score].iloc[j] >= thresh:
                    if crowd_results["Experts"].iloc[j] == 1:
                        tp = tp + 1
                        
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-directionality/" + "tp_pairs_directionality.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
            
                    else:
                        fp = fp + 1
                            
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-directionality/" + "fp_pairs_directionality.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
                else:
                    if crowd_results["Experts"].iloc[j] == 1:
                        fn = fn + 1
                            
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-directionality/" + "fn_pairs_directionality.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
                            
                    else:
                        tn = tn + 1
                            
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-directionality/" + "tn_pairs_directionality.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
    
        p = compute_P(tp, fp)
        r = compute_R(tp, fn)
        a = compute_A(tp, tn, fp, fn)
        f1 = compute_F1(p, r)
        
        row = [thresh, tp, tn, fp, fn, p, r, a, f1]
        rows.append(row)
        
    return rows


def compute_crowd_performance_pair_only(crowd_results, output_directory, crowd_score):
    rows = []
    header = ["Thresh", "TP", "TN", "FP", "FN", "Precision", "Recall", "Accuracy", "F1-score"]
    rows.append(header)
    
    for i in range(5, 101, 5):
        row = []
        thresh = i / 100.0

        if not os.path.exists(output_directory + str(thresh) + "-pairs-only"):
            os.makedirs(output_directory + str(thresh) + "-pairs-only")
                    
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        
        for j in range(len(crowd_results.index)):
            if crowd_results["event-event_pair_only"].iloc[j] != "no_relation": # and crowd_results["no_of_annotations"].iloc[j] >= 7:
                if crowd_results[crowd_score].iloc[j] >= thresh:
                    if crowd_results["Experts_Pair"].iloc[j] == 1:
                        tp = tp + 1
                        
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair_only"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-only/" + "tp_pairs_only.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
            
                    else:
                        fp = fp + 1
                            
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair_only"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-only/" + "fp_pairs_only.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
                else:
                    if crowd_results["Experts_Pair"].iloc[j] == 1:
                        fn = fn + 1
                            
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair_only"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-only/" + "fn_pairs_only.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
                            
                    else:
                        tn = tn + 1
                            
                        entry = crowd_results["input.sentence1_id"].iloc[j] + "\t" + crowd_results["event-event_pair_only"].iloc[j] + "\t" + str(crowd_results[crowd_score].iloc[j])
                            
                        output = open(output_directory + str(thresh) + "-pairs-only/" + "tn_pairs_only.txt", 'a')
                        output.writelines(entry + "\n")
                        output.close()
    
        p = compute_P(tp, fp)
        r = compute_R(tp, fn)
        a = compute_A(tp, tn, fp, fn)
        f1 = compute_F1(p, r)
        
        row = [thresh, tp, tn, fp, fn, p, r, a, f1]
        rows.append(row)
        
    return rows

def compute_majority_vote(crowd_results, crowd_score):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
        
    for j in range(len(crowd_results.index)):
        if crowd_results["event-event_pair"].iloc[j] != "no_relation": # and crowd_results["no_of_annotations"].iloc[j] >= 7:
            if crowd_results[crowd_score].iloc[j] >= 8:
                if crowd_results["Experts"].iloc[j] == 1:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if crowd_results["Experts"].iloc[j] == 1:
                    fn = fn + 1
                else:
                    tn = tn + 1
    
    p = compute_P(tp, fp)
    r = compute_R(tp, fn)
    a = compute_A(tp, tn, fp, fn)
    f1 = compute_F1(p, r)
        
    return tp, tn, fp, fn, p, r, a, f1



    
