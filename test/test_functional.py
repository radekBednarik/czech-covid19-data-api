import pytest
from covid19_api.src import api
from hamcrest import assert_that, empty, is_, is_not


class TestApiCalls:
    def test_get_number_of_tests_done(self) -> None:
        (status, data) = api.get_number_of_tests_done()

        assert_that(status, is_(True))
        assert_that(data, is_(dict))
        assert_that(data, is_not(empty()))  # type: ignore

    def test_get_number_of_infected_done(self) -> None:
        (status, data) = api.get_number_of_infected()

        assert_that(status, is_(True))
        assert_that(data, is_(dict))
        assert_that(data, is_not(empty()))  # type: ignore
