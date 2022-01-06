
def setup_output():
    print("begin")

def teardown_output():
    print("end")

def sign(request):
    key = "124"
    body = request.get("json")
    a = [b for b in body.items()]
    new_body = [str(i) + str(b) for i, b in a if i != "sign" and b]
    new_body.sort()
    print(new_body)
    str_body = "".join(new_body)
    request["json"]["sign"] = str_body + str(key)
    print(str_body + str(key))

    return str_body + str(key)
