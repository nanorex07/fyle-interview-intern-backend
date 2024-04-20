from core.models.assignments import AssignmentStateEnum, GradeEnum

def test_access_principal(client, h_teacher_1):
    """
    failure case: a principal must access principal end point
    """
    response = client.get(
        "/principal/teachers",
        headers=h_teacher_1
    )
    assert response.status_code == 403
    assert response.json["error"] == "FyleError"

def test_get_teachers_as_principal(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    assert len(data) == 2
    assert data[0].get("username", "") == "teacher1"
    assert data[0].get("email", "") == "teacher1@fylebe.com"
    assert data[0].get("id", 0) == 3
    assert data[1].get("username", "") == "teacher2"
    assert data[1].get("email", "") == "teacher2@fylebe.com"
    assert data[1].get("id",0) == 4
    

def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B
