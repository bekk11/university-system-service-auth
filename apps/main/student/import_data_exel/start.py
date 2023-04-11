import openpyxl

from apps.main.student.import_data_exel.clear_datas import clear_datas
from apps.main.student.import_data_exel.create_faculty import create_faculty
from apps.main.student.import_data_exel.create_group import create_group
from apps.main.student.import_data_exel.create_students import create_student
from apps.main.student.import_data_exel.detect_columns import detect_columns
from config.settings import BASE_DIR


def start_importing(data):
    # opening and activating workbook
    sheet_obj = openpyxl.load_workbook(
        str(f"{BASE_DIR}/media/student_exel_data/{str(data['exel_file']).split('student_exel_data/')[1]}")).active

    # step 1 is to detect all columns
    columns = detect_columns(sheet_obj)

    # step 2 is clearing all datas
    cleared_data = clear_datas(sheet_obj, columns)

    # print(cleared_data)

    # step 3 create all faculties
    create_faculty(cleared_data, int(data['dean_id']))

    # step 4 create all groups
    create_group(cleared_data)

    # final step create students
    create_student(cleared_data)
