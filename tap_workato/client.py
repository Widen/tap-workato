"""REST client handling, including WorkatoStream base class."""

from pathlib import Path
from typing import Any, Dict, Iterable, Optional

import requests
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class WorkatoStream(RESTStream):
    """Workato stream class."""

    url_base = "https://www.workato.com"

    records_jsonpath = "$[*]"
    next_page_token_jsonpath = "$.next_page"  # Or override `get_next_page_token`.

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        return {
            "x-user-token": self.config.get("user_token"),
            "x-user-email": self.config.get("user_email"),
        }

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            next_page_token = response.headers.get("X-Next-Page", None)

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {"per_page": 100}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["order"] = "default"
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        """As needed, append or transform raw data to match expected structure."""
        return row
