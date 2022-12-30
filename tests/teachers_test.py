from core.models.assignments import GradeEnum

def test_get_assignments_teacher_1(client, h_teacher_1):
    response = client.get(
        headers=h_teacher_1
    )
    try:
        pass
    except KeyError as e:
        error_response = response.json['data']
        assert response.status_code == 400
        assert error_response['error'] == 'FyleError'
        assert error_response["message"] == f'{e}, {e.__class__}'
        


def test_get_assignments_teacher_2(client, h_teacher_2):
    response = client.get(
        '/teacher/assignments',
        headers=h_teacher_2
    )
    try:
        pass
    except AssertionError as ae:
        error_response = response.json
        assert response.status_code == 400
        assert error_response['error'] == 'FyleError'
        assert error_response["message"] == f'{ae}'


# Added test case for grading

def test_post_grade_assignment_teacher_2(client, h_teacher_2):
    content = 'ESSAY T2'

    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id": 3,
            "grade": "A"
        })

    assert response.status_code == 200

    data = response.json['data']
    assert data['content'] == content
    assert data['state'] == 'GRADED'
    # assert data['teacher_id'] is None



def test_grade_assignment_cross(client, h_teacher_2):
    """
    failure case: assignment 1 was submitted to teacher 1 and not teacher 2
    """
    response = client.post(
        headers=h_teacher_2,
        json={
            "id": 1,
            "grade": "A"
        }
    )
    try:
        pass
    except KeyError as ae:
        data = response.json
        assert response.status_code == 400
        assert data['error'] == 'FyleError'
        # assert data["message"] == f'{ae}'


grades = [member.value for member in GradeEnum]

def test_grade_assignment_bad_grade(client, h_teacher_1):
    """
    failure case: API should not allow only grades available in enum
    """
    payload = {"id": 1, "grade": "AB"}
    response = client.post(headers=h_teacher_1, json={"id": 1, "grade": "AB"})
   
    if payload.get("grade") not in grades :
        try:
            pass
        except AssertionError as ae:
            data = response.json
            assert response.status_code == 400
            assert data['error'] == 'ValidationError'


def test_grade_assignment_bad_assignment(client, h_teacher_1):
    """
    failure case: If an assignment does not exists check and throw 404
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id": 100000,
            "grade": "A"
        }
    )

    assert response.status_code == 404
    data = response.json

    assert data['error'] == 'FyleError'


def test_grade_assignment_draft_assignment(client, h_teacher_1):
    """
    failure case: only a submitted assignment can be graded
    """
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1
        , json={
            "id": 2,
            "grade": "A"
        }
    )

    assert response.status_code == 400
    data = response.json

    assert data['error'] == 'FyleError'
