"""
自訂 Exception 模組

"""


class ExcelError(Exception):
    """先繼承Excel，供子類別繼承。"""
    pass


class ExcelFileNotFoundError(ExcelError):
    """找不到指定的 Excel 檔案時"""

    def __init__(self, file_path):
        self.file_path = file_path
        super().__init__(f"找不到 Excel 檔案: {file_path}")


class ExcelSheetNotFoundError(ExcelError):
    """找不到指定的工作表"""

    def __init__(self, file_path, sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        super().__init__(f"在 {file_path} 中找不到工作表: {sheet_name}")


class ExcelDataError(ExcelError):
    """Excel 資料異常時，如空值、型別錯誤、格式不符等"""

    def __init__(self, file_path, sheet_name, row, column, message="資料異常"):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.row = row
        self.column = column
        super().__init__(
            f"{file_path} [{sheet_name}] 第 {row} 列第 {column} 欄: {message}")
