# -*- coding: utf-8 -*-
import string
def translate(inputed):
    alph = list(string.ascii_lowercase+'ab')
    result = ''
    for i in list(inputed):
        if i.isalpha():
            result += alph[alph.index(i)+2]
        else:
            result += i

    print(result)

translate("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb "
          "rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

def translate_2(inputed):
    alph = string.ascii_lowercase
    new_alph = string.ascii_lowercase[2:] + string.ascii_lowercase [:2]
    trantab = str.maketrans(alph, new_alph)
    print(inputed.translate(trantab))

translate_2("g fmnc wms bgblr rpylqjyrc gr zw fylb.")
translate('map')
