# TS-14: Rezervasiya Formu UI

## TC-UI-029: 3 addımlı progress bar-ın görünüşü
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var pb=document.querySelector('[data-testid*=\"progress\"],[class*=\"progress-bar\"],[class*=\"progressBar\"],[class*=\"stepper\"],[role=\"progressbar\"]');if(!pb){pb=document.querySelector('[class*=\"step\"],[class*=\"wizard\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-030: Sol paneldə rezervasiya xülasəsinin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var summary=document.querySelector('[data-testid*=\"booking-summary\"],[class*=\"booking-summary\"],[class*=\"sidebar\"],[class*=\"order-summary\"]');if(!summary){summary=document.querySelector('[class*=\"summary\"],[class*=\"panel\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-031: 'Just 3 days away!' xəbərdarlığının göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var warn=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('days away')>=0;});if(!warn){warn=document.querySelector('[class*=\"urgency\"],[class*=\"warning\"],[data-testid*=\"urgency\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-032: 'Change your selection' ilə otaq seçiminə qayıdış
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var btn=Array.from(document.querySelectorAll('button,a')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('change your selection')>=0||(e.textContent||'').toLowerCase().indexOf('change selection')>=0;});if(btn){btn.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-033: Ölkə/Region seçimi – Azerbaijan default
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var countrySel=document.querySelector('select[name*=\"country\"],select[id*=\"country\"],[data-testid*=\"country\"],[class*=\"country-select\"]');if(countrySel){var val=countrySel.value;}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-034: Telefon ölkə prefiksi seçimi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var prefixSel=document.querySelector('select[name*=\"phone_prefix\"],select[name*=\"dialcode\"],[data-testid*=\"phone-prefix\"],[class*=\"phone-prefix\"],[class*=\"dial-code\"]');if(prefixSel){prefixSel.dispatchEvent(new Event('click',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-035: E-poçt ünvanının avtomatik doldurulması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var emailInp=document.querySelector('input[type=\"email\"],input[name=\"email\"],input[autocomplete=\"email\"]');if(emailInp){var val=emailInp.value;}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-036: SMS bildiriş seçiminin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sms=document.querySelector('[data-testid*=\"sms\"],[class*=\"sms\"],[name*=\"sms\"],[id*=\"sms\"]');if(!sms){sms=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('sms')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-037: 'Sign in' ilə hesaba daxilolma linki
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var signIn=document.querySelector('a[href*=\"signin\"],a[href*=\"login\"],[data-testid*=\"sign-in\"],[class*=\"signin\"]');if(!signIn){signIn=Array.from(document.querySelectorAll('a,button')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('sign in')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-038: Boş forma göndərmə – validasiya mesajları
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sub=document.querySelector('button[type=\"submit\"],[data-testid*=\"submit\"],[class*=\"submit-btn\"],[class*=\"next-btn\"]');if(sub){sub.click();}"
* "2" saniye gözle
* JavaScript icra et "var errs=document.querySelectorAll('[class*=\"error\"],[class*=\"invalid\"],[role=\"alert\"],[aria-invalid=\"true\"]');var hasErr=errs.length>0;"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-039: Xətalı sahəyə fokuslanma – 'Enter your first name'
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sub=document.querySelector('button[type=\"submit\"],[data-testid*=\"submit\"],[class*=\"submit-btn\"]');if(sub){sub.click();}"
* "2" saniye gözle
* JavaScript icra et "var firstNameErr=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('first name')>=0&&(e.closest('[class*=\"error\"]')||e.className.indexOf('error')>=0);});if(!firstNameErr){firstNameErr=document.querySelector('[class*=\"error\"],[aria-invalid=\"true\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla
