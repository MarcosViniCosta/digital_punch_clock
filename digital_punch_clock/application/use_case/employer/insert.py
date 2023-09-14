from domain.entity.employer import EmployerEntity
from domain.repository.employer import EmployerRepository


class InsertEmployerUseCase:
    def __init__(self, employer_repository: EmployerRepository):
        self._employer_repository = employer_repository

    async def execute(self, employer: EmployerEntity):
        await self._employer_repository.insert(employer)
