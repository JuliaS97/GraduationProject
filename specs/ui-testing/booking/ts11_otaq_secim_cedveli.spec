# TS-11: Otaq Seçim Cədvəli

## TC-UI-001: Otaq növü məlumatlarının tam göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var roomTable=document.querySelector('[data-testid=\"rooms-table\"],[class*=\"rooms-table\"],[class*=\"hprt-table\"],[id*=\"rooms\"]');if(!roomTable){roomTable=document.querySelector('table,[class*=\"room\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-002: Pulsuz ləğv şərti olan otağın vizual fərqi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var freeCancel=document.querySelector('[data-testid*=\"free-cancel\"],[class*=\"free-cancel\"],[class*=\"free_cancellation\"]');if(!freeCancel){var els=Array.from(document.querySelectorAll('*'));freeCancel=els.find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('free cancellation')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-003: Rezervasiya düyməsinin görünməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"availability-cta-btn\"],[class*=\"reserve\"],[class*=\"book-now\"],[href*=\"reservation\"]');if(!btn){btn=document.querySelector('button[class*=\"cta\"],a[class*=\"cta\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-004: 'No prepayment needed – pay at the property' şərtinin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var els=Array.from(document.querySelectorAll('*'));var el=els.find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('no prepayment')>=0;});if(!el){el=els.find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('pay at the property')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-005: Qonaq rəyinin ümumi balının göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var score=document.querySelector('[data-testid=\"review-score\"],[class*=\"review-score\"],[class*=\"reviewScore\"],[aria-label*=\"Scored\"]');if(!score){score=document.querySelector('[class*=\"score\"],[class*=\"rating\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-006: BVA – Otaq sayı dropdown (min: 0 = seçilməyib)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sel=document.querySelector('select[name*=\"nr\"],select[name*=\"room\"],select[class*=\"room-count\"],[data-testid*=\"room-select\"]');if(sel){sel.value='0';sel.dispatchEvent(new Event('change',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-007: BVA – Otaq sayı dropdown (min+1: 1 otaq)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sel=document.querySelector('select[name*=\"nr\"],select[name*=\"room\"],select[class*=\"room-count\"],[data-testid*=\"room-select\"]');if(sel){sel.value='1';sel.dispatchEvent(new Event('change',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-008: BVA – Otaq sayı dropdown (max: 10 otaq)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sel=document.querySelector('select[name*=\"nr\"],select[name*=\"room\"],select[class*=\"room-count\"],[data-testid*=\"room-select\"]');if(sel){var opts=sel.options;var maxVal=opts[opts.length-1]?opts[opts.length-1].value:'10';sel.value=maxVal;sel.dispatchEvent(new Event('change',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-009: BVA – Otaq qiymətinin düzgün hesablanması (10 otaq × 26 gecə)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-27&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sel=document.querySelector('select[name*=\"nr\"],select[name*=\"room\"],[data-testid*=\"room-select\"]');if(sel){var opts=sel.options;var maxVal=opts[opts.length-1]?opts[opts.length-1].value:'10';sel.value=maxVal;sel.dispatchEvent(new Event('change',{bubbles:true}));}"
* "2" saniye gözle
* JavaScript icra et "var price=document.querySelector('[data-testid=\"price-summary\"],[class*=\"totalPrice\"],[class*=\"total-price\"],[class*=\"price-total\"]');if(!price){price=document.querySelector('[class*=\"price\"],[class*=\"Price\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-010: Səhər yeməyi əlavəsinin qiymətə əksi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var breakfast=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('breakfast')>=0;});if(!breakfast){breakfast=document.querySelector('[class*=\"breakfast\"],[data-testid*=\"breakfast\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-011: Otaq şəkillərinin görünməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var roomImgs=document.querySelectorAll('[class*=\"room\"] img,[data-testid*=\"room\"] img,table img');var loaded=Array.from(roomImgs).filter(function(i){return i.complete&&i.naturalHeight>0;});"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-012: 'Change search' düyməsi ilə axtarışın dəyişdirilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var btn=Array.from(document.querySelectorAll('button,a')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('change search')>=0||(e.textContent||'').toLowerCase().indexOf('modify search')>=0;});if(btn){btn.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla
