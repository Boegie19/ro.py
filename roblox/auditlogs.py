from __future__ import annotations
from datetime import datetime
from enum import Enum
from dateutil.parser import parse

from roblox.members import Member
from roblox.partials.partialbadge import TypePartialBadge
from roblox.partials.partialrole import PartialRole
from roblox.partials.partialuser import PartialUser
from roblox.utilities.shared import ClientSharedObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from roblox.groups import BaseGroup


class Actions(Enum):
    delete_post = "DeletePost"
    remove_member = "RemoveMember"
    accept_join_request = "AcceptJoinRequest"
    decline_join_request = "DeclineJoinRequest"
    post_shout = "PostStatus"
    change_rank = "ChangeRank"
    buy_ad = "BuyAd"
    send_ally_request = "SendAllyRequest"
    create_enemy = "CreateEnemy"
    accept_ally_request = "AcceptAllyRequest"
    decline_ally_request = "DeclineAllyRequest"
    delete_ally = "DeleteAlly"
    delete_enemy = "DeleteEnemy"
    add_group_place = "AddGroupPlace"
    remove_group_place = "RemoveGroupPlace"
    create_items = "CreateItems"
    configure_items = "ConfigureItems"
    spend_group_funds = "SpendGroupFunds"
    change_owner = "ChangeOwner"
    delete = "Delete"
    adjust_currency_amounts = "AdjustCurrencyAmounts"
    abandon = "Abandon"
    claim = "Claim"
    rename = "Rename"
    change_description = "ChangeDescription"
    invite_to_clan = "InviteToClan"
    cancel_clan_invite = "CancelClanInvite"
    kick_from_clan = "KickFromClan"
    buy_clan = "BuyClan"
    create_group_asset = "CreateGroupAsset"
    update_group_asset = "UpdateGroupAsset"
    configure_group_asset = "ConfigureGroupAsset"
    revert_group_asset = "RevertGroupAsset"
    create_group_developer_product = "CreateGroupDeveloperProduct"
    configure_group_game = "ConfigureGroupGame"
    lock = "Lock"
    unlock = "Unlock"
    create_game_pass = "CreateGamePass"
    create_badge = "CreateBadge"
    configure_badge = "ConfigureBadge"
    save_place = "SavePlace"
    publish_place = "PublishPlace"
    update_roleset_rank = "UpdateRolesetRank"
    update_roleset_data = "UpdateRolesetData"


class AuditLog:
    """
    Attributes:
        actor: Member who did it.
        action_type: Type of the action
        created: Datetime of creation of the audit_log
        group: the group that this audit_log comes form
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        self.shared: ClientSharedObject = shared
        self.group: BaseGroup = group
        self.actor: Member = Member(shared=self.shared, data=data["actor"], group=self.group)
        self.action_type: str = data["actionType"]
        self.created: datetime = parse(data["created"])

    def __repr__(self):
        return f"<{self.__class__.__name__} actor={self.actor} action_type={self.action_type!r}"


class DeletePost(AuditLog):
    """
    Attributes:
        description: The post description.
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.target: PartialUser = PartialUser(shared=shared, data=data["description"])
        self.description: str = data["description"]["PostDesc"]


class RemoveMember(AuditLog):
    """
    Attributes:
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.target: PartialUser = PartialUser(shared=shared, data=data["description"])


class AcceptJoinRequest(AuditLog):
    """
    Attributes:
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.target: PartialUser = PartialUser(shared=shared, data=data["description"])


class DeclineJoinRequest(AuditLog):
    """
    Attributes:
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.target: PartialUser = PartialUser(shared=shared, data=data["description"])


class PostStatus(AuditLog):
    """
    Attributes:
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.text: str = data["description"]["Text"]


class ChangeRank(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialUser = PartialUser(shared=shared, data=data["description"])
        self.new_role: PartialRole = PartialRole(shared=shared,
                                                 data={"id": data["description"]["NewRoleSetId"],
                                                       "name": data["description"]["NewRoleSetName"]},
                                                 group=group)
        self.old_role: PartialRole = PartialRole(shared=shared,
                                                 data={"id": data["description"]["OldRoleSetId"],
                                                       "name": data["description"]["OldRoleSetName"]},
                                                 group=group)


class BuyAd(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.name: str = data["description"]["AdName"]
        self.bid: int = data["description"]["Bid"]
        self.currency_type_id: int = data["description"]["CurrencyTypeId"]
        # CurrencyTypeName is always an emty string


class SendAllyRequest(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgroup import PartialGroup
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialGroup = PartialGroup(shared=shared, data=data["description"])


class CreateEnemy(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgroup import PartialGroup
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialGroup = PartialGroup(shared=shared, data=data["description"])


class AcceptAllyRequest(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgroup import PartialGroup
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialGroup = PartialGroup(shared=shared, data=data["description"])


class DeclineAllyRequest(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgroup import PartialGroup
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialGroup = PartialGroup(shared=shared, data=data["description"])


class DeleteAlly(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgroup import PartialGroup
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialGroup = PartialGroup(shared=shared, data=data["description"])


class DeleteEnemy(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgroup import PartialGroup
        super().__init__(shared=shared, data=data, group=group)
        self.target: PartialGroup = PartialGroup(shared=shared, data=data["description"])


class AddGroupPlace(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class RemoveGroupPlace(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class CreateItems(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialasset import PartialAsset
        super().__init__(shared=shared, data=data, group=group)
        self.asset: PartialAsset = PartialAsset(shared=shared, data=data["description"])


class ConfigureItems(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialasset import PartialAsset

        super().__init__(shared=shared, data=data, group=group)

        self.asset: PartialAsset = PartialAsset(shared=shared, data=data["description"])


class SpendGroupFunds(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.amount: int = data["description"]["Amount"]
        self.currency_type_id: int = data["description"]["CurrencyTypeId"]
        self.item_description: int = data["description"]["CurrencyTypeId"]


class ChangeOwner(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.is_roblox: int = data["description"]["IsRoblox"]
        self.old_owner: PartialUser = PartialUser(shared=shared, data={"Id": data["description"]["OldOwnerId"],
                                                                       "Name": data["description"]["OldOwnerName"]})
        self.new_owner: PartialUser = PartialUser(shared=shared, data={"Id": data["description"]["NewOwnerId"],
                                                                       "Name": data["description"]["NewOwnerName"]})


class Delete(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class AdjustCurrencyAmounts(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class Abandon(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class Claim(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class Rename(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class ChangeDescription(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)
        self.new_description = data["description"]["NewDescription"]


class CancelClanInvite(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.target: PartialUser = PartialUser(shared=shared, data=data["description"])


class KickFromClan(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class BuyClan(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.text: str = data["description"]["Text"]

class CreateGroupAsset(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialasset import VersionPartialAsset
        super().__init__(shared=shared, data=data, group=group)
        self.asset: VersionPartialAsset = VersionPartialAsset(shared=self.shared, data=data["description"])


class UpdateGroupAsset(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialasset import VersionPartialAsset
        super().__init__(shared=shared, data=data, group=group)
        self.asset: VersionPartialAsset = VersionPartialAsset(shared=self.shared, data=data["description"])


class ConfigureGroupAsset(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialasset import ActionsPartialAsset
        super().__init__(shared=shared, data=data, group=group)
        self.asset: ActionsPartialAsset = ActionsPartialAsset(shared=self.shared, data=data["description"])


class RevertGroupAsset(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class CreateGroupDeveloperProduct(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialasset import PartialAsset
        super().__init__(shared=shared, data=data, group=group)

        self.asset: PartialAsset = PartialAsset(shared=shared, data=data["description"])


class ConfigureGroupGame(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialplace import PartialPlace
        super().__init__(shared=shared, data=data, group=group)

        self.asset: PartialPlace = PartialPlace(shared=shared, data=data["description"])


class Lock(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.reason: str = data["description"]["Reason"]


class Unlock(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)


class CreateGamePass(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialgamepass import PartialGamePass
        from roblox.partials.partialplace import PartialPlace

        super().__init__(shared=shared, data=data, group=group)

        self.gamepass: PartialGamePass = PartialGamePass(shared=self.shared, data=data["description"])
        self.place: PartialPlace = PartialPlace(shared=self.shared, data=data["description"])


class CreateBadge(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialbadge import PartialBadge

        super().__init__(shared=shared, data=data, group=group)

        self.badge: PartialBadge = PartialBadge(shared=self.shared, data=data["description"])


class ConfigureBadge(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        super().__init__(shared=shared, data=data, group=group)

        self.badge: TypePartialBadge = TypePartialBadge(shared=shared, data=data["description"])


class SavePlace(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """

        from roblox.partials.partialasset import PartialAsset

        super().__init__(shared=shared, data=data, group=group)

        self.asset: PartialAsset = PartialAsset(shared=shared, data=data["description"])


class PublishPlace(AuditLog):
    """
    Attributes:
        asset: The asset being published
    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """

        from roblox.partials.partialasset import PartialAsset

        super().__init__(shared=shared, data=data, group=group)

        self.asset: PartialAsset = PartialAsset(shared=shared, data=data["description"])


class UpdateRolesetRank(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """

        from roblox.partials.partialrole import UpdateRankPartialRole

        super().__init__(shared=shared, data=data, group=group)

        self.asset: UpdateRankPartialRole = UpdateRankPartialRole(shared=shared, data=data["description"], group=group)


class UpdateRolesetData(AuditLog):
    """
    Attributes:

    """

    def __init__(self, shared: ClientSharedObject, data: dict, group: BaseGroup):
        """
        Arguments:
            shared: The ClientSharedObject to be used when getting information on badges.
            data: The data from the endpoint.
            group: the group you have the audit logs from
        """
        from roblox.partials.partialrole import UpdateDataPartialRole

        super().__init__(shared=shared, data=data, group=group)

        self.asset: UpdateDataPartialRole = UpdateDataPartialRole(shared=shared, data=data["description"], group=group)
