from nce_coop.rules import LABEL, is_co_op_eligible, label


def test_cooperative_education_engineering_only_is_eligible():
    assert is_co_op_eligible("Cooperative Education", "Full-Time", "Structural Co-op", True)


def test_cooperative_education_non_engineering_is_not_eligible():
    assert not is_co_op_eligible("Cooperative Education", "Full-Time", "Marketing Co-op", False)


def test_full_time_internship_with_co_op_in_title_engineering_only_is_eligible():
    assert is_co_op_eligible("Internship", "Full-Time", "Mechanical Engineering Co-op Intern", True)


def test_full_time_internship_without_co_op_in_title_is_not_eligible():
    assert not is_co_op_eligible("Internship", "Full-Time", "Mechanical Engineering Intern", True)


def test_part_time_internship_with_co_op_in_title_is_not_eligible():
    assert not is_co_op_eligible("Internship", "Part-Time", "Engineering Co-op Assistant", True)


def test_internship_not_full_time_is_not_eligible_even_with_co_op_title():
    assert not is_co_op_eligible("Internship", "", "Co-op Intern", True)


def test_case_and_whitespace_insensitive():
    assert is_co_op_eligible("  cooperative education  ", " full-time ", "Co-Op Intern", True)


def test_label_returns_none_when_not_eligible():
    assert label("Internship", "Full-Time", "Software Intern", True) is None


def test_label_returns_the_constant_string_when_eligible():
    assert label("Cooperative Education", "Full-Time", "Civil Co-op", True) == LABEL
