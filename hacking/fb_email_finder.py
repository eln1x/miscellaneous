#!/usr/bin/env python
import requests


#GET /ajax/registration/validation/contactpoint_invalid/?contactpoint=targetuser@%40gmail.com&dpr=1&__user=0&__a=1&__dyn=7xeXxaER2HwNJ0ZwRAKxZ3ocWwAyUG4XzEa8uwh9UcU88lwIyo8obo6ucxG48hwv9FovgeFUuzUhzE2HBUfE&__af=i0&__req=u&__be=-1&__pc=PHASED%3ADEFAULT&__rev=2812196 HTTP/1.1
#Host: www.facebook.com
#Connection: close
#User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36
#Accept: */*
#DNT: 1
#Referer: https://www.facebook.com/
#Accept-Language: en-US,en;q=0.8,ar;q=0.6
#Cookie: fr=0w9ltXPCDeivFFgEE..BYlEsH.hv.AAA.0.0.BYlEsH.AWX0q9Sd; datr=B0uUWOYAb94Xg5ao5OjlbkWq; reg_fb_ref=https%3A%2F%2Fwww.facebook.com%2F; reg_fb_gate=https%3A%2F%2Fwww.facebook.com%2F; wd=1319x776

#for (;;);{"__ar":1,"__sf":"i0","payload":{"valid":false,"error":null},"bootloadable":{},"ixData":{},"lid":"21778252211"}
cookies = dict(fr='0w9ltXPCDeiE..BYlEsH.hv.AAA.0.0.BYlEsH.AWX0q9Sd', datr='B0uUWOYA94Xg5ao5OjlbkWq', reg_fb_ref='https%3A%2F%2Fwww.facebook.com%2F', reg_fb_gate='https%3A%2F%2Fwww.facebook.com%2F', wd='1319x776')


