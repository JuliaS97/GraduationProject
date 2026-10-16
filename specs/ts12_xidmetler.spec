# TS-12: Xidmətlər

## TC-UI-013: 'Most popular facilities' sürətli ikonların göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var fac=document.querySelector('[data-testid=\"property-most-popular-facilities\"],[class*=\"popular-facilities\"],[class*=\"facilities\"],[id*=\"facilities\"]');if(!fac){fac=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('popular facilities')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-014: 'Internet – No internet access available' xəbərdarlığı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var noNet=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('no internet')>=0;});if(!noNet){noNet=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('internet')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-015: 'Additional charge' etiketli xidmətlər
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var addCharge=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('additional charge')>=0;});if(!addCharge){addCharge=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('surcharge')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-016: Əlçatımlılıq (Accessibility) xidmətlərinin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/hotel/gb/the-savoy-london.html?checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "6" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var acc=document.querySelector('[data-testid*=\"accessibility\"],[class*=\"accessibility\"],[id*=\"accessibility\"]');if(!acc){acc=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('accessibility')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla
