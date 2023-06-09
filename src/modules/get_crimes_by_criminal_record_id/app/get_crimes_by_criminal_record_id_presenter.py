from .get_crimes_by_criminal_record_id_controller import GetCrimesByCriminalRecordIdController
from .get_crimes_by_criminal_record_id_usecase import GetCrimesByCriminalRecordIdUsecase
from src.shared.helpers.external_interfaces.http_fastapi_requests import FastAPIHttpRequest, FastAPIHttpResponse
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


def get_crimes_by_criminal_record_id_presenter(event, context):
    """Function Presenter of the route Get Crimes By Criminal Record Id"""

    repo = CriminalRecordRepositoryMock()
    usecase = GetCrimesByCriminalRecordIdUsecase(repo)
    controller = GetCrimesByCriminalRecordIdController(usecase)

    httpRequest = FastAPIHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = FastAPIHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.to_dict()
