from src.modules.create_criminal_record.app.create_criminal_record_viewmodel import CreateCriminalRecordViewmodel
from src.shared.infra.repositories.criminal_record_repository_mock import CriminalRecordRepositoryMock


class Test_CreateCriminalRecordViewmodel:

    def test_create_criminal_record_viewmodel(self):
        """
            The function that tests if the criminal record view model translation is the same as the expected 
        """
        repo = CriminalRecordRepositoryMock()
        criminal_record = repo.criminal_record_list[0]
        criminal_record_viewmodel = CreateCriminalRecordViewmodel(criminal_record
                                                                  ).to_dict()

        expected_criminal_record_json = {
            "criminal_record": {
                "criminal_record_id": "4d108071-6d0f-48cb-8675-5d38049c3ecc",
                "criminal_owner": {
                    "name": "Lonnie Machin",
                    "nickname": "Anarky",
                    "age": 16,
                    "blood_type": "UNDEFINED",
                    "criminal_description": "Anarky uses his abilities to bring down any corporation or authoritative entity that he feels hurts and oppresses people. While he can throw a punch as well as anyone, he relies primarily on his thorough understanding of modern technology to defeat his foes along with the very essence of anarchy itself—surprise.",
                    "gender": "MALE",
                    "height": 1.7,
                    "weight": 75.2,
                    "criminal_region": "NEW_GOTHAM"
                },
                "danger_score": 3,
                "is_arrested": False,
                "prison": None
            },
            "message": "the criminal record was created"
        }

        assert criminal_record_viewmodel == expected_criminal_record_json
