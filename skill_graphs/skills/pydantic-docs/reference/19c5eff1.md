# or as a string value (but only if used with `validate_default=True`)
class ImportThingsDefaultString(BaseModel):
    obj: ImportString = Field(default='math.cos', validate_default=True)

my_cos_default1 = ImportThingsDefaultPyObj()
my_cos_default2 = ImportThingsDefaultString()
assert my_cos_default1.obj == my_cos_default2.obj == math.cos
