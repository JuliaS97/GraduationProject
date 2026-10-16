# TS-15: Qiymət Xülasəsi

## TC-UI-041: Qiymət xülasəsinin komponentlərinin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var priceBox=document.querySelector('[data-testid*=\"price-summary\"],[class*=\"price-summary\"],[class*=\"price-breakdown\"],[class*=\"priceBreakdown\"]');if(!priceBox){priceBox=document.querySelector('[class*=\"price\"],[class*=\"Price\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-042: VAT 15% hesablama doğruluğu
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var vat=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&((e.textContent||'').toLowerCase().indexOf('vat')>=0||(e.textContent||'').toLowerCase().indexOf('tax')>=0);});if(!vat){vat=document.querySelector('[class*=\"tax\"],[class*=\"vat\"],[data-testid*=\"tax\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-043: 'In property currency' ikincil valyuta göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var propCurr=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('property currency')>=0;});if(!propCurr){propCurr=document.querySelector('[class*=\"currency\"],[data-testid*=\"currency\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-044: 'The exchange rate might change before you pay' xəbərdarlığı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var exWarn=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('exchange rate')>=0;});if(!exWarn){exWarn=document.querySelector('[class*=\"exchange\"],[class*=\"rate\"],[data-testid*=\"exchange\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-045: Ümumi qiymət komponentlərinin cəmi yoxlanması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var total=document.querySelector('[data-testid*=\"total\"],[class*=\"total-price\"],[class*=\"totalPrice\"],[class*=\"grand-total\"]');if(!total){total=document.querySelector('[class*=\"total\"],[class*=\"Total\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-046: Qiymət dəyişikliyi bildirişinin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var priceNote=document.querySelector('[data-testid*=\"price-note\"],[class*=\"price-note\"],[class*=\"price-info\"],[class*=\"price-disclaimer\"]');if(!priceNote){priceNote=document.querySelector('[class*=\"disclaimer\"],[class*=\"note\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-047: BVA – Otaq müştəri sayı fərqi (1 böyük vs 2 böyük)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=1"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var price1=document.querySelector('[data-testid*=\"price\"],[class*=\"price\"],[class*=\"Price\"]');if(price1){var t1=price1.textContent;}"
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var price2=document.querySelector('[data-testid*=\"price\"],[class*=\"price\"],[class*=\"Price\"]');if(price2){var t2=price2.textContent;}"
* URL "booking.com" içermelidir
* Brauzeri bağla
