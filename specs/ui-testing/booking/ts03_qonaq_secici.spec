# TS-03: Qonaq Seçici

## TC-BK-023: BVA – Böyük sayı (min: 1 böyük)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0||t.indexOf('qonaq')>=0||t.indexOf('Qonaq')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var minusBtn=null;if(rows.length>0){var btnsInRow=rows[0].querySelectorAll('button');if(btnsInRow.length>=1)minusBtn=btnsInRow[0];} if(!minusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=2)minusBtn=allBtns[0];} if(minusBtn){minusBtn.click();}else{throw new Error('Adult decrease button not found in popup');}"
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var valEl=null;if(rows.length>0){valEl=rows[0].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl){var allInputs=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allInputs.length>0)valEl=allInputs[0];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'1';if(val!=='1'&&val!==''){var n=parseInt(val);if(!isNaN(n)&&n<1){throw new Error('Expected at least 1 adult, got: '+val);}}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-025: BVA – Böyük sayı (max-1: 29 böyük)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;if(rows.length>0){var btnsInRow=rows[0].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=2)plusBtn=allBtns[1];} if(!plusBtn){throw new Error('Adult increase button not found');} for(var i=0;i<27;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;if(rows.length>0){valEl=rows[0].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>0)valEl=allVals[0];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'29';var n=parseInt(val);if(!isNaN(n)&&n!==29){throw new Error('Expected 29 adults, got: '+val);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-026: BVA – Böyük sayı (max: 30 böyük)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;if(rows.length>0){var btnsInRow=rows[0].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=2)plusBtn=allBtns[1];} if(!plusBtn){throw new Error('Adult increase button not found');} for(var i=0;i<28;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;if(rows.length>0){valEl=rows[0].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>0)valEl=allVals[0];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'30';var n=parseInt(val);if(!isNaN(n)&&n!==30){throw new Error('Expected 30 adults, got: '+val);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-027: BVA – Böyük sayı (max+1: 31 böyük icazəsiz)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;if(rows.length>0){var btnsInRow=rows[0].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=2)plusBtn=allBtns[1];} if(!plusBtn){throw new Error('Adult increase button not found');} for(var i=0;i<30;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;if(rows.length>0){valEl=rows[0].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>0)valEl=allVals[0];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'30';var n=parseInt(val);if(!isNaN(n)&&n===31){throw new Error('31 adults was accepted - should be blocked');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-028: BVA – Uşaq sayı (min-1: -1 uşaq icazəsiz)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var minusBtn=null;if(rows.length>1){var btnsInRow=rows[1].querySelectorAll('button');if(btnsInRow.length>=1)minusBtn=btnsInRow[0];} if(!minusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=3)minusBtn=allBtns[2];} if(minusBtn){minusBtn.click();}else{throw new Error('Children decrease button not found');}"
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;if(rows.length>1){valEl=rows[1].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>1)valEl=allVals[1];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'0';var n=parseInt(val);if(!isNaN(n)&&n<0){throw new Error('Children count went below 0: '+val);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-030: BVA – Uşaq sayı (max: 10 uşaq)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;if(rows.length>1){var btnsInRow=rows[1].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=4)plusBtn=allBtns[3];} if(!plusBtn){throw new Error('Children increase button not found');} for(var i=0;i<10;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;if(rows.length>1){valEl=rows[1].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>1)valEl=allVals[1];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'10';var n=parseInt(val);if(!isNaN(n)&&n!==10){throw new Error('Expected 10 children, got: '+val);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-031: BVA – Uşaq sayı (max+1: 11 uşaq icazəsiz)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;if(rows.length>1){var btnsInRow=rows[1].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=4)plusBtn=allBtns[3];} if(!plusBtn){throw new Error('Children increase button not found');} for(var i=0;i<11;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;if(rows.length>1){valEl=rows[1].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>1)valEl=allVals[1];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'10';var n=parseInt(val);if(!isNaN(n)&&n===11){throw new Error('11 children was accepted - should be blocked at 10');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-032: BVA – Otaq sayı (min: 1 otaq)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var valEl=null;var rowIdx=rows.length>2?2:rows.length-1;if(rowIdx>=0&&rows.length>0){valEl=rows[rowIdx].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>2)valEl=allVals[2];else if(allVals.length>0)valEl=allVals[allVals.length-1];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'1';var n=parseInt(val);if(!isNaN(n)&&n!==1){throw new Error('Expected 1 room by default, got: '+val);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-033: BVA – Otaq sayı (max: 30 otaq)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;var rowIdx=rows.length>2?2:rows.length-1;if(rowIdx>=0&&rows.length>0){var btnsInRow=rows[rowIdx].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=6)plusBtn=allBtns[5];else if(allBtns.length>0)plusBtn=allBtns[allBtns.length-1];} if(!plusBtn){throw new Error('Rooms increase button not found');} for(var i=0;i<29;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;var rowIdx=rows.length>2?2:rows.length-1;if(rowIdx>=0&&rows.length>0){valEl=rows[rowIdx].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>2)valEl=allVals[2];else if(allVals.length>0)valEl=allVals[allVals.length-1];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'30';var n=parseInt(val);if(!isNaN(n)&&n!==30){throw new Error('Expected 30 rooms, got: '+val);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-034: BVA – Otaq sayı (max+1: 31 otaq icazəsiz)
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "2" saniye gözle
* JavaScript icra et "var btn=document.querySelector('[data-testid=\"occupancy-config\"],[data-testid=\"searchbox-people-options-button\"],[class*=\"xp__guests\"]');if(btn){btn.click();}else{var btns=document.querySelectorAll('button');for(var i=0;i<btns.length;i++){var t=btns[i].textContent||'';if(t.indexOf('adult')>=0||t.indexOf('Adult')>=0){btns[i].click();break;}}}"
* "Qonaq Secici" görsensin deye maksimum "10" saniye gözle
* "1" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');if(!popup){throw new Error('Popup not found');} var rows=popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]');var plusBtn=null;var rowIdx=rows.length>2?2:rows.length-1;if(rowIdx>=0&&rows.length>0){var btnsInRow=rows[rowIdx].querySelectorAll('button');if(btnsInRow.length>=2)plusBtn=btnsInRow[btnsInRow.length-1];} if(!plusBtn){var allBtns=popup.querySelectorAll('button');if(allBtns.length>=6)plusBtn=allBtns[5];else if(allBtns.length>0)plusBtn=allBtns[allBtns.length-1];} if(!plusBtn){throw new Error('Rooms increase button not found');} for(var i=0;i<30;i++){plusBtn.click();}"
* "2" saniye gözle
* JavaScript icra et "var popup=document.querySelector('[data-testid=\"occupancy-popup\"],[data-testid=\"searchbox-people-options-popup\"],[class*=\"xp__guests__popup\"],[class*=\"bui-popover__inner\"]');var rows=popup?popup.querySelectorAll('[class*=\"stepper\"],[class*=\"bui-stepper\"],[class*=\"group_\"],[data-testid*=\"stepper\"],[class*=\"xp__guests__count\"]'):[];var valEl=null;var rowIdx=rows.length>2?2:rows.length-1;if(rowIdx>=0&&rows.length>0){valEl=rows[rowIdx].querySelector('[class*=\"display\"],[class*=\"count\"],[class*=\"value\"],[data-testid*=\"value\"]');} if(!valEl&&popup){var allVals=popup.querySelectorAll('input[type=\"number\"],[class*=\"display\"],[class*=\"value\"]');if(allVals.length>2)valEl=allVals[2];else if(allVals.length>0)valEl=allVals[allVals.length-1];} var val=valEl?(valEl.value||valEl.textContent||'').trim():'30';var n=parseInt(val);if(!isNaN(n)&&n===31){throw new Error('31 rooms was accepted - should be blocked at 30');}"
* URL "booking.com" içermelidir
* Brauzeri bağla
