import pytest
import test_steps

# pytest -v -m for_all run_tests.py


@pytest.mark.for_all
@pytest.mark.first
def test_name_Giovanni():
    test_steps.test_first()


@pytest.mark.for_all
@pytest.mark.second
def test_total_six_entries():
    test_steps.test_second()


@pytest.mark.for_all
@pytest.mark.third
def test_added_new_entry():
    test_steps.test_third()


@pytest.mark.for_all
@pytest.mark.fourth
def test_change_all_data():
    test_steps.test_fourth()


@pytest.mark.for_all
@pytest.mark.fifth
def test_delete_all_Mexico():
    test_steps.test_fifth()
