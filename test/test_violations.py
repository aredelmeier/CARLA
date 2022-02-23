import pandas as pd

from carla.data.catalog import OnlineCatalog
from carla.evaluation import constraint_violation
from carla.models.catalog import MLModelCatalog


def test_constraint_violations():
    # Build data and mlmodel
    data_name = "adult"
    data = OnlineCatalog(data_name)

    model = MLModelCatalog(data, "ann")
    # get factuals
    columns = [
        "age",
        "workclass",
        "fnlwgt",
        "education-num",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "capital-gain",
        "capital-loss",
        "hours-per-week",
        "native-country",
        "income",
    ]
    test_factual = [
        [
            39,
            "Non-Private",
            77516,
            13,
            "Non-Married",
            "Managerial-Specialist",
            "Non-Husband",
            "White",
            "Male",
            2174,
            0,
            40,
            "US",
            0,
        ],
        [
            50,
            "Non-Private",
            83311,
            13,
            "Married",
            "Managerial-Specialist",
            "Husband",
            "White",
            "Male",
            0,
            0,
            13,
            "US",
            0,
        ],
        [
            38,
            "Private",
            215646,
            9,
            "Non-Married",
            "Other",
            "Non-Husband",
            "White",
            "Male",
            0,
            0,
            40,
            "US",
            0,
        ],
        [
            53,
            "Private",
            234721,
            7,
            "Married",
            "Other",
            "Husband",
            "Non-White",
            "Male",
            0,
            0,
            40,
            "US",
            0,
        ],
        [
            28,
            "Private",
            338409,
            13,
            "Married",
            "Managerial-Specialist",
            "Non-Husband",
            "Non-White",
            "Female",
            0,
            0,
            40,
            "Non-US",
            0,
        ],
    ]
    test_factual = pd.DataFrame(
        test_factual,
        columns=columns,
    )

    test_counterfactual = [
        [
            45,
            "Non-Private",
            77516,
            13,
            "Non-Married",
            "Managerial-Specialist",
            "Non-Husband",
            "White",
            "Female",
            2174,
            0,
            40,
            "US",
            0,
        ],
        [
            50,
            "Non-Private",
            83311,
            13,
            "Married",
            "Managerial-Specialist",
            "Husband",
            "White",
            "Male",
            0,
            0,
            13,
            "US",
            0,
        ],
        [
            18,
            "Private",
            215646,
            9,
            "Non-Married",
            "Other",
            "Non-Husband",
            "White",
            "Male",
            0,
            0,
            40,
            "US",
            0,
        ],
        [
            53,
            "Private",
            234721,
            7,
            "Married",
            "Other",
            "Husband",
            "Non-White",
            "Male",
            0,
            0,
            40,
            "US",
            0,
        ],
        [
            28,
            "Private",
            338409,
            13,
            "Married",
            "Managerial-Specialist",
            "Non-Husband",
            "Non-White",
            "Male",
            0,
            0,
            40,
            "Non-US",
            0,
        ],
    ]
    test_counterfactual = pd.DataFrame(
        test_counterfactual,
        columns=columns,
    )
    test_counterfactual = data.transform(test_counterfactual)
    test_factual = data.transform(test_factual)

    expected = [[2], [0], [1], [0], [1]]
    actual = constraint_violation(model, test_counterfactual, test_factual)

    assert expected == actual
