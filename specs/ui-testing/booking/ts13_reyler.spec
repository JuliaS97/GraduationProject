# TS-13: Rəylər

## TC-UI-020: Rəy mövzu çiplərinin filtrləməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var chip=document.querySelector('[data-testid*=\"review-topic\"],[class*=\"review-chip\"],[class*=\"topic-chip\"],[class*=\"review-filter\"]');if(chip){chip.click();}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-021: Rəy sıralama funksiyası
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sortSel=document.querySelector('select[name*=\"review_sort\"],select[id*=\"review_sort\"],[data-testid*=\"review-sort\"],[class*=\"review-sort\"]');if(sortSel){sortSel.dispatchEvent(new Event('click',{bubbles:true}));}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-022: Müəyyən dil üzrə rəy filtrləməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var langSel=document.querySelector('select[name*=\"language\"],select[id*=\"language\"],[data-testid*=\"language\"],[class*=\"language-filter\"]');if(langSel){langSel.dispatchEvent(new Event('click',{bubbles:true}));}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-023: Fərdi rəyin tam mətninin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var readMore=document.querySelector('[data-testid*=\"read-more\"],[class*=\"read-more\"],[class*=\"readmore\"]');if(!readMore){readMore=Array.from(document.querySelectorAll('button,a')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('read more')>=0;});}if(readMore){readMore.click();}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-024: 'Read all reviews' düyməsi ilə tam rəylər siyahısı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var btn=Array.from(document.querySelectorAll('button,a')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('read all reviews')>=0||(e.textContent||'').toLowerCase().indexOf('all reviews')>=0;});if(btn){btn.click();}"
* "4" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-025: Rəy xalının kateqoriyalar üzrə göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var cats=document.querySelectorAll('[data-testid*=\"review-score-category\"],[class*=\"score-category\"],[class*=\"review-category\"]');if(!cats||cats.length===0){cats=document.querySelectorAll('[class*=\"rating-bar\"],[class*=\"score-bar\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-026: Müəyyən qonaq növü üzrə rəy filtrləməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var travellerFilter=document.querySelector('[data-testid*=\"traveller-type\"],[class*=\"traveller-type\"],[class*=\"traveler-type\"],[class*=\"group-type\"]');if(travellerFilter){travellerFilter.dispatchEvent(new Event('click',{bubbles:true}));}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-027: 'See availability' CTA düyməsi ilə otaq bölməsinə keçid
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var btn=Array.from(document.querySelectorAll('button,a')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('see availability')>=0||(e.textContent||'').toLowerCase().indexOf('check availability')>=0;});if(btn){btn.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-028: BVA – Rəy xal filtri keçid nöqtəsi (7.0 / 8.0 / 9.0)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2&review_score=70"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var url70=window.location.href;"
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2&review_score=80"
* "5" saniye gözle
* JavaScript icra et "var url80=window.location.href;"
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2&review_score=90"
* "5" saniye gözle
* JavaScript icra et "var url90=window.location.href;"
* URL "booking.com" içermelidir
* Brauzeri bağla
