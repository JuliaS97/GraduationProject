# EPIC-3: Ödəniş İdarəetməsi

## GRAD-301-TC-01: Parametrsiz – bütün 6 təchizatçı, sahələr tam
tags: grad-301, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/billers" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri boş olmamalıdır

___

## GRAD-301-TC-02: category=MOBILE – yalnız Azercell + Bakcell
tags: grad-301, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/billers?category=MOBILE" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-301-TC-03: category=UTILITY – Azərişıq + Azərsu
tags: grad-301, pozitiv, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/billers?category=UTILITY" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-301-TC-04: category=INTERNET – komissiya sahələri doğru
tags: grad-301, pozitiv, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/billers?category=INTERNET" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-301-TC-05: category=GAS – 400 VALIDATION_ERROR
tags: grad-301, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/billers?category=GAS" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-301-TC-06: Token olmadan – 401
tags: grad-301, neqativ, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/billers" olsun
* "GET" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-302-TC-01: Etibarlı CityNet ödənişi – 201, total=amount+fee
tags: grad-302, pozitiv, kritik

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc01-citynet-pay-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri boş olmamalıdır

___

## GRAD-302-TC-02: Ödənişdən sonra GET /cards/{id} balansı + spentToday yenilənir
tags: grad-302, pozitiv, kritik

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc02-balance-check-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards/${cardId}" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-302-TC-04: İdempotency replay – eyni key+body → 200, balans İKİNCİ DƏFƏ azalmır
tags: grad-302, pozitiv, kritik

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc04-idempotent-key-fixed"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc04-idempotent-key-fixed"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-302-TC-05: İdempotency conflict – eyni key, fərqli amount → 409
tags: grad-302, neqativ, kritik

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc05-conflict-key-fixed"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc05-conflict-key-fixed"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet-diff.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "409" olmalıdır

___

## GRAD-302-TC-06: Idempotency-Key header yoxdur – 400 IDEMPOTENCY_KEY_REQUIRED
tags: grad-302, neqativ, kritik

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-302-TC-07: BVA – Idempotency-Key 7 simvol (min-1) – 400 INVALID
tags: grad-302, bva, yuksel, neqativ

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "abcdefg"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-302-TC-08: BVA – Idempotency-Key 8 simvol (min) – keçir
tags: grad-302, bva, yuksel

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "abcdefgh"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azerisiq-small.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-302-TC-09: INVALID_SUBSCRIBER – Azercell-ə Bakcell nömrəsi
tags: grad-302, neqativ, yuksel

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc09-invalid-sub-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-invalid-subscriber.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-302-TC-10: BVA – Azercell 0.49 (min-1) – AMOUNT_OUT_OF_RANGE
tags: grad-302, bva, yuksel, neqativ

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc10-amount-min1-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azercell-049.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-302-TC-11: BVA – Azercell 0.50 (min) – qəbul edilir
tags: grad-302, bva, yuksel

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc11-amount-min-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azercell-050.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-302-TC-12: BVA – Azercell 200.00 (max) – qəbul edilir
tags: grad-302, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc06.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc12-amount-max-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azercell-200.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-302-TC-13: BVA – Azercell 200.01 (max+1) – AMOUNT_OUT_OF_RANGE
tags: grad-302, bva, yuksel, neqativ

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc13-amount-max1-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azercell-20001.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-302-TC-15: Aztelekom sabit komissiya 0.50 AZN
tags: grad-302, pozitiv, orta

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc15-aztelekom-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-aztelekom.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-302-TC-16: BVA – total 300.00 (perTransaction limit) – keçir
tags: grad-302, bva, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc06.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc16-pertx-max-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azerisiq-300.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır

___

## GRAD-302-TC-17: BVA – total 300.01 (perTransaction+0.01) – 422 PER_TRANSACTION_LIMIT
tags: grad-302, bva, yuksel, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/cards" olsun
* Add as a header "Authorization" = "token"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/card-tc06.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc17-pertx-max1-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-azerisiq-30001.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-302-TC-21: FROZEN kart ilə ödəniş – 422 CARD_NOT_ACTIVE
tags: grad-302, neqativ, yuksel

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
* Add as a header "Idempotency-Key" = "grad302-tc21-frozen-pay-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-frozen-card.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "422" olmalıdır

___

## GRAD-302-TC-23: amount string ('10') – 400 VALIDATION_ERROR
tags: grad-302, neqativ, yuksel

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc23-string-amount-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-string-amount.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-302-TC-24: Mövcud olmayan billerId – 404 BILLER_NOT_FOUND
tags: grad-302, neqativ, orta

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad302-tc24-notfound-biller-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-unknown-biller.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "404" olmalıdır

___

## GRAD-302-TC-25: Token olmadan – 401
tags: grad-302, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Idempotency-Key" = "grad302-tc25-no-token-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-no-token.json" faylını elave et
* "POST" sorğusu gönder
* Status kodunun "401" olmalıdır

___

## GRAD-303-TC-01: Parametrsiz – default page 1, limit 10, ən yeni birinci
tags: grad-303, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-303-TC-04: BVA – limit=1 (min) – qəbul edilir
tags: grad-303, bva, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?limit=1" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-303-TC-05: BVA – limit=0 (min-1) – 400 VALIDATION_ERROR
tags: grad-303, bva, orta, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?limit=0" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-303-TC-06: BVA – limit=50 (max) – qəbul edilir
tags: grad-303, bva, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?limit=50" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-303-TC-07: BVA – limit=51 (max+1) – 400 VALIDATION_ERROR
tags: grad-303, bva, orta, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?limit=51" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-303-TC-08: BVA – page=0 (min-1) – 400 VALIDATION_ERROR
tags: grad-303, bva, orta, neqativ

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?page=0" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-303-TC-09: page=abc (mətn) – 400 VALIDATION_ERROR
tags: grad-303, neqativ, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?page=abc" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-303-TC-10: from > to – 400 VALIDATION_ERROR
tags: grad-303, neqativ, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?from=2026-10-01&to=2026-09-01" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-303-TC-11: Mövcud olmayan tarix (ay 13) – 400 VALIDATION_ERROR
tags: grad-303, neqativ, orta

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?from=2026-13-01" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "400" olmalıdır

___

## GRAD-303-TC-13: billerId=citynet filtrləməsi
tags: grad-303, pozitiv, yuksel

* GRAD API-ya login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments?billerId=citynet" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-303-TC-14: Sandbox izolyasiyası – user2 user1-in ödənişlərini görə bilmir
tags: grad-303, kritik, tehlukesizlik

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
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* Add as a header "Idempotency-Key" = "grad303-tc14-isolation-001"
* Header elave et "Content-Type" = "application/json"
* Body olaraq "grad/payment-citynet.json" faylını elave et
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* "POST" sorğusu gönder
* Status kodunun "201" olmalıdır
* GRAD API-ya user2 kimi login ol və tokeni yadda saxla
* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* Add as a header "Authorization" = "token"
* "GET" sorğusu gönder
* Status kodunun "200" olmalıdır

___

## GRAD-303-TC-15: Token olmadan – 401
tags: grad-303, neqativ, kritik, tehlukesizlik

* Yeni API sorğusu hazırla
* API base URL "https://api.anarabbas.com" olsun
* Endpoint "/bill-payments" olsun
* "GET" sorğusu gönder
* Status kodunun "401" olmalıdır
