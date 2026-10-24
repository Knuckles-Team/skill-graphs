# A string whose value cannot be imported will raise an error
try:
    ImportThings(obj='foo.bar')
except ValidationError as e:
    print(e)
    '''
    1 validation error for ImportThings
    obj
      Invalid python path: No module named 'foo.bar' [type=import_error, input_value='foo.bar', input_type=str]
    '''
