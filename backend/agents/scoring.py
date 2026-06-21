def calculate_readiness_score(
    python_skill,
    git_skill,
    sql_skill,
    problem_solving
):

    programming = python_skill * 2.5
    git = git_skill * 1.5
    database = sql_skill * 1.0
    problem = problem_solving * 1.5

    total_score = (
        programming +
        git +
        database +
        problem
    )

    return round(total_score)