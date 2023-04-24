from src.modules.create_criminal_record.create_criminal_record_viewmodel import CreateCriminalRecordViewlModel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordViewmodel:

    def test_create_criminal_record_viewmodel(self):
        """
            The function that tests if the criminal record view model translation is the same as the expected 
        """
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.criminal_record_list[0]
        criminal_record_viewmodel = CreateCriminalRecordViewlModel(criminal_record
                                                                  ).to_dict()

        expected_criminal_record_json = {
            "criminal_record": {
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "crime_list": [
                    {
                        "crime_id": "d9af6081-74f9-478d-9599-d2b21a06b386",
                        "crime_type": "Arson",
                        "responsible_criminal": {
                            "name": "Lonnie Machin",
                            "nickname": "Anarky",
                            "age": 16,
                            "blood_type": "Undefined",
                            "criminal_description": "New Gotham",
                            "gender": "Male",
                            "height": 1.7,
                            "weight": 75.2
                        },
                        "date": 1648755588000,
                        "crime_description": "Crime committed violently against innocent people",
                        "crime_region": "Amusement Mile",
                        "seriousness": "High"
                    },
                    {
                        "crime_id": "9130a793-ad89-4171-adf2-c33575a4c066",
                        "crime_type": "Theft",
                        "responsible_criminal": {
                            "name": "Lonnie Machin",
                            "nickname": "Anarky",
                            "age": 16,
                            "blood_type": "Undefined",
                            "criminal_description": "New Gotham",
                            "gender": "Male",
                            "height": 1.7,
                            "weight": 75.2
                        },
                        "date": 1648755588000,
                        "crime_description": "Armed robbery against the elderly",
                        "crime_region": "New Gotham",
                        "seriousness": "Medium"
                    }
                ],
                "criminal_owner": {
                    "name": "Lonnie Machin",
                    "nickname": "Anarky",
                    "age": 16,
                    "blood_type": "Undefined",
                    "criminal_description": "New Gotham",
                    "gender": "Male",
                    "height": 1.7,
                    "weight": 75.2
                },
                "danger_score": 3,
                "is_arrested": False,
                "prison": None
            },
            "message": "the criminal record was created"
        }

        assert criminal_record_viewmodel == expected_criminal_record_json