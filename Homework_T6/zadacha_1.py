def koding():
    string_cod = b'r\xc3\xa9sum\xc3\xa9'
    string = string_cod.decode("utf-8")
    string_cod_2 = string.encode("Latin1")
    string_2 = string_cod_2.decode("latin1")
    print(string_2)
    print(string)


koding()
