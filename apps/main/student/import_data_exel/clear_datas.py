import requests
import datetime


def clear_datas(sheet_obj, columns):
    cleaned_datas = []
    for i in range(2, sheet_obj.max_row + 1):
        cleaned_datas.append({
            # ============================================================================================
            "fio": str(
                sheet_obj.cell(row=i, column=columns['fio']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['fio']).value else None,

            # ============================================================================================

            "order_date": datetime.date(
                int(f"20{str(sheet_obj.cell(row=i, column=columns['order_date']).value)[6:9]}"),
                int(str(sheet_obj.cell(row=i, column=2).value)[3:5]),
                int(str(sheet_obj.cell(row=i, column=2).value)[0:2])
            )
            if sheet_obj.cell(row=i, column=columns['order_date']).value else None,

            # ============================================================================================

            "level": int(
                sheet_obj.cell(row=i, column=columns['level']).value
            )
            if sheet_obj.cell(row=i, column=columns['level']).value else None,

            # ============================================================================================

            "faculty": str(
                sheet_obj.cell(row=i, column=columns['faculty']).value
            ).upper().strip().split(") ")[1]
            if sheet_obj.cell(row=i, column=columns['faculty']).value else None,

            # ============================================================================================

            "group": str(
                sheet_obj.cell(row=i, column=columns['group']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['group']).value else None,

            # ============================================================================================

            "lang": str(
                sheet_obj.cell(row=i, column=columns['lang']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['lang']).value else None,

            # ============================================================================================

            "sex": str(
                sheet_obj.cell(row=i, column=columns['sex']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['sex']).value else None,

            # ============================================================================================

            "id_card": str(
                sheet_obj.cell(row=i, column=columns['id_card']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['id_card']).value else None,

            # ============================================================================================

            "form": str(
                sheet_obj.cell(row=i, column=columns['form']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['form']).value else None,

            # ============================================================================================

            "passport": str(
                sheet_obj.cell(row=i, column=columns['passport']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['passport']).value else None,

            # ============================================================================================

            "date_birth": sheet_obj.cell(row=i, column=columns['date_birth']).value.date()
            if sheet_obj.cell(row=i, column=columns['date_birth']).value else None,

            # ============================================================================================

            "region_birth": str(
                sheet_obj.cell(row=i, column=columns['region_birth']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['region_birth']).value else None,

            # ============================================================================================

            "type_school": str(
                sheet_obj.cell(row=i, column=columns['type_school']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['type_school']).value else None,

            # ============================================================================================

            "nation": str(
                sheet_obj.cell(row=i, column=columns['nation']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['nation']).value else None,

            # ============================================================================================

            "description": str(
                sheet_obj.cell(row=i, column=columns['description']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['description']).value else None,

            # ============================================================================================

            "dean": str(
                sheet_obj.cell(row=i, column=columns['dean']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['dean']).value else None,

            # ============================================================================================

            "course_from_course": str(
                sheet_obj.cell(row=i, column=columns['course_from_course']).value
            ).upper().strip()
            if sheet_obj.cell(row=i, column=columns['course_from_course']).value else None
        })

    return cleaned_datas
