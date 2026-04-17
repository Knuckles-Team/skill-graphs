# You can set default field value either as Python object:
class ImportThingsDefaultPyObj(BaseModel):
    obj: ImportString = math.cos
