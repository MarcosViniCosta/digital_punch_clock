from abc import ABCMeta, abstractmethod

from domain.entity.employer import EmployerEntity


class EmployerRepository(metaclass=ABCMeta):

    @abstractmethod
    async def insert(self, employer: EmployerEntity):
        ...
