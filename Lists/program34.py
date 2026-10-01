# find languages which start with letter p
languages = ('java','python','php','c','c#','javascript')
print("languages = ('java','python','php','c','c#','javascript'): ",
      [languages for languages in languages if languages.startswith('p')])