# Autograde Example

## Disclaimer

This repository is a demo for our coding assignments. Please note that **nothing in this repository is related to database!**

## Question Sample: Average of list

Write a function called `avg_list` in [exercise.py](https://github.com/SE-starshippilot/autograde_example/blob/master/src/exercise.py) that returns the average of a list of number in python. The return should be rounded to int.

```python
numbers = []
numbers.append(3)
numbers.append(2)
numbers.append(6)
numbers.append(-1)
print(avg_list(numbers))  // should be 3

numbers.append(5)
numbers.append(1)
print(avg_list(numbers))  //should be 3
```

## How you write your coding assignments for this course

1. When the assignment is released, we will provide you with a link. Click link and accept the homework. This will create a repo in you GitHub.
2. Clone this repository to your computer. (`git clone <repo url>`)
3. Work on your codes.
4. When you think you're ready, push your changes to github (`git push origin master`)
5. GitHub Action will run the testcase, and you can check if you passed.

## Some warm reminders

- As mentioned in tutorial, make *constant*, *semantic* commits locally.
- We **will** replace the testcase for grading, so please don't do testcase-oriented programmng. 😊
- You can push to your repository to perform test run as many times as you like.
