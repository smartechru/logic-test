# Overview

The purpose of this task is to test your capabilities in developing algorithms to manipulate / convert the format of a dataset.

All you need to get started is python running on your machine!

# Speed & Accuracy

This test is about speed & accuracy, not code quality. 

The result must be 100% correct and accurate... however, we will be far more impressed with a 'hacky' fully working answer in 20 minutes than we will be with a thoroughly documented, unit-tested, passing all PEP8-checks, fancy library-using solution in 2 hours. 

Get your code working and back to us as soon as it is functional. The time is already ticking :)

# The Task

Oh no! We need to get an easy overview on some data of our internal project management tool, but the format of our database dump is a mess! Particularly, we would like to see what projects are under each of two user types, 'managers' and 'watchers', in the right priority order.

<br/>
<br/>

The steps you should take:

* Download the source file: https://drive.google.com/file/d/1pJIynVU63BK9WGUSKPWTsHDCSPJG5hCb/view?usp=sharing. In the source json file you will encounter a list of dictionaries, each with the name of a project, the list of managers in that project, the list of watchers in the project, and the priority interger of that project. **Very important here - the lower the interger, the higher the priority**
Example of one project's dictionary:
<br/>

```
{
        "name": "[CV] [Qt] OpenCV GUI",
        "managers": [
            "csaftoiu",
            "merlin"
        ],
        "watchers": [
            "merlin",
            "morris"
        ],
        "priority": 850
}
```
<br/>

* Generate 2 output files, watchers.json and managers.json. Each should contain a dictionary with the manager / watcher  in the key, and a list of projects in the value. The projects in the list should be ordered by priority - from most priority to least priority  (remember here that a lower number means a higher priority).

Here is the answer for one manager that should be in the managers.json output file, in the correct format and ordering. The watchers.json file should follow the same format:

<br/>

```
"csaftoiu": [
        "sportsparsers - pinnacle API",
        "[OCR] tesseract MRZ reading ",
        "unity render diff passport text artur",
        "[CV] [Qt] OpenCV GUI",
        "unity render different passport text",
        "[template] unity render passport text",
        "matchbook parser - mfilho"
    ],
``` 
<br/>

Please commit both json files, and send us the python file of the code you used to generate them.

Good Luck!