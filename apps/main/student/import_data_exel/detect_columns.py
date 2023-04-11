def detect_columns(sheet_obj):
    row = sheet_obj.max_row
    column = sheet_obj.max_column

    columns = {
        "fio": None,
        "order_date": None,
        "level": None,
        "faculty": None,
        "group": None,
        "lang": None,
        "sex": None,
        "id_card": None,
        "form": None,
        "passport": None,
        "date_birth": None,
        "region_birth": None,
        "type_school": None,
        "nation": None,
        "description": None,
        "dean": None,
        "course_from_course": None
    }

    for i in range(1, row + 1):
        if i == 1:
            for i in range(1, column):
                cell_value = str(sheet_obj.cell(row=1, column=i).value).upper()

                if cell_value == "FIO" or cell_value == "ФИО":
                    columns['fio'] = i
                elif cell_value == "ORDER" or cell_value == "ORDER DATE":
                    columns['order_date'] = i
                elif cell_value == "DEGREE" or cell_value == "LEVEL" or cell_value == "COURSE" or cell_value == "КУРС" or cell_value == "УРОВЕНЬ" or cell_value == "ГОД":
                    columns['level'] = i
                elif cell_value == "FACULTY" or cell_value == "DIRECTION" or cell_value == "ФАКУЛЬТЕТ" or cell_value == "ФАКУЛТЕТ" or cell_value == "НАПРАВЛЕНИЯ":
                    columns['faculty'] = i
                elif cell_value == "GROUP":
                    columns['group'] = i
                elif cell_value == "LANG":
                    columns['lang'] = i
                elif cell_value == "SEX":
                    columns['sex'] = i
                elif cell_value == "ID":
                    columns['id_card'] = i
                elif cell_value == "FORM":
                    columns['form'] = i
                elif cell_value == "PASSPORT":
                    columns['passport'] = i
                elif cell_value == "DATE OF BIRTH":
                    columns['date_birth'] = i
                elif cell_value == "REGION OF BIRTH":
                    columns['region_birth'] = i
                elif cell_value == "TYPE OF SCHOOL":
                    columns['type_school'] = i
                elif cell_value == "NATION":
                    columns['nation'] = i
                elif cell_value == "DESCRIPTION" or cell_value == "ИЗОХ":
                    columns['description'] = i
                elif cell_value == "DEAN":
                    columns['dean'] = i
                elif cell_value == "KURSDAN KURSGA":
                    columns['course_from_course'] = i

    return columns
