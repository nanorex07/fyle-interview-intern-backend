import pytest
from core.libs.assertions import assert_auth, assert_true, assert_valid, assert_found
from core.libs.exceptions import FyleError


def test_assert_auth():
    with pytest.raises(FyleError) as e:
        assert_auth(False)
    assert e.value.status_code == 401
    assert e.value.message == 'UNAUTHORIZED'


def test_assert_true():
    with pytest.raises(FyleError) as e:
        assert_true(False)
    assert e.value.status_code == 403
    assert e.value.message == 'FORBIDDEN'


def test_assert_valid():
    with pytest.raises(FyleError) as e:
        assert_valid(False)
    assert e.value.status_code == 400
    assert e.value.message == 'BAD_REQUEST'


def test_assert_found():
    with pytest.raises(FyleError) as e:
        assert_found(None)
    assert e.value.status_code == 404
    assert e.value.message == 'NOT_FOUND'