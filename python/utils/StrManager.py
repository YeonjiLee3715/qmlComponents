#!/usr/bin/env python
# coding: utf8

import unicodedata

def CaselessEqual(str1: str, str2: str) -> bool:
    return str1.lower() == str2.lower() # unicode text는 잘 못 변환 된다고 함. 아래의 함수 사용

# unicode용
def NormalizeCaseless(text) -> str:
    return unicodedata.normalize("NFKD", text.casefold())

# unicode용
def UCaselessEqual(str1, str2) -> bool:
    return NormalizeCaseless(str1) == NormalizeCaseless(str2)