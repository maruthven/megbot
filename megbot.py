#!/usr/bin/python
''' 
Author: Megan Ruthven
Date: August 18, 2015
'''

import sys 
import json
import re
import string
from collections import Counter
from nltk.corpus import stopwords
from stemming.porter2 import stem
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import requests 
from splinter import Browser
from urllib2 import URLError

_base_url = "https://mbasic.facebook.com"
_base_msg_url = _base_url + "/messages/read/?tid=id."
_msg_url_mid = "&start=";
_intro_message = "Hey y'all! I'm megbot. Here to help with some chat automation. My use cases are endless. If you're interested in what I'm here for, ask who invited me into this chat what I can do!";

class MegBot:
        """MegBot is an interface to Facebook Messages. You can use it by logging into your account, and giving it a group message you are a member of. You can navigate to different pages of the message, read the page, and write to the group chat. Please make sure the other members are aware MegBot is joining y'all in your conversation."""
        def __init__(self, un, pw):
                self.username = un;
                self.password = pw;
                self.currentPage = 0;
                self.messageID = 0;
                self.browser = Browser("phantomjs");
                pass;

        def login(self): 
        	self.browser.visit(_base_url)
                self.browser.fill('email', self.username);
                self.browser.fill('pass', self.password);
                self.browser.find_by_css('input[type="submit"]').first.click();

	        print "Logged in!"

                if self.messageID:
                        self.moveToMessage();

        def move_to_message(self, mID):
                self.currentPage = 0;
                self.messageID = mID.strip();
                self.browser.visit(_base_msg_url + self.messageID);
                time.sleep(3);
                self.send_message(_intro_message);

        def refresh_messages(self):
                if self.messageID == 0:
                        return;
                
                self.currentPage = 0;
                self.browser.visit(_base_msg_url + self.messageID);
                time.sleep(3);

        def next_page(self):
                if self.messageID == 0:
                        return False;
                
                self.currentPage += 1;
                print self.currentPage;
                self.browser.visit(_base_msg_url + self.messageID + _msg_url_mid + str(5 * self.currentPage));
                time.sleep(3);

        def send_message(self, inWords):
                self.browser.find_by_id('composerInput').fill(inWords);
                self.browser.find_by_css('input[name="send"]').first.click();
                time.sleep(3);

        def read_messages(self):
                messages = [];
                mHTML = self.browser.find_by_id("messageGroup").find_by_css("div");
                #unnecessary right now
                link = mHTML.pop(0).find_by_css("a")["href"];
                lines = mHTML.find_by_css("span");
                for line in lines:
                        l = filter(lambda x: x in string.printable, line.text.strip());
                        if l and l != "." and not ("Sent from" in l) and not ("Seen by" in l):
                                messages.insert(0, l);
                else:
                        print "skipped " + l;

                return messages;

        
