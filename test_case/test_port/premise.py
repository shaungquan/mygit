import pytest
import os
from config import YamlParse

def testdata():
    testname = YamlParse.YamlParse()
    testname.loadyaml("../../data/activity.yaml")
    data = testname.getJson()
    return data

