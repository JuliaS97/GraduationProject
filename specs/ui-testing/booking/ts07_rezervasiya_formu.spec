# TS-07: Rezervasiya Formu

## TC-BK-075: Rezervasiya formasının yüklənməsi
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

## TC-BK-076: Qonaq məlumatlarının doldurulması (pozitiv)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"],input[placeholder*=\"First\"],input[placeholder*=\"first\"]');if(inp){inp.focus();inp.value='Test';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* JavaScript icra et "var inp=document.querySelector('input[name=\"lastname\"],input[id*=\"last\"],input[placeholder*=\"Last\"],input[placeholder*=\"last\"]');if(inp){inp.focus();inp.value='User';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* JavaScript icra et "var inp=document.querySelector('input[name=\"email\"],input[type=\"email\"]');if(inp){inp.focus();inp.value='test@example.com';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-077: BVA – Ad sahəsi uzunluğu (min-1: 0 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');if(inp){inp.value='';inp.dispatchEvent(new Event('input',{bubbles:true}));var form=inp.closest('form');if(form){var sub=form.querySelector('[type=\"submit\"]');if(sub){sub.click();}}}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-078: BVA – Ad sahəsi uzunluğu (min: 1 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');if(inp){inp.value='A';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-079: BVA – Ad sahəsi uzunluğu (max: 50 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');if(inp){inp.value='Abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwx';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-080: BVA – Ad sahəsi uzunluğu (max+1: 51 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');if(inp){inp.value='Abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-081: Telefon nömrəsi formatı yoxlanması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"phone\"],input[type=\"tel\"],input[id*=\"phone\"]');if(inp){inp.value='abc-def-ghij';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-082: BVA – Telefon rəqəm sayı (min-1: 6 rəqəm)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"phone\"],input[type=\"tel\"],input[id*=\"phone\"]');if(inp){inp.value='123456';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-083: BVA – Telefon rəqəm sayı (min: 7 rəqəm)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"phone\"],input[type=\"tel\"],input[id*=\"phone\"]');if(inp){inp.value='1234567';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-084: BVA – Telefon rəqəm sayı (max: 15 rəqəm – E.164)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"phone\"],input[type=\"tel\"],input[id*=\"phone\"]');if(inp){inp.value='123456789012345';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-085: BVA – Telefon rəqəm sayı (max+1: 16 rəqəm)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"phone\"],input[type=\"tel\"],input[id*=\"phone\"]');if(inp){inp.value='1234567890123456';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-086: Məcburi sahələrin boş buraxılması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inputs=document.querySelectorAll('input[required],input[name=\"firstname\"],input[name=\"lastname\"],input[name=\"email\"]');inputs.forEach(function(i){i.value='';i.dispatchEvent(new Event('input',{bubbles:true}));});"
* JavaScript icra et "var sub=document.querySelector('button[type=\"submit\"],[data-testid*=\"submit\"],[class*=\"submit\"]');if(sub){sub.click();}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-087: BVA – Xüsusi istək simvol sayı (max: 500 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var ta=document.querySelector('textarea[name*=\"request\"],textarea[name*=\"special\"],textarea[id*=\"request\"],textarea[placeholder*=\"request\"]');if(ta){ta.value=new Array(501).join('a');ta.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-088: BVA – Xüsusi istək simvol sayı (max+1: 501 simvol)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var ta=document.querySelector('textarea[name*=\"request\"],textarea[name*=\"special\"],textarea[id*=\"request\"],textarea[placeholder*=\"request\"]');if(ta){ta.value=new Array(502).join('a');ta.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-089: Qiymət xülasəsinin doğruluğu
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var price=document.querySelector('[data-testid=\"price-summary\"],[class*=\"price-summary\"],[class*=\"totalPrice\"],[class*=\"total-price\"]');if(!price){price=document.querySelector('[class*=\"price\"],[class*=\"Price\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-090: XSS – Ad sahəsindəki skript
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');if(inp){inp.value='<script>alert(1)<\/script>';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla
