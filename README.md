# Fyle Backend Challenge

## Challenge outline

This challenge involves writing a backend service for a classroom. The challenge is described in detail [here](./Application.md)


## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Start Server

```
bash run.sh
```
### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```

## Features Added

## 1. APIs

### GET /teacher/assignments

List all assignments submitted to this teacher
```
headers:
X-Principal: {"user_id":3, "teacher_id":1}

response:
{
    "data": [
        {
            "content": "ESSAY T1",
            "created_at": "2021-09-17T03:14:01.580126",
            "grade": null,
            "id": 1,
            "state": "SUBMITTED",
            "student_id": 1,
            "teacher_id": 1,
            "updated_at": "2021-09-17T03:14:01.584644"
        }
    ]
}
```

### POST /teacher/assignments/grade

Grade an assignment
```
headers:
X-Principal: {"user_id":3, "teacher_id":1}

payload:
{
    "id":  1,
    "grade": "A"
}

response:
{
    "data": {
        "content": "ESSAY T1",
        "created_at": "2021-09-17T03:14:01.580126",
        "grade": "A",
        "id": 1,
        "state": "GRADED",
        "student_id": 1,
        "teacher_id": 1,
        "updated_at": "2021-09-17T03:20:42.896947"
    }
}
```

## 2. Test for grading API

![image](https://user-images.githubusercontent.com/81697577/210067551-a8155b5f-2f77-454f-872e-fb8273fb1b98.png)

## 3. 12/12 Test cases passed

![image](https://user-images.githubusercontent.com/81697577/210067593-c71cc57b-a2f1-4bed-92ce-bcf8f1cf8ed1.png)

## 4. Test coverage of 95% achieved

![image](https://user-images.githubusercontent.com/81697577/210067643-6977a9b3-87c8-4669-a016-bf0d3541896e.png)


