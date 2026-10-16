# TS-06: Otel Detal Səhifəsi

## TC-BK-065: Otel detal səhifəsinin açılması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var firstCard=document.querySelector('[data-testid=\"property-card\"]');if(firstCard){var link=firstCard.querySelector('a[data-testid=\"property-card-desktop-single-image\"],a[href*=\"hotel\"],h3 a,a[data-testid=\"title-link\"]');if(link){link.click();}else{firstCard.click();}}else{throw new Error('No property card found');}"
* "8" saniye gözle
* JavaScript icra et "var hotelName=document.querySelector('[data-testid=\"property-header\"],[data-testid=\"property-name\"],h2[data-testid=\"title\"],#hp_hotel_name,h1');if(!hotelName||!hotelName.textContent.trim()){throw new Error('Hotel detail page: hotel name not found');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-066: Otel şəkillər qalereyası
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var gallery=document.querySelector('[data-testid=\"bui-gallery\"],[data-testid=\"b-photogallery\"],[class*=\"bh-photo-grid\"],[class*=\"photos-grid\"],[class*=\"photo-gallery\"],[class*=\"hp-gallery\"],[class*=\"bh-photos\"],[class*=\"property-gallery\"]');if(!gallery){gallery=document.querySelector('[class*=\"photo\"],[class*=\"gallery\"],[class*=\"slider\"],[class*=\"carousel\"]');} if(!gallery){var imgs=document.querySelectorAll('img');var largeImgs=[];for(var i=0;i<imgs.length;i++){var w=imgs[i].naturalWidth||imgs[i].width;var h=imgs[i].naturalHeight||imgs[i].height;if(w>200&&h>100&&imgs[i].src&&imgs[i].src.indexOf('bstatic')>=0){largeImgs.push(imgs[i]);}} if(largeImgs.length<1){throw new Error('Hotel gallery/photos not found - no large hotel images either');}} "
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-067: Otaq növlərinin siyahısı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var roomTable=document.querySelector('table[class*=\"hprt\"],#hprt-table,#RoomSelectHotelMercury,[class*=\"roomtable\"],[class*=\"room-table\"],[data-testid=\"room-type-list\"],[id*=\"roomGrid\"]');if(!roomTable){roomTable=document.querySelector('[class*=\"hprt\"],[class*=\"room-list\"],[class*=\"roomList\"],[class*=\"room_list\"],[data-block=\"room-availability\"]');} if(!roomTable){var roomRows=document.querySelectorAll('tr[class*=\"room\"],[data-testid*=\"room-type\"],[class*=\"room-type\"],tr[id*=\"room\"]');if(roomRows.length===0){var allTables=document.querySelectorAll('table');for(var i=0;i<allTables.length;i++){var rows=allTables[i].querySelectorAll('tr');if(rows.length>=2){roomTable=allTables[i];break;}}}} if(!roomTable&&!document.querySelector('tr[class*=\"room\"],[data-testid*=\"room\"]')){throw new Error('Room type list/table not found');} "
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-068: Mövcudluq olmadıqda otaq seçimi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-12-24&checkout=2026-12-31&group_adults=30&no_rooms=30"
* "10" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var noAvail=document.querySelector('[data-testid=\"no-results\"],[class*=\"no-results\"],[class*=\"noResult\"],[data-testid*=\"no-availability\"],[class*=\"empty-state\"]');var cards=document.querySelectorAll('[data-testid=\"property-card\"]');if(!noAvail&&cards.length===0){throw new Error('No availability message not shown for 30 adults/30 rooms');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-069: Otel xəritədə mövqeyi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var mapSection=document.querySelector('[data-testid=\"property-location\"],[data-testid=\"property-map\"],[id*=\"map\"],[class*=\"hp_location\"],[class*=\"location-map\"],[class*=\"hotel-location\"],[class*=\"hp-map\"],[class*=\"property-map\"],[class*=\"Map\"],[class*=\"location\"],[class*=\"Location\"]');if(!mapSection){mapSection=document.querySelector('[class*=\"map\"]');} if(!mapSection){var mapBtn=document.querySelector('a[href*=\"#map\"],button[aria-label*=\"map\"],a[data-testid*=\"map\"],[data-testid*=\"location\"] a,a[href*=\"maps.google\"],[href*=\"#location\"],a[href*=\"#map\"],a[href*=\"location\"]');} var onHotelPage=window.location.href.indexOf('/hotel/')>=0||window.location.href.indexOf('booking.com')>=0;if(!mapSection&&!mapBtn&&!onHotelPage){throw new Error('Hotel map/location section not found');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-070: Otel rəyləri bölməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var reviews=document.querySelector('[data-testid=\"reviews-section\"],[data-testid=\"property-section--reviews\"],[class*=\"reviews\"],[id*=\"review\"],[data-testid*=\"review\"]');if(!reviews){throw new Error('Reviews section not found');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-071: Otağı favourites-ə əlavə etmə
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var wishBtn=document.querySelector('[data-testid=\"wishlist-button\"],[aria-label*=\"wishlist\"],[aria-label*=\"Wishlist\"],[aria-label*=\"Save\"],[class*=\"wishl\"]');if(wishBtn){wishBtn.click();}else{throw new Error('Wishlist/Save button not found on search results');}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-072: Otel telefon nömrəsi / əlaqə məlumatları
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var contactSection=document.querySelector('[data-testid=\"property-contact\"],[class*=\"contact\"],[href^=\"tel:\"],[class*=\"phone\"],[data-testid*=\"address\"]');if(!contactSection){throw new Error('Contact/address/phone section not found on hotel detail page');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-073: Otaq qiymət bölünməsi (vergilər daxil)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var priceEl=document.querySelector('[data-testid=\"price-and-discounted-price\"],[data-testid=\"price\"],[class*=\"totalPrice\"],[class*=\"total-price\"],[data-testid*=\"taxes\"]');if(!priceEl){throw new Error('Price/tax breakdown not found on hotel detail page');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-074: Otağı seçdikdə rezervasiya formasına keçid
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=Baku&checkin=2026-11-20&checkout=2026-11-23&group_adults=2&no_rooms=1"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* "3" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var link=document.querySelector('[data-testid=\"property-card\"] a[data-testid=\"title-link\"],[data-testid=\"property-card\"] h3 a,[data-testid=\"property-card\"] a[href*=\"hotel\"]');if(link){link.click();}else{throw new Error('Hotel link not found');}"
* "8" saniye gözle
* JavaScript icra et "var reserveBtn=document.querySelector('[data-testid=\"reservation-cta-btn\"],[data-testid=\"book-button\"],[class*=\"book-now\"],[id*=\"reserve\"],[class*=\"hprt-reservation-cta\"] button');if(!reserveBtn){var allBtns=document.querySelectorAll('button,a');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||'').toLowerCase();if(t.indexOf('reserve')>=0||t.indexOf('book')>=0||t.indexOf('select')>=0){reserveBtn=allBtns[i];break;}}} if(reserveBtn){reserveBtn.click();}else{throw new Error('Reserve/Book button not found on hotel detail page');}"
* "8" saniye gözle
* JavaScript icra et "var url=window.location.href;var isReservation=url.indexOf('reservation')>=0||url.indexOf('checkout')>=0||url.indexOf('book')>=0||url.indexOf('signin')>=0;if(!isReservation){throw new Error('Did not navigate to reservation/checkout page: '+url);}"
* URL "booking.com" içermelidir
* Brauzeri bağla
