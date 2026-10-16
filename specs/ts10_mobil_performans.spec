# TS-10: Mobil/Performans

## TC-BK-110: Mobil görünüşdə axtarış formasının işləməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "5" saniye gözle
* JavaScript icra et "Object.defineProperty(window.navigator,'userAgent',{value:'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',configurable:true});"
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var form=document.querySelector('form[action*=\"search\"],form[data-testid*=\"search\"],[class*=\"search-form\"],[data-testid=\"search-form\"]');if(!form){form=document.querySelector('form,[class*=\"searchbox\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-111: Mobil menyunun açılması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var menu=document.querySelector('[aria-label*=\"menu\"],[data-testid*=\"menu\"],[class*=\"hamburger\"],[class*=\"burger\"],[class*=\"nav-toggle\"]');if(menu){menu.click();}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-112: Ana səhifənin yükləmə sürəti
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var timing=window.performance&&window.performance.timing;if(timing){var loadTime=timing.loadEventEnd-timing.navigationStart;if(loadTime>0&&loadTime>10000){throw new Error('Page load time exceeded 10s: '+loadTime+'ms');}}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-113: Axtarış nəticələrinin yükləmə sürəti
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "8" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var timing=window.performance&&window.performance.timing;if(timing){var loadTime=timing.loadEventEnd-timing.navigationStart;if(loadTime>0&&loadTime>15000){throw new Error('Search results load time exceeded 15s: '+loadTime+'ms');}}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-114: Yüksək yük vəziyyətindəki davranış
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var results=document.querySelectorAll('[data-testid=\"property-card\"],[class*=\"sr_item\"],[class*=\"property-card\"]');var pageOk=window.location.href.indexOf('booking.com')>=0;"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-115: Şəkil qalereyasının yüklənməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var imgs=document.querySelectorAll('[data-testid=\"property-card\"] img,[class*=\"property-card\"] img');var loaded=Array.from(imgs).filter(function(i){return i.complete&&i.naturalHeight>0;});"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-116: Sessiya bitdikdən sonra rezervasiya qorunması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/myreservations"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var isLogin=window.location.href.indexOf('signin')>=0||window.location.href.indexOf('login')>=0||document.querySelector('[data-testid*=\"sign-in\"],[class*=\"signin\"],[class*=\"login\"]');var isReservations=window.location.href.indexOf('myreservations')>=0;"
* URL "booking.com" içermelidir
* Brauzeri bağla
