from typing import Any, Dict, Optional, Tuple, Union

import requests as r
from requests import Request, Response

# TYPE ALIASES:
# pylint: disable=unsubscriptable-object
data_ = Union[Dict[str, Any], None, str]
response_ = Tuple[bool, data_]

# CONSTANTS:
main_url: str = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19"


def _get_resource(resource: str) -> response_:
    """REST API resource getter.

    Args:
        resource (str): API resource string

    Returns:
        response_ (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    try:
        response: Response = r.get(f"{main_url}{resource}")

        if response.status_code in [200, 201]:

            if resource.endswith(".json"):
                return (True, response.json())

            if resource.endswith(".csv"):
                return (True, response.text)

            raise Exception("Resource can be either .json or .csv. Please check that.")

        return (False, None)

    except Exception as e:
        print(f"Exception in '_get_resource': {str(e)}")
        return (False, None)


def get_number_of_tests_done(resource="/testy.json") -> response_:
    """Returns `dict` with data about daily COVID tests done.

    Args:
        resource (str, optional): API resource string. Defaults to "/testy.json".

    Returns:
        response_ (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    return _get_resource(resource)


def get_number_of_infected(resource="/nakaza.json") -> response_:
    """Returns `dict` with data about daily COVID infected people.

    Args:
        resource (str, optional): API resource string. Defaults to "/nakaza.json".

    Returns:
        response_ (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    return _get_resource(resource)


def get_all_numbers(
    resource="/nakazeni-vyleceni-umrti-testy.json",
) -> response_:
    """Returns `dict` with daily data about infected, cured, died and tests done.

    Args:
        resource (str, optional): API resource string. Defaults to "/nakazeni-vyleceni-umrti-testy.json".

    Returns:
        response_ (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    return _get_resource(resource)


def get_basic_overview(resource="/zakladni-prehled.json") -> response_:
    """Returns `dict` with summary data about situation in Czech Republic.

    Args:
        resource (str, optional): API resource string. Defaults to "/nakazeni-vyleceni-umrti-testy.json".

    Returns:
        response_ (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    return _get_resource(resource)
