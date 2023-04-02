class MyEexception(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None
    def __str__(self):
        return f"Error: {self.message}"

class ExceptionGender(MyEexception):
    description = "Gender should be enterd 'f' or 'm'!"

class ExceptionDate(MyEexception):
    description = "Date or telephone entered incorrectly!"

class ExceptionWrongNumberData(MyEexception):
    description = "Incorrect amount of data entered!"

class ExceptionNotAllData(MyEexception):
    description = "The following data entered incorrectly!"