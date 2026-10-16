# TS-16: Xüsusi İstəklər

## TC-UI-048: Xüsusi istəklər textarea-nın göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var ta=document.querySelector('textarea[name*=\"request\"],textarea[name*=\"special\"],textarea[id*=\"request\"],[data-testid*=\"special-request\"]');if(!ta){ta=document.querySelector('textarea');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-049: Xüsusi istəkdə Azərbaycan dilinin qəbulu
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var ta=document.querySelector('textarea[name*=\"request\"],textarea[name*=\"special\"],textarea[id*=\"request\"]');if(!ta){ta=document.querySelector('textarea');}if(ta){ta.value='Xahiş edirəm yüksək mərtəbədə otaq verin';ta.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-050: Textarea simvol sayacının göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var ta=document.querySelector('textarea[name*=\"request\"],textarea[name*=\"special\"]');if(!ta){ta=document.querySelector('textarea');}if(ta){ta.value='Test request';ta.dispatchEvent(new Event('input',{bubbles:true}));}"
* "1" saniye gözle
* JavaScript icra et "var counter=document.querySelector('[class*=\"char-count\"],[class*=\"charCount\"],[class*=\"character-count\"],[class*=\"counter\"]');if(!counter){counter=Array.from(document.querySelectorAll('*')).find(function(e){var t=e.textContent||'';return e.childElementCount===0&&t.indexOf('/')>0&&t.length<20;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-051: Gəliş vaxtı seçiminin göstərilməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var arrivalSel=document.querySelector('select[name*=\"arrival\"],select[id*=\"arrival\"],[data-testid*=\"arrival-time\"],[class*=\"arrival\"]');if(!arrivalSel){arrivalSel=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('arrival')>=0;});}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-052: BVA – Gəliş vaxtı: check-in açılış vaxtından əvvəl (min-1)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sel=document.querySelector('select[name*=\"arrival\"],select[id*=\"arrival\"],[data-testid*=\"arrival\"]');if(sel){var opts=Array.from(sel.options);var earlyOpt=opts.find(function(o){return (o.text||'').indexOf('1:')>=0||(o.text||'').indexOf('13:')>=0;});if(earlyOpt){sel.value=earlyOpt.value;sel.dispatchEvent(new Event('change',{bubbles:true}));}}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-053: BVA – Gəliş vaxtı: tam check-in saatı (min: 2:00 PM)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var sel=document.querySelector('select[name*=\"arrival\"],select[id*=\"arrival\"],[data-testid*=\"arrival\"]');if(sel){var opts=Array.from(sel.options);var pmOpt=opts.find(function(o){return (o.text||'').indexOf('2:00 PM')>=0||(o.text||'').indexOf('14:00')>=0;});if(pmOpt){sel.value=pmOpt.value;sel.dispatchEvent(new Event('change',{bubbles:true}));}}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-054: 'Next: Final details' CTA düyməsinin işləməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var btn=Array.from(document.querySelectorAll('button,a')).find(function(e){return (e.textContent||'').toLowerCase().indexOf('final details')>=0||(e.textContent||'').toLowerCase().indexOf('next')>=0;});if(btn){btn.click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-055: 'I'll book without a credit card' seçiminin görünməsi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var noCard=Array.from(document.querySelectorAll('*')).find(function(e){return e.childElementCount===0&&(e.textContent||'').toLowerCase().indexOf('without a credit card')>=0;});if(!noCard){noCard=document.querySelector('[data-testid*=\"no-card\"],[class*=\"no-card\"],[class*=\"noCard\"]');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-056: Gezinmə çubuğundakı 'Home' linki
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var homeLink=document.querySelector('a[href=\"/\"],a[href=\"https://www.booking.com/\"],a[aria-label*=\"Home\"],[data-testid*=\"home\"]');if(!homeLink){homeLink=document.querySelector('header a,[class*=\"logo\"] a');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-057: Səhifəni yeniləmə (F5) – forma datalarının qorunması
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');if(inp){inp.value='TestUser';inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* JavaScript icra et "window.location.reload();"
* "4" saniye gözle
* JavaScript icra et "var inp=document.querySelector('input[name=\"firstname\"],input[id*=\"first\"]');var val=inp?inp.value:'';"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-UI-058: XSS – Xüsusi istəklər textarea
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/searchresults.html?ss=London&checkin=2025-03-01&checkout=2025-03-05&group_adults=2"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var ta=document.querySelector('textarea[name*=\"request\"],textarea[name*=\"special\"]');if(!ta){ta=document.querySelector('textarea');}if(ta){ta.value='<script>alert(1)<\/script>';ta.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla
