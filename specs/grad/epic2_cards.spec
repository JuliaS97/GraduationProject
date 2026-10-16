# EPIC-2: Kart İdarəetməsi

## GRAD-201-TC-01: Etibarlı sorğu – kart ACTIVE, limitlər standart
tags: grad-201, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır
* Json cavabında "status" deyeri boş olmamalıdır

___

## GRAD-201-TC-02: maskedPan formatı + expiry 3 il sonra
tags: grad-201, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "maskedPan" deyeri boş olmamalıdır
* Json cavabında "expiry" deyeri boş olmamalıdır

___

## GRAD-201-TC-03: label olmadan – null qaytarılır
tags: grad-201, pozitiv, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc03.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-201-TC-04: BVA – initialAmount 1.00 (min) – qəbul edilir
tags: grad-201, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc04.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-201-TC-05: BVA – initialAmount 0.99 (min-1) – rədd edilir
tags: grad-201, bva, yuksel, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc05.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-201-TC-06: BVA – initialAmount 1000.00 (max) – qəbul edilir
tags: grad-201, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc06.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-201-TC-07: BVA – initialAmount 1000.01 (max+1) – rədd edilir
tags: grad-201, bva, yuksel, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc07.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-201-TC-08: initialAmount string ('50') – 400 VALIDATION_ERROR
tags: grad-201, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc08.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-201-TC-09: initialAmount 3 onluq – rədd edilir
tags: grad-201, neqativ, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc09.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-201-TC-10: Başqa istifadəçinin hesabı – 403 FORBIDDEN
tags: grad-201, neqativ, kritik, tehlukesizlik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc10.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "403" olmalıdır

___

## GRAD-201-TC-11: Balansdan çox – 422 INSUFFICIENT_FUNDS
tags: grad-201, neqativ, yuksel

* GRAD API-ya user2 kimi login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc11.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-201-TC-12: 3 ACTIVE kart var, 4-cü – 422 CARD_LIMIT_REACHED
tags: grad-201, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc12a.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc12b.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc12c.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-201-TC-13: 1 BLOCKED + 2 ACTIVE kart – yeni kart yaranır (BLOCKED sayılmır)
tags: grad-201, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc13a.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "blockCardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${blockCardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-lost.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc13b.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc13c.json" faylını elave et
* "POST" sorğusu gönder
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc13d.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-201-TC-14: Token olmadan – 401
tags: grad-201, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-202-TC-01: Yeni kart – GET cavabı POST cavabı ilə eynidir
tags: grad-202, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri boş olmamalıdır

___

## GRAD-202-TC-02: Başqa istifadəçinin kartı – 404 NOT_FOUND
tags: grad-202, neqativ, kritik, tehlukesizlik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* GRAD API-ya user2 kimi login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "404" olmalıdır

___

## GRAD-202-TC-03: Token olmadan – 401
tags: grad-202, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/test-card-id" olsun
* "GET" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-203-TC-01: ACTIVE + TEMPORARY → FROZEN
tags: grad-203, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri boş olmamalıdır

___

## GRAD-203-TC-02: ACTIVE + LOST → BLOCKED
tags: grad-203, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-lost.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-203-TC-03: FROZEN + STOLEN → BLOCKED (eskalasiya)
tags: grad-203, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-stolen.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-203-TC-04: FROZEN + TEMPORARY → 409 ALREADY_FROZEN
tags: grad-203, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-203-TC-05: BLOCKED + TEMPORARY → 409 CARD_BLOCKED
tags: grad-203, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-lost.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-203-TC-06: BLOCKED + LOST → 409 CARD_BLOCKED
tags: grad-203, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-stolen.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-lost.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-203-TC-07: Etibarsız reason – 400 VALIDATION_ERROR
tags: grad-203, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-invalid.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-203-TC-08: reason yoxdur – 400 VALIDATION_ERROR
tags: grad-203, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-empty.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-203-TC-09: FROZEN kart ilə ödəniş cəhdi – 422 CARD_NOT_ACTIVE
tags: grad-203, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "frozen-card-pay-test-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-frozen-card.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-203-TC-10: Token olmadan – 401
tags: grad-203, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/test-card-id/block" olsun
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-204-TC-01: FROZEN kart ACTIVE edilir
tags: grad-204, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/unblock" olsun
* Add as a header "Authorization" = "token"
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri boş olmamalıdır

___

## GRAD-204-TC-02: ACTIVE kart unblock – 409 NOT_FROZEN
tags: grad-204, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/unblock" olsun
* Add as a header "Authorization" = "token"
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-204-TC-03: BLOCKED kart unblock – 409 PERMANENTLY_BLOCKED
tags: grad-204, neqativ, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-stolen.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/unblock" olsun
* Add as a header "Authorization" = "token"
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-204-TC-04: Açılmış kartla ödəniş uğurlu keçir
tags: grad-204, pozitiv, kritik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc04b.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/unblock" olsun
* Add as a header "Authorization" = "token"
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "unblock-pay-test-001"
* Header elave et "Content-Type" = "application/json"
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Body olaraq "grad/payment-unblock-test.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-204-TC-05: Başqa istifadəçinin kartını açmaq – 404 NOT_FOUND
tags: grad-204, neqativ, kritik, tehlukesizlik

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc01.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/block" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/block-temporary.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır
* GRAD API-ya user2 kimi login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}/unblock" olsun
* Add as a header "Authorization" = "token"
* "POST" sorğusu gönder
* Status kodunun "404" olmalıdır

___

## GRAD-204-TC-06: Token olmadan – 401
tags: grad-204, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/test-card-id/unblock" olsun
* "POST" sorğusu gönder
* Status kodunun "401" olmalıdır
