from typing import Any, Dict, Optional, Tuple, Union

import requests as r
from requests import Request, Response

# TYPE ALIASES:
# pylint: disable=unsubscriptable-object
response_data = Tuple[bool, Optional[Dict[str, Any]]]

# CONSTANTS:
main_url: str = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19"


def _get_resource(resource: str) -> response_data:
    """REST API resource getter.

    Args:
        resource (str): API resource string

    Returns:
        response_data (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    try:
        response: Response = r.get(f"{main_url}{resource}")

        if response.status_code in [200, 201]:
            return (True, response.json())

        return (False, None)

    except Exception as e:
        print(f"Exception in '_get_resource': {str(e)}")
        return (False, None)


def get_number_of_tests_done(resource="/testy.json") -> response_data:
    """Returns `dict` with data about daily COVID tests done.

    Args:
        resource (str, optional): API resource string. Defaults to "/testy.json".

    Returns:
        response_data (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    return _get_resource(resource)


def get_number_of_infected(resource="/nakaza.json") -> response_data:
    """Returns `dict` with data about daily COVID infected people.

    Args:
        resource (str, optional): API resource string. Defaults to "nakaza.json".

    Returns:
        response_data (Tuple[bool, Optional[Dict[str, Any]]]): status of the resource call, and data
    """
    return _get_resource(resource)


if __name__ == "__main__":
    (state, data) = get_number_of_infected()

    if state:
        print(data)
