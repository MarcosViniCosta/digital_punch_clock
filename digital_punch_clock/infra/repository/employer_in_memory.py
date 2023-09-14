from domain.entity.employer import EmployerEntity
from domain.repository.employer import EmployerRepository

_TABLE = {}


class EmployerInMemoryRepository(EmployerRepository):
    async def insert(self, employer: EmployerEntity):
        _TABLE[employer.registration] = employer
