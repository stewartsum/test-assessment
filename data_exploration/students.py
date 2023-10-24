import pandas as pd


def get_data(file: str) -> pd.DataFrame:
    return pd.read_csv(file)


def get_students_by_female_with_score_greater_than_90(
    students: pd.DataFrame,
) -> pd.DataFrame:
    # Replace the next line with your implemention
    raise NotImplementedError()


def main():
    file = "students.csv"
    students = get_data(file)
    print(students.head())

    #    id        name  class  score  gender
    # 0   1    John Deo   Four     75  female
    # 1   2    Max Ruin  Three     85    male
    # 2   3      Arnold  Three     55    male
    # 3   4  Krish Star   Four     60  female
    # 4   5   John Mike   Four     60  female

    female_students_with_high_score = get_students_by_female_with_score_greater_than_90(
        students
    )

    print(female_students_with_high_score)


#     id       name class  score  gender
# 11  12      Recky   Six     94  female
# 32  33  Kenn Rein   Six     96  female


if __name__ == "__main__":
    main()
