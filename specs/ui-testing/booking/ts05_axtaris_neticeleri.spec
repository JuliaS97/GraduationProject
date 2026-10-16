# TS-05: Otel Axtarış Nəticələri

## TC-BK-050: Nəticələrin qiymətə görə sıralanması (aşağıdan yuxarı)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sortBtn=document.querySelector('[data-testid=\"sorters-dropdown-trigger\"],[data-testid=\"sorter-dropdown\"],[data-testid=\"sort-by\"],[class*=\"sort\"] button,[class*=\"Sort\"] button');if(!sortBtn){var allBtns=document.querySelectorAll('button');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||allBtns[i].getAttribute('aria-label')||'').toLowerCase();if(t.indexOf('sort')>=0||t.indexOf('order')>=0){sortBtn=allBtns[i];break;}}} if(sortBtn){sortBtn.click();} "
* "2" saniye gözle
* JavaScript icra et "var priceAsc=null;var opts=document.querySelectorAll('[data-testid=\"sorter-item\"],[role=\"option\"],[class*=\"sort-item\"],[class*=\"sortItem\"],[class*=\"dropdown\"] li,[class*=\"Dropdown\"] li,li[class*=\"item\"]');for(var i=0;i<opts.length;i++){var t=(opts[i].textContent||'').toLowerCase();if(t.indexOf('price')>=0&&(t.indexOf('low')>=0||t.indexOf('asc')>=0||t.indexOf('cheap')>=0||t.indexOf('ascending')>=0)){priceAsc=opts[i];break;}} if(!priceAsc){for(var i=0;i<opts.length;i++){var t=(opts[i].textContent||'').toLowerCase();if(t.indexOf('price')>=0){priceAsc=opts[i];break;}}} if(!priceAsc){var allAs=document.querySelectorAll('a[href*=\"price\"],a[href*=\"sort\"]');if(allAs.length>0)priceAsc=allAs[0];} if(priceAsc){priceAsc.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-051: Nəticələrin reytinqə görə sıralanması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sortBtn=document.querySelector('[data-testid=\"sorters-dropdown-trigger\"],[data-testid=\"sorter-dropdown\"],[data-testid=\"sort-by\"],[class*=\"sort\"] button,[class*=\"Sort\"] button');if(!sortBtn){var allBtns=document.querySelectorAll('button');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||allBtns[i].getAttribute('aria-label')||'').toLowerCase();if(t.indexOf('sort')>=0||t.indexOf('order')>=0){sortBtn=allBtns[i];break;}}} if(sortBtn){sortBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var ratingOpt=null;var opts=document.querySelectorAll('[data-testid=\"sorter-item\"],[role=\"option\"],[class*=\"sort-item\"],[class*=\"sortItem\"],[class*=\"dropdown\"] li,[class*=\"Dropdown\"] li,li[class*=\"item\"]');for(var i=0;i<opts.length;i++){var t=(opts[i].textContent||'').toLowerCase();if(t.indexOf('rating')>=0||t.indexOf('review')>=0||t.indexOf('score')>=0||t.indexOf('star')>=0||t.indexOf('top')>=0||t.indexOf('best')>=0){ratingOpt=opts[i];break;}} if(ratingOpt){ratingOpt.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-052: Populyar filtr – Pulsuz Wi-Fi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var filter=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"],[class*=\"facility\"]');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if(t.indexOf('wi-fi')>=0||t.indexOf('wifi')>=0||t.indexOf('wireless')>=0){filter=allEls[i];break;}} if(!filter){var allInputs=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<allInputs.length;i++){var lbl=allInputs[i].closest('label')||document.querySelector('label[for=\"'+allInputs[i].id+'\"]');if(lbl){var t=(lbl.textContent||'').toLowerCase();if(t.indexOf('wifi')>=0||t.indexOf('wi-fi')>=0){filter=lbl;break;}}}} if(filter){filter.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-053: Populyar filtr – Kredit kartısız sifariş
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var filter=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"],[class*=\"facility\"],[class*=\"filter\"] span,[class*=\"Filter\"] span');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if(t.indexOf('no credit card')>=0||t.indexOf('without credit')>=0||t.indexOf('book without')>=0||t.indexOf('no card')>=0||t.indexOf('kredit')>=0){filter=allEls[i];break;}} if(!filter){var allInputs=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<allInputs.length;i++){var lbl=allInputs[i].closest('label')||document.querySelector('label[for=\"'+allInputs[i].id+'\"]');if(lbl){var t=(lbl.textContent||'').toLowerCase();if(t.indexOf('credit')>=0||t.indexOf('card')>=0){filter=lbl;break;}}}} if(filter){filter.click();} "
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-054: Populyar filtr – Səhər yeməyi daxil
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var filter=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"],[class*=\"meal\"],[class*=\"board\"],[class*=\"filter\"] span,[class*=\"Filter\"] span');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if(t.indexOf('breakfast')>=0||t.indexOf('səhər')>=0||(t.indexOf('included')>=0&&t.indexOf('meal')>=0)){filter=allEls[i];break;}} if(!filter){var allInputs=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<allInputs.length;i++){var lbl=allInputs[i].closest('label')||document.querySelector('label[for=\"'+allInputs[i].id+'\"]');if(lbl){var t=(lbl.textContent||'').toLowerCase();if(t.indexOf('breakfast')>=0){filter=lbl;break;}}}} if(filter){filter.click();} "
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-055: Rəy balı filtri – 9+ Əla
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var filter=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"]');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if((t.indexOf('9')>=0&&(t.indexOf('wonderful')>=0||t.indexOf('exceptional')>=0||t.indexOf('superb')>=0))||(t.indexOf('9+')>=0)){filter=allEls[i];break;}} if(!filter){var allInputs=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<allInputs.length;i++){if(allInputs[i].value==='90'||allInputs[i].id&&allInputs[i].id.indexOf('score9')>=0){var lbl=allInputs[i].closest('label')||document.querySelector('label[for=\"'+allInputs[i].id+'\"]');if(lbl){filter=lbl;break;}}}} if(filter){filter.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-056: Rəy balı filtri – 8+ Çox yaxşı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var filter=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"]');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if((t.indexOf('8')>=0&&(t.indexOf('very good')>=0||t.indexOf('great')>=0))||(t.indexOf('8+')>=0)){filter=allEls[i];break;}} if(!filter){var allInputs=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<allInputs.length;i++){if(allInputs[i].value==='80'||allInputs[i].id&&allInputs[i].id.indexOf('score8')>=0){var lbl=allInputs[i].closest('label')||document.querySelector('label[for=\"'+allInputs[i].id+'\"]');if(lbl){filter=lbl;break;}}}} if(filter){filter.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-057: BVA – Rəy balı (min: 1.0)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2&review_score=10"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-058: BVA – Rəy balı (max: 10.0)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2&review_score=100"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var results=document.querySelectorAll('[data-testid=\"property-card\"],[data-testid=\"sr-card\"],[class*=\"sr_item\"],[class*=\"property-card\"]');var noResults=document.querySelector('[data-testid=\"no-results\"],[class*=\"no-results\"],[class*=\"noResults\"]');var isAcceptable=results.length>=0||noResults;if(!isAcceptable){throw new Error('Unexpected page state for max score filter');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-059: Çoxlu filtrlərin birlikdə tətbiqi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var wifi=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"],[class*=\"facility\"],[class*=\"filter\"] span');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if(t.indexOf('wi-fi')>=0||t.indexOf('wifi')>=0||t.indexOf('wireless')>=0){wifi=allEls[i];break;}} if(!wifi){var inps=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<inps.length;i++){var lbl=inps[i].closest('label')||document.querySelector('label[for=\"'+inps[i].id+'\"]');if(lbl&&(lbl.textContent||'').toLowerCase().indexOf('wifi')>=0){wifi=lbl;break;}}} if(wifi){wifi.click();}"
* "2" saniye gözle
* JavaScript icra et "var score=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"]');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if(t.indexOf('7')>=0&&(t.indexOf('good')>=0||t.indexOf('pleasant')>=0)){score=allEls[i];break;}} if(!score){var allEls2=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<allEls2.length;i++){if(allEls2[i].value==='70'||allEls2[i].id&&allEls2[i].id.indexOf('score7')>=0){var lbl=allEls2[i].closest('label');if(lbl){score=lbl;break;}}}} if(score){score.click();}"
* "3" saniye gözle
* JavaScript icra et "var onBooking=window.location.href.indexOf('booking.com')>=0;if(!onBooking){throw new Error('Not on booking.com after applying multiple filters');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-060: Filtr sıfırlama
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var wifi=null;var allEls=document.querySelectorAll('label,li,[data-testid*=\"filter\"],[class*=\"filter-item\"],[class*=\"filterItem\"],[class*=\"facility\"],[class*=\"filter\"] span');for(var i=0;i<allEls.length;i++){var t=(allEls[i].textContent||'').toLowerCase();if(t.indexOf('wi-fi')>=0||t.indexOf('wifi')>=0){wifi=allEls[i];break;}} if(!wifi){var inps=document.querySelectorAll('input[type=\"checkbox\"]');for(var i=0;i<inps.length;i++){var lbl=inps[i].closest('label')||document.querySelector('label[for=\"'+inps[i].id+'\"]');if(lbl&&(lbl.textContent||'').toLowerCase().indexOf('wifi')>=0){wifi=lbl;break;}}} if(wifi){wifi.click();}"
* "3" saniye gözle
* JavaScript icra et "var resetBtn=document.querySelector('[data-testid=\"filter-bar-reset\"],[data-testid=\"reset-filters\"],[data-testid=\"filters-reset\"],[data-testid=\"filter-clear-all\"]');if(!resetBtn){resetBtn=document.querySelector('[class*=\"reset\"] button,button[class*=\"reset\"],[class*=\"clear\"] button,button[class*=\"clear\"],[class*=\"Reset\"] button,button[class*=\"Clear\"]');} if(!resetBtn){var allBtns=document.querySelectorAll('button,a');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||'').toLowerCase().trim();if(t==='reset'||t==='clear all'||t==='clear filters'||t==='remove all filters'||t==='delete all filters'||(t.indexOf('reset')>=0&&t.length<30)||(t.indexOf('clear')>=0&&t.indexOf('filter')>=0)){resetBtn=allBtns[i];break;}}} if(resetBtn){resetBtn.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-061: Xəritə görünüşü
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var mapBtn=document.querySelector('[data-testid=\"map-trigger\"],[data-testid=\"show-map-button\"],[data-testid=\"map-button\"],[data-testid=\"sr-map-container\"] button,[data-testid=\"map-cta\"],[aria-label*=\"map\"],[aria-label*=\"Map\"]');if(!mapBtn){mapBtn=document.querySelector('[class*=\"map-trigger\"],[class*=\"mapTrigger\"],[class*=\"show-map\"],[class*=\"showMap\"],[class*=\"MapTrigger\"],[class*=\"map-btn\"],[class*=\"mapBtn\"]');} if(!mapBtn){var allBtns=document.querySelectorAll('button,a');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||allBtns[i].getAttribute('aria-label')||'').toLowerCase().trim();if(t.indexOf('map')>=0&&t.length<50){mapBtn=allBtns[i];break;}}} if(mapBtn){mapBtn.click();}"
* "4" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-062: Səhifə 2-yə keçid (Pagination)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var page2=document.querySelector('[data-testid=\"pagination-item-2\"],[aria-label=\"Page 2\"],[aria-label=\"2\"]');if(!page2){var allBtns=document.querySelectorAll('[data-testid*=\"pagination\"] button,[class*=\"pagination\"] button,[class*=\"Pagination\"] button,nav button');for(var i=0;i<allBtns.length;i++){if((allBtns[i].textContent||'').trim()==='2'){page2=allBtns[i];break;}}} if(!page2){var nextBtn=document.querySelector('[data-testid=\"pagination-next\"],[aria-label=\"Next page\"],[aria-label=\"Next\"],[rel=\"next\"]');page2=nextBtn;} if(page2){page2.click();}"
* "4" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-063: Nəticə kartına klik – detal səhifəsinə keçid
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var card=document.querySelector('[data-testid=\"title-link\"],[data-testid=\"property-card-title\"] a,[class*=\"sr-card\"] a[href*=\"hotel\"]');if(!card){card=document.querySelector('[data-testid=\"property-card\"] a,a[href*=\"booking.com/hotel\"]');} if(card){card.click();}else{throw new Error('Property card link not found');}"
* "5" saniye gözle
* JavaScript icra et "var isHotelPage=window.location.href.indexOf('/hotel/')>=0||document.querySelector('[data-testid=\"property-header\"],[data-testid=\"hotel-name\"],[class*=\"hp_hotel_name\"],[class*=\"hotelName\"]');if(!isHotelPage){throw new Error('Did not navigate to hotel detail page: '+window.location.href);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-064: IDOR – başqa istifadəçinin axtarış tarixi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/mysearchhistory.html?user_id=99999999"
* "4" saniye gözle
* JavaScript icra et "var url=window.location.href;var redirected=url.indexOf('signin')>=0||url.indexOf('login')>=0||url.indexOf('register')>=0||url.indexOf('myaccount')>=0;var currentPage=url.indexOf('mysearchhistory')>=0;if(currentPage){var pageContent=document.body.innerText.toLowerCase();var hasHistory=pageContent.indexOf('hotel')>=0&&pageContent.indexOf('london')>=0;if(hasHistory){throw new Error('IDOR: exposed search history of user 99999999');}} "
* URL "booking.com" içermelidir
* Brauzeri bağla
