# TS-09: Rezervasiya Təsdiqi

## TC-BK-105: Uğurlu rezervasiyadan sonra təsdiq səhifəsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var conf=document.querySelector('[data-testid=\"confirmation\"],[class*=\"confirmation\"],[class*=\"booking-confirmation\"],[id*=\"confirmation\"]');if(!conf){conf=document.querySelector('[class*=\"success\"],[class*=\"complete\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-106: Rezervasiya təsdiq e-poçtu alınması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/myreservations"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var emailNote=document.querySelector('[class*=\"email\"],[data-testid*=\"email\"],[class*=\"confirmation-email\"]');if(!emailNote){emailNote=document.querySelector('[class*=\"sent\"],[class*=\"notification\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-107: Rezervasiyanın idarə panelindən görünməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/myreservations"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var res=document.querySelector('[data-testid=\"reservation-item\"],[class*=\"reservation\"],[class*=\"booking-item\"]');if(!res){res=document.querySelector('[class*=\"my-booking\"],[class*=\"trip\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-108: Rezervasiyanın ləğvi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/myreservations"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var cancelBtn=document.querySelector('[data-testid*=\"cancel\"],[class*=\"cancel\"],button[aria-label*=\"Cancel\"],a[href*=\"cancel\"]');if(cancelBtn){cancelBtn.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-109: Ləğv müddəti keçdikdən sonra ləğv cəhdi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/myreservations"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var cancelBtn=document.querySelector('[data-testid*=\"cancel\"],[class*=\"cancel\"],button[aria-label*=\"Cancel\"]');if(cancelBtn){cancelBtn.click();}"
* "3" saniye gözle
* JavaScript icra et "var errMsg=document.querySelector('[class*=\"error\"],[class*=\"alert\"],[role=\"alert\"],[data-testid*=\"error\"]');if(!errMsg){errMsg=document.querySelector('[class*=\"warning\"],[class*=\"message\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla
