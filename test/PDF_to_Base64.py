import base64
with open("C:\\Users\\SanthoshKittane\\Downloads\\Payslip 2026050.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())
    byte64string = encoded_string.decode('utf-8')
    print(byte64string[:100])

