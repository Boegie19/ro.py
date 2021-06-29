from __future__ import annotations
from typing import Tuple, Union

from roblox.utilities.errors import NotFound
from roblox.utilities.subdomain import Subdomain
from roblox.user import PartialUser, User
from roblox.group import Group
from roblox.utilities.clientsharedobject import ClientSharedObject
from roblox.role import Role

# TODO Deal with if user is exiled or has left the group since you can't rank somebody who is no longer in the group
class Member:
    """
    Represents a user in a group.
    """

    def __init__(self: Member, cso: ClientSharedObject, user: Union[PartialUser, User], group: Group, role: Role):
        self.cso = cso
        """Client shared object."""
        self.user= user
        """The user that is in the group."""
        self.group = group
        """The group the user is in."""
        self.role = role
        """The role the user has in the group."""
        self.subdomain = Subdomain("groups")

    async def update_role(self: Member) -> Role:
        """
        Updates the role information of the user.

        Returns
        -------
        ro_py.roles.Role
        """

        url = self.subdomain.generate_endpoint("v2", "users", self.group.id, "groups", "roles")
        response = await self.cso.requests.get(url)

        data = response.json()
        for role in data['data']:
            if role['group']['id'] == self.group.id:
                self.role = Role(self.cso, self.group, role['role'])
                break
        
        return self.role

    async def change_rank(self: Member, num: int) -> Tuple[Role, Role]:
        """
        Changes the users rank specified by a number.
        If num is 1 the users role will go up by 1.
        If num is -1 the users role will go down by 1.

        Parameters
        ----------
        num : int
                How much to change the rank by.
        """

        old_role = await self.update_role()
        roles = await self.group.get_roles()

        role_counter = 0
        for group_role in roles:
            if group_role.rank == self.role.rank:
                break

            role_counter += 1
        
        role_counter += num

        if role_counter < 1 or role_counter >= len(roles):
            raise IndexError(f"Index is out of range")

        # if not roles:
        #    raise NotFound(f"User {self.user.id} is not in group {self.group.id}")

        await self.__setrank(roles[role_counter].id)
        self.role = roles[role_counter]

        return old_role, self.role

    async def promote(self: Member, rank: int = 1) -> Tuple[Role, Role]:
        """
        Promotes the user.

        Parameters
        ----------
        rank : int
                amount of ranks to promote

        Returns
        -------
        int
        """

        return await self.change_rank(abs(rank))

    async def demote(self: Member, rank: int = 1) -> Tuple[Role, Role]:
        """
        Demotes the user.

        Parameters
        ----------
        rank : int
                amount of ranks to demote

        Returns
        -------
        int
        """

        return await self.change_rank(-abs(rank))

    async def __set_rank(self: Member, rank: int) -> None:
        """
        Sets the users role to specified role using rank id.

        Parameters
        ----------
        rank : int
                Rank id

        Returns
        -------
        bool
        """

        url = self.subdomain.generate_endpoint("v1", "groups", self.group.id, "users", self.user.id)
        data = {
            "roleId": rank
        }

        await self.cso.requests.patch(url, json=data)

    async def set_rank(self, rank) -> None:
        await self.__set_rank(rank)
        await self.update_role()

    async def set_role(self, role_num):
        """
        Sets the users role to specified role using role number (1-255).

        Parameters
        ----------
        role_num : int
                Role number (1-255)

        Returns
        -------
        bool
        """

        roles = await self.group.get_roles()

        rank_role = None
        for role in roles:
            if role.rank == role_num:
                rank_role = role
                break
        
        if not rank_role:
            raise NotFound(f"Role {role_num} not found")
        
        return await self.__set_rank(rank_role.id)

    async def exile(self: Member) -> None:
        url = self.subdomain.generate_endpoint("v1", "groups", self.group.id, "users", self.user.id)

        await self.cso.requests.delete(url)