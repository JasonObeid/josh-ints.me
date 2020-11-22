import csv
import datetime
import json
import operator
import random
import sys
import time
from collections import Counter
from math import floor
from statistics import mean, mode

import requests
from flask import Flask, jsonify, request, send_from_directory
from flask_caching import Cache
from flask_cors import CORS

from utils.helperFunctions import *



buildList, stats = getMobalytics()