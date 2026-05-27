"""Workato tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_workato.streams import (
    ApiClientsStream,
    ApiCollectionsStream,
    ConnectionsStream,
    CustomerAccountsStream,
    CustomerApiAccessProfilesStream,
    CustomerApiClientsStream,
    CustomerApiCollectionsStream,
    CustomerApiEndpointsStream,
    CustomerConnectionsStream,
    CustomerFoldersStream,
    CustomerMembersStream,
    CustomerRecipesStream,
    CustomerRolesStream,
    FoldersStream,
    JobsStream,
    OnPremAgentsStream,
    OnPremGroupsStream,
    RecipesStream,
    RolesStream,
)

STREAM_TYPES = [
    ApiClientsStream,
    ApiCollectionsStream,
    ConnectionsStream,
    CustomerAccountsStream,
    CustomerApiAccessProfilesStream,
    CustomerApiClientsStream,
    CustomerApiCollectionsStream,
    CustomerApiEndpointsStream,
    CustomerConnectionsStream,
    CustomerFoldersStream,
    CustomerMembersStream,
    CustomerRecipesStream,
    CustomerRolesStream,
    FoldersStream,
    JobsStream,
    OnPremAgentsStream,
    OnPremGroupsStream,
    RecipesStream,
    RolesStream,
]


class TapWorkato(Tap):
    """Workato tap class."""

    name = "tap-workato"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType,
            required=True,
            description="Bearer token for Workato API authentication",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
