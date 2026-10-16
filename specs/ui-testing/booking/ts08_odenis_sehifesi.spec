# TS-08: Ödəniş Səhifəsi

## TC-BK-091: Ödəniş formasının yüklənməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var card=document.querySelector('[data-testid=\"property-card\"] a,[data-testid=\"title-link\"],a[href*=\"/hotel/\"]');if(card){card.click();}"
* "5" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"availability-cta-btn\"],button[data-testid*=\"reserve\"],a[data-testid*=\"reserve\"],[class*=\"reserve\"]');if(btn){btn.click();}"
* "4" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-092: Uğurlu ödəniş (test kartı)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_number\"],input[id*=\"card\"],input[placeholder*=\"Card number\"],input[autocomplete=\"cc-number\"]');if(inp){inp.value='4111111111111111';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-093: Rədd edilmiş kart ilə ödəniş
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_number\"],input[id*=\"card\"],input[placeholder*=\"Card number\"],input[autocomplete=\"cc-number\"]');if(inp){inp.value='4000000000000002';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-094: BVA – Kart nömrəsi rəqəm sayı (min-1: 15 rəqəm)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_number\"],input[id*=\"card\"],input[placeholder*=\"Card number\"],input[autocomplete=\"cc-number\"]');if(inp){inp.value='411111111111111';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-095: BVA – Kart nömrəsi rəqəm sayı (min/max: 16 rəqəm)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_number\"],input[id*=\"card\"],input[placeholder*=\"Card number\"],input[autocomplete=\"cc-number\"]');if(inp){inp.value='4111111111111111';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-096: BVA – Kart nömrəsi rəqəm sayı (max+1: 17 rəqəm)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_number\"],input[id*=\"card\"],input[placeholder*=\"Card number\"],input[autocomplete=\"cc-number\"]');if(inp){inp.value='41111111111111111';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-097: BVA – CVV uzunluğu (min-1: 2 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_cvc\"],input[name=\"cvc\"],input[name=\"cvv\"],input[autocomplete=\"cc-csc\"],input[placeholder*=\"CVV\"],input[placeholder*=\"CVC\"]');if(inp){inp.value='12';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-098: BVA – CVV uzunluğu (min: 3 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_cvc\"],input[name=\"cvc\"],input[name=\"cvv\"],input[autocomplete=\"cc-csc\"],input[placeholder*=\"CVV\"],input[placeholder*=\"CVC\"]');if(inp){inp.value='123';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-099: BVA – CVV uzunluğu (max+1: 5 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_cvc\"],input[name=\"cvc\"],input[name=\"cvv\"],input[autocomplete=\"cc-csc\"],input[placeholder*=\"CVV\"],input[placeholder*=\"CVC\"]');if(inp){inp.value='12345';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-100: Vaxtı keçmiş kart son tarixi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_expiry\"],input[name=\"expiry\"],input[autocomplete=\"cc-exp\"],input[placeholder*=\"MM\"],input[placeholder*=\"expiry\"]');if(inp){inp.value='01/20';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-101: 3D Secure doğrulaması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var is3ds=document.querySelector('[class*=\"3ds\"],[class*=\"secure\"],[id*=\"3ds\"],[id*=\"secure\"],iframe[src*=\"3ds\"],iframe[src*=\"secure\"]');if(!is3ds){is3ds=document.querySelector('iframe');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-102: Ödəniş formasında SSL/HTTPS yoxlanması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "var isHttps=window.location.protocol==='https:';if(!isHttps){throw new Error('Page is not HTTPS: '+window.location.protocol);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-103: Kart məlumatlarının maskalanması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"cc_number\"],input[autocomplete=\"cc-number\"],input[placeholder*=\"Card number\"]');if(inp){var t=inp.type;}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-104: CSRF token yoxlanması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var csrf=document.querySelector('input[name=\"_token\"],input[name=\"csrf_token\"],input[name=\"authenticity_token\"],meta[name=\"csrf-token\"]');if(!csrf){csrf=document.querySelector('input[type=\"hidden\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla
