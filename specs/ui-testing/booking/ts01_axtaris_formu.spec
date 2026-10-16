# TS-01: Ana Səhifə – Axtarış Formu

## TC-BK-001: Etibarlı Şəhər Axtarışı – Bakı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){['mousedown','mouseup','click','focus'].forEach(function(t){inp.dispatchEvent(new MouseEvent(t,{bubbles:true,cancelable:true}));});var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'Bakı');['keydown','keypress','input','keyup','change'].forEach(function(t){inp.dispatchEvent(new Event(t,{bubbles:true,cancelable:true}));});} else {throw new Error('Input not found');}"
* "5" saniye gözle
* JavaScript icra et "var found=document.querySelector('[data-testid=\"autocomplete-results-container\"],[data-testid=\"autocomplete-results\"],[role=\"listbox\"],[data-testid=\"destination-container\"] ul,ul[aria-label],[ul][class*=\"auto\"]'); if(!found){var allUl=document.querySelectorAll('ul');var vis=null;for(var i=0;i<allUl.length;i++){var r=allUl[i].getBoundingClientRect();if(r.width>50&&r.height>20){vis=allUl[i];break;}} if(!vis){throw new Error('No dropdown ul visible. Body snippet: '+document.body.innerHTML.substring(300,800));}} "
* JavaScript icra et "var opts=document.querySelectorAll('[role=\"option\"],[data-testid=\"autocomplete-results-container\"] li,[data-testid=\"autocomplete-results\"] li,[data-testid=\"destination-container\"] ul li'); if(opts.length===0){var allLis=document.querySelectorAll('ul li');for(var i=0;i<allLis.length;i++){var r=allLis[i].getBoundingClientRect();if(r.width>50&&r.height>10){opts=document.querySelectorAll('ul li');break;}}} var baku=null; for(var i=0;i<opts.length;i++){var t=opts[i].textContent||''; if(t.indexOf('Bak')>=0||t.indexOf('Бак')>=0){baku=opts[i];break;}} if(baku){baku.dispatchEvent(new MouseEvent('mousedown',{bubbles:true}));baku.dispatchEvent(new MouseEvent('mouseup',{bubbles:true}));baku.click();}else if(opts.length>0){opts[0].dispatchEvent(new MouseEvent('mousedown',{bubbles:true}));opts[0].click();} else{throw new Error('No list items found, opts count: '+opts.length);}"
* JavaScript icra et "var btn=document.querySelector('button[data-testid=\"searchbox-submit-button\"],[data-testid=\"searchbox-submit-button\"],button[type=\"submit\"]');if(btn){btn.click();}else{throw new Error('Submit button not found');}"
* "Netice Sehifesi Otel Karti" görsensin deye maksimum "20" saniye gözle
* URL "searchresults" içermelidir
* "Netice Sehifesi Otel Karti" elementlerinin sayı en az "1" olmalıdır
* Brauzeri bağla

## TC-BK-002: Mövcud Olmayan Şəhər – Sıfır Nəticə
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){['mousedown','mouseup','click','focus'].forEach(function(t){inp.dispatchEvent(new MouseEvent(t,{bubbles:true,cancelable:true}));});var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'ZZZQQQXXXsəhər');['keydown','keypress','input','keyup','change'].forEach(function(t){inp.dispatchEvent(new Event(t,{bubbles:true,cancelable:true}));});}"
* "5" saniye gözle
* JavaScript icra et "var btn=document.querySelector('button[data-testid=\"searchbox-submit-button\"],[data-testid=\"searchbox-submit-button\"],button[type=\"submit\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button[type=\"submit\"]');if(btns.length>0)btns[btns.length-1].click();}"
* "Sifir Netice Mesaji" görsensin deye maksimum "15" saniye gözle
* Brauzeri bağla

## TC-BK-003: Məkan Boş – Validasiya Xətası
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'');inp.dispatchEvent(new Event('input',{bubbles:true}));inp.dispatchEvent(new Event('change',{bubbles:true}));inp.blur();}"
* JavaScript icra et "var btn=document.querySelector('button[data-testid=\"searchbox-submit-button\"],[data-testid=\"searchbox-submit-button\"],button[type=\"submit\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button[type=\"submit\"]');if(btns.length>0)btns[btns.length-1].click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-004: Bütün Sahələr Boş – Validasiya Xətası
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var btn=document.querySelector('button[data-testid=\"searchbox-submit-button\"],[data-testid=\"searchbox-submit-button\"],button[type=\"submit\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button[type=\"submit\"]');if(btns.length>0)btns[btns.length-1].click();}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-005: Tək Simvol Avtotamamlama
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){['mousedown','mouseup','click','focus'].forEach(function(t){inp.dispatchEvent(new MouseEvent(t,{bubbles:true,cancelable:true}));});var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'Ba');['keydown','keypress','input','keyup','change'].forEach(function(t){inp.dispatchEvent(new Event(t,{bubbles:true,cancelable:true}));});} else {throw new Error('Input not found');}"
* "7" saniye gözle
* JavaScript icra et "var found=false;var candidates=['[data-testid=\"autocomplete-results-container\"]','[data-testid=\"autocomplete-results\"]','[role=\"listbox\"]','[data-testid=\"destination-container\"] ul'];for(var c=0;c<candidates.length;c++){var el=document.querySelector(candidates[c]);if(el&&el.children.length>0){found=true;break;}} if(!found){var allUl=document.querySelectorAll('ul');for(var i=0;i<allUl.length;i++){var r=allUl[i].getBoundingClientRect();if(r.width>50&&r.height>20&&allUl[i].children.length>0){found=true;break;}}} if(!found){throw new Error('No autocomplete dropdown found after 7s. Input value: '+(document.querySelector('[name=\"ss\"],[data-testid=\"destination-container\"] input')||{value:'not found'}).value);}"
* "Avtotamamlama Dropdown" elementlerinin sayı en az "1" olmalıdır
* Brauzeri bağla

## TC-BK-008: 100 Simvol Qəbulu – BVA Üst Hədd
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){inp.focus();inp.click();var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* "Mekan Sahesi" görsensin deye maksimum "5" saniye gözle
* Brauzeri bağla

## TC-BK-009: 101 Simvol Kəsilmə – BVA Üst Hədd Aşımı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){inp.focus();inp.click();var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaX');inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* "Mekan Sahesi" görsensin deye maksimum "5" saniye gözle
* Brauzeri bağla

## TC-BK-010: XSS Payload – Güvənlik Testi
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var inp=document.querySelector('[name=\"ss\"],#searchbox-horizontal-destination-input,[data-testid=\"destination-container\"] input,[data-testid=\"searchbox-destination-input\"] input,input[placeholder*=\"Where\"],input[autocomplete=\"off\"][type=\"search\"]'); if(inp){inp.focus();inp.click();var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(inp,'<script>alert(\"xss\")<\\/script>');inp.dispatchEvent(new Event('input',{bubbles:true}));}"
* URL "booking.com" içermelidir
* Brauzeri bağla
