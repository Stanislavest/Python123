#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1
import re
# s = "my-p@ssw0rd"
# reg = r'[0-9A-Za-z@_-]{6,18}'
# print(re.findall(reg, s))

#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# s = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, " \
#     "были зафиксированы максимумы месячных осадков."
# # reg = r'([0-2][0-9]|[3][01][/][0][1-9]|[1][12][/][2][0][2][1])'
# reg = r'\d+[/]\d+[/]\d+'
# print(re.findall(reg, s))
# # print(re.sub(reg, s))

#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

s = "+7 499 456-45-78 +74994564578 7 (499) 456 45 78 7 (499) 456-45-78"
reg = r'[+]?[7]\s?[(]?\d{3}[)]?\s?[\s]?\d{3}[\s-]?\d{2}[\s-]?\d{2}'
print(re.findall(reg, s))

