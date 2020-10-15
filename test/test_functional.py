import pytest
from covid19_api.src import api
from hamcrest import assert_that, empty, is_, is_not


class TestApiCallsJson:
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

    def test_get_all_numbers(self) -> None:
        (status, data) = api.get_all_numbers()

        assert_that(status, is_(True))
        assert_that(data, is_(dict))
        assert_that(data, is_not(empty()))  # type: ignore

    def test_get_basic_overview(self) -> None:
        (status, data) = api.get_basic_overview()

        assert_that(status, is_(True))
        assert_that(data, is_(dict))
        assert_that(data, is_not(empty()))  # type: ignore


class TestApiCallsCsv:
    def test_get_number_of_tests_done(self) -> None:
        (status, data) = api.get_number_of_tests_done(resource="/testy.csv")

        assert_that(status, is_(True))
        assert_that(data, is_(str))
        assert_that(data, is_not(empty()))  # type: ignore

    def test_get_number_of_infected_done(self) -> None:
        (status, data) = api.get_number_of_infected(resource="/nakaza.csv")

        assert_that(status, is_(True))
        assert_that(data, is_(str))
        assert_that(data, is_not(empty()))  # type: ignore

    def test_get_all_numbers(self) -> None:
        (status, data) = api.get_all_numbers(
            resource="/nakazeni-vyleceni-umrti-testy.csv"
        )

        assert_that(status, is_(True))
        assert_that(data, is_(str))
        assert_that(data, is_not(empty()))  # type: ignore

    def test_get_basic_overview(self) -> None:
        (status, data) = api.get_basic_overview(resource="/zakladni-prehled.csv")

        assert_that(status, is_(True))
        assert_that(data, is_(str))
        assert_that(data, is_not(empty()))  # type: ignore
