# EPIC-1: Benefisiar İdarəetməsi

## GRAD-101-TC-01: Tam etibarlı məlumatlarla alıcı yaradılması (nikneym daxil)
tags: grad-101, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "iban" deyeri boş olmamalıdır
* Json cavabında "nickname" deyeri boş olmamalıdır

___

## GRAD-101-TC-02: IBAN normallaşdırması – boşluqlu kiçik hərflə gəlir, böyük boşluqsuz saxlanır
tags: grad-101, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc02.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "iban" deyeri boş olmamalıdır

___

## GRAD-101-TC-03: nickname göndərilmədikdə cavabda null olur
tags: grad-101, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc03.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-101-TC-04: BVA – fullName 2 simvol (min) – qəbul edilir
tags: grad-101, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc04.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-101-TC-05: BVA – fullName 1 simvol (min-1) – rədd edilir
tags: grad-101, bva, yuksel, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc05.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-101-TC-06: BVA – fullName 50 simvol (max) – qəbul edilir
tags: grad-101, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc06.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-101-TC-07: BVA – fullName 51 simvol (max+1) – rədd edilir
tags: grad-101, bva, yuksel, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc07.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-101-TC-08: fullName rəqəmlə başlayır – rədd edilir
tags: grad-101, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc08.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-101-TC-09: fullName yalnız defisdir – rədd edilir
tags: grad-101, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc09.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-101-TC-10: Çox sahə eyni anda səhv – details-də hər biri ayrıca
tags: grad-101, neqativ, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc10.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-101-TC-11: Eyni IBAN ikinci dəfə – 409 BENEFICIARY_EXISTS
tags: grad-101, neqativ, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc11.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-101-TC-12: Eyni ləqəb (böyük hərflə) – 409 NICKNAME_TAKEN
tags: grad-101, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc12.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-101-TC-13: Öz hesab IBAN-ı əlavə edilir – 422 OWN_ACCOUNT
tags: grad-101, neqativ, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/add-beneficiary-own.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-101-TC-14: 10 alıcı var, 11-ci əlavə edilir – 422 LIMIT_REACHED
tags: grad-101, neqativ, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-1.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-2.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-3.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-4.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-5.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-6.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-7.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-8.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-9.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/debug-ben-10.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/add-beneficiary-limit.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-101-TC-15: Azərbaycan hərfləri + defis fullName-də – qəbul edilir
tags: grad-101, pozitiv, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc15.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-101-TC-16: nickname BVA – 1 simvol (min) – qəbul edilir
tags: grad-101, bva, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc16.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-101-TC-17: nickname BVA – 20 simvol (max) – qəbul edilir
tags: grad-101, bva, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc17.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-101-TC-18: nickname BVA – 21 simvol (max+1) – rədd edilir
tags: grad-101, bva, orta, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc18.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-101-TC-19: Token olmadan – 401
tags: grad-101, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-101-TC-20: Etibarsız JSON body – 400
tags: grad-101, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc20.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-102-TC-01: Parametrsiz – bütün alıcılar, desc sıra (ən yeni birinci)
tags: grad-102, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü en az "1" olmalıdır

___

## GRAD-102-TC-02: sort=fullName&order=asc – əlifba sırası
tags: grad-102, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?sort=fullName&order=asc" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-102-TC-03: currency=USD filtrləməsi
tags: grad-102, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc03.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?currency=USD" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-102-TC-04: q axtarışı – İ/I/ı fərqi nəzərə alınmır
tags: grad-102, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?q=nigar" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü en az "1" olmalıdır

___

## GRAD-102-TC-05: q ləqəb üzrə tapır
tags: grad-102, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?q=Ana" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü en az "1" olmalıdır

___

## GRAD-102-TC-06: BVA – q=1 simvol (min-1) – 400 VALIDATION_ERROR
tags: grad-102, bva, yuksel, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?q=a" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-102-TC-07: BVA – q=2 simvol (min) – qəbul edilir
tags: grad-102, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?q=ni" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-102-TC-08: Heç nə tapılmır – 200, boş siyahı
tags: grad-102, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?q=zxcvbn" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-102-TC-09: Etibarsız currency – 400 VALIDATION_ERROR
tags: grad-102, neqativ, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries?currency=GBP" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-102-TC-10: Sandbox izolyasiyası – user2 user1-in alıcılarını görə bilmir
tags: grad-102, kritik, tehlukesizlik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/ben-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* GRAD API-ya user2 kimi login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-102-TC-11: Token olmadan – 401
tags: grad-102, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* "GET" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-103-TC-01: Mövcud alıcı silinir – 204, body boş
tags: grad-103, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/add-beneficiary-delete-test.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "beneficiaryId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries/${beneficiaryId}" olsun
* Add as a header "Authorization" = "token"
* "DELETE" sorğusu gönder
* Status kodunun "204" olmalıdır

___

## GRAD-103-TC-02: Silinmiş alıcı GET siyahısında yoxdur, total azalıb
tags: grad-103, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/add-beneficiary-delete-test.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "beneficiaryId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries/${beneficiaryId}" olsun
* Add as a header "Authorization" = "token"
* "DELETE" sorğusu gönder
* Status kodunun "204" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-103-TC-03: Artıq silinmiş id – 404 NOT_FOUND
tags: grad-103, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/add-beneficiary-delete-test.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "beneficiaryId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries/${beneficiaryId}" olsun
* Add as a header "Authorization" = "token"
* "DELETE" sorğusu gönder
* Status kodunun "204" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries/${beneficiaryId}" olsun
* Add as a header "Authorization" = "token"
* "DELETE" sorğusu gönder
* Status kodunun "404" olmalıdır

___

## GRAD-103-TC-04: Başqa istifadəçinin alıcısı – 404 NOT_FOUND (IDOR)
tags: grad-103, neqativ, kritik, tehlukesizlik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/add-beneficiary-delete-test.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "beneficiaryId" olaraq yadda saxla
* GRAD API-ya user2 kimi login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries/${beneficiaryId}" olsun
* Add as a header "Authorization" = "token"
* "DELETE" sorğusu gönder
* Status kodunun "404" olmalıdır

___

## GRAD-103-TC-05: Token olmadan – 401
tags: grad-103, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/beneficiaries/test-id-123" olsun
* "DELETE" sorğusu gönder
* Status kodunun "401" olmalıdır
