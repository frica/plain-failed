# Works with Python 2.7.5 and the standard lib
# Usage:
# python plain-failed.py http://my_server/job/my_project/run_nbr/testReport/api/json

import json
import urllib2
import argparse
from os import sys

class JenkinsTestResultsConverter:

    def convert(self, url):

        try:
            response = urllib2.urlopen(url)
        except urllib2.HTTPError, e:
            print "URL Error: " + str(e.code) 
            print "      (url [" + url + "] probably wrong)"
            sys.exit(2)

        try:
            json_object = json.load(response)
        except:
            print "Failed to parse json"
            sys.exit(3)

        failedtestlist = []

        print "\n******************************\n"
        print "FAILING TESTS"
        print "\n******************************\n"
        for item in json_object["suites"]:
            for case in item["cases"]:
                if case["status"] in "REGRESSION" or "FAILED":
                    for action in case["testActions"]:
                        if action:
                            test = { 'name' : item["name"], 
                                    'test name' : case["name"],
                                    'status' : case["status"], 
                                    'errordetails' : case["errorDetails"],
                                    'errorStackTrace' : case["errorStackTrace"],
                                    'stdout' : case["stdout"],
                                    'claim' : action["reason"] }
                            print test["name"]
                            print test["test name"]
                            print test["status"]
                            print "------------------------------"  
                            print test["errordetails"]
                            print test["errorStackTrace"]
                            if test["stdout"] is not None:
                                print test["stdout"]
                            if test["claim"] is not None:
                                print test["claim"] 
                            print "\n******************************\n"  
                            failedtestlist.append(test)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Get a plain list of failed tests out of the Jenkins test results')
    parser.add_argument('input', help='Input file path')
    args = parser.parse_args()
    url = args.input
    print("URL to look at: %s" % url)

    if "json" not in url or "testReport" not in url:
        print("\nInput error: Please provide a json URL of a Jenkins test report.\nExample: http://my_server/job/my_project/run_nbr/testReport/api/json\n")
        sys.exit(1)
   
    converter = JenkinsTestResultsConverter()
    plainresults = converter.convert(url)
