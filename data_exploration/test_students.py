import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

from students import get_data, get_students_by_female_with_score_greater_than_90


class TestStudents(unittest.TestCase):
    def setUp(self) -> None:
        file = "students.csv"
        self.students = get_data(file)

    def test_get_students_by_female_with_score_greater_than_90(self):
        students = get_students_by_female_with_score_greater_than_90(self.students)
        assert_frame_equal(
            students,
            pd.DataFrame(
                {
                    "id": [12, 33],
                    "name": ["Recky", "Kenn Rein"],
                    "class": ["Six", "Six"],
                    "score": [94, 96],
                    "gender": ["female", "female"],
                },
                index=([11, 32]),
            ),
        )


if __name__ == "__main__":
    unittest.main()
