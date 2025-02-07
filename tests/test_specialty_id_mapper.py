import pytest


specialty_ids = [
    ["7-623", "8235", "8-235"],
    ["934*823", "143124", "abc1!", "@@934^8)23"],
    ["91*ps1", "13#0^82!3", "p5%91", "--9++1*1"],
]


specialties_by_id = [
    [
        [1381, "front-end web development"],
        [8235, "data engineering"],
        [3434, "API design"],
        [7623, "security"],
        [9153, "UX"]
    ],
    [
        [934823, "backend development"],
        [6897, "data engineering"],
        [143124, "data science"],
        [1, "product management"],
        [9153, "fullstack engineer"]
    ],
    [
        [911, "white hat hacker"],
        [130823, "machine learning engineer"],
        [12, "data engineering"],
        [1293, "product management"],
        [591, "UX researcher"]
    ],
]

no_matches_found = "No Matches Found"


@pytest.mark.parametrize("id_input, id_mapper_input, expected_result", [
    (specialty_ids[0], specialties_by_id[0], [
        specialties_by_id[0][3][1], specialties_by_id[0][1][1]
    ]),
    (specialty_ids[1], specialties_by_id[1], [
        specialties_by_id[1][0][1],
        specialties_by_id[1][2][1],
        specialties_by_id[1][3][1]
    ]),
    (specialty_ids[2], specialties_by_id[2], [
        specialties_by_id[2][0][1],
        specialties_by_id[2][1][1],
        specialties_by_id[2][4][1]
    ]),
])
def test_get_specialty_name_with_matching_ids(specialty_id_mapper_instance, id_input, id_mapper_input, expected_result):
    assert specialty_id_mapper_instance.get_specialty_names(id_input, id_mapper_input) == expected_result


@pytest.mark.parametrize("id_input, id_mapper_input, expected_result", [
    (specialty_ids[0], specialties_by_id[1], no_matches_found),
    (specialty_ids[1], specialties_by_id[2], no_matches_found),
    (specialty_ids[2], specialties_by_id[0], no_matches_found),
])
def test_get_specialty_name_with_no_matching_ids(specialty_id_mapper_instance, id_input, id_mapper_input, expected_result):
    assert specialty_id_mapper_instance.get_specialty_names(id_input, id_mapper_input) == expected_result
