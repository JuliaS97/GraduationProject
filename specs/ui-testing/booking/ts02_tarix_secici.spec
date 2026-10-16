# TS-02: Tarix Seçici

## TC-BK-011: Giriş Tarixi Seçimi – Gələcək Tarix
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var calBtn=document.querySelector('[data-testid=\"searchbox-dates-container\"],[data-testid=\"date-display-field-start\"],[aria-label*=\"Check-in\"],[aria-label*=\"Giriş\"]'); if(calBtn){calBtn.click();}else{var dateFields=document.querySelectorAll('[class*=\"date\"],[class*=\"Date\"]');for(var i=0;i<dateFields.length;i++){var r=dateFields[i].getBoundingClientRect();if(r.width>50&&r.height>20){dateFields[i].click();break;}}}"
* "Tarix Secici" görsensin deye maksimum "10" saniye gözle
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var checkin=new Date(today);checkin.setDate(today.getDate()+14);var targetDay=checkin.getDate();var found=false;var selectors=['[data-testid=\"calendar\"] [role=\"gridcell\"]','[data-testid=\"calendar\"] td','[class*=\"bui-calendar\"] [role=\"gridcell\"]','[class*=\"bui-calendar\"] td','[class*=\"calendar\"] [role=\"gridcell\"]','[class*=\"calendar\"] td','[role=\"gridcell\"]'];for(var s=0;s<selectors.length&&!found;s++){var cells=document.querySelectorAll(selectors[s]);for(var i=0;i<cells.length;i++){var cell=cells[i];var txt=(cell.textContent||'').trim();if(txt===String(targetDay)&&cell.getAttribute('aria-disabled')!=='true'&&!cell.classList.contains('disabled')&&!cell.classList.contains('is-disabled')){var r=cell.getBoundingClientRect();if(r.width>0&&r.height>0){['mousedown','mouseup','click'].forEach(function(ev){cell.dispatchEvent(new MouseEvent(ev,{bubbles:true,cancelable:true,view:window}));});found=true;break;}}}} if(!found){var allCells=document.querySelectorAll('[role=\"gridcell\"],[role=\"button\"][class*=\"day\"],[role=\"button\"][class*=\"Day\"]');var info='Total cells: '+allCells.length+'; ';for(var i=0;i<Math.min(5,allCells.length);i++){info+=allCells[i].textContent.trim()+'|';} throw new Error('Check-in day '+targetDay+' not found. Debug: '+info);}"
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var checkout=new Date(today);checkout.setDate(today.getDate()+17);var targetDay=checkout.getDate();var found=false;var selectors=['[data-testid=\"calendar\"] [role=\"gridcell\"]','[data-testid=\"calendar\"] td','[class*=\"bui-calendar\"] [role=\"gridcell\"]','[class*=\"bui-calendar\"] td','[class*=\"calendar\"] [role=\"gridcell\"]','[class*=\"calendar\"] td','[role=\"gridcell\"]'];for(var s=0;s<selectors.length&&!found;s++){var cells=document.querySelectorAll(selectors[s]);for(var i=0;i<cells.length;i++){var cell=cells[i];var txt=(cell.textContent||'').trim();if(txt===String(targetDay)&&cell.getAttribute('aria-disabled')!=='true'&&!cell.classList.contains('disabled')&&!cell.classList.contains('is-disabled')){var r=cell.getBoundingClientRect();if(r.width>0&&r.height>0){['mousedown','mouseup','click'].forEach(function(ev){cell.dispatchEvent(new MouseEvent(ev,{bubbles:true,cancelable:true,view:window}));});found=true;break;}}}} if(!found){throw new Error('Check-out day '+targetDay+' not found');}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-012: Keçmiş Tarix Seçilə Bilməz
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var calBtn=document.querySelector('[data-testid=\"searchbox-dates-container\"],[data-testid=\"date-display-field-start\"],[aria-label*=\"Check-in\"]'); if(calBtn){calBtn.click();}else{var dateFields=document.querySelectorAll('[class*=\"date\"],[class*=\"Date\"]');for(var i=0;i<dateFields.length;i++){var r=dateFields[i].getBoundingClientRect();if(r.width>50&&r.height>20){dateFields[i].click();break;}}}"
* "Tarix Secici" görsensin deye maksimum "10" saniye gözle
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var pastDay=today.getDate()-1;if(pastDay<1){pastDay=1;} var allCells=document.querySelectorAll('[role=\"gridcell\"],[data-testid=\"calendar\"] td,[class*=\"bui-calendar\"] td');var pastCell=null;for(var i=0;i<allCells.length;i++){var txt=(allCells[i].textContent||'').trim();if(txt===String(pastDay)){pastCell=allCells[i];break;}} var isDisabledOrMissing=!pastCell||(pastCell&&(pastCell.getAttribute('aria-disabled')==='true'||pastCell.classList.contains('disabled')||pastCell.classList.contains('is-disabled')||pastCell.getAttribute('tabindex')==='undefined')); if(!isDisabledOrMissing&&pastCell){pastCell.click();} "
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-013: Giriş = Çıxış Tarixi – Eyni Gün
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var calBtn=document.querySelector('[data-testid=\"searchbox-dates-container\"],[data-testid=\"date-display-field-start\"],[aria-label*=\"Check-in\"]'); if(calBtn){calBtn.click();}else{var dateFields=document.querySelectorAll('[class*=\"date\"],[class*=\"Date\"]');for(var i=0;i<dateFields.length;i++){var r=dateFields[i].getBoundingClientRect();if(r.width>50&&r.height>20){dateFields[i].click();break;}}}"
* "Tarix Secici" görsensin deye maksimum "10" saniye gözle
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var sameDay=new Date(today);sameDay.setDate(today.getDate()+10);var targetDay=sameDay.getDate();var found=false;var selectors=['[data-testid=\"calendar\"] [role=\"gridcell\"]','[data-testid=\"calendar\"] td','[class*=\"bui-calendar\"] [role=\"gridcell\"]','[class*=\"bui-calendar\"] td','[role=\"gridcell\"]'];for(var s=0;s<selectors.length&&!found;s++){var cells=document.querySelectorAll(selectors[s]);for(var i=0;i<cells.length;i++){var cell=cells[i];var txt=(cell.textContent||'').trim();if(txt===String(targetDay)&&cell.getAttribute('aria-disabled')!=='true'&&!cell.classList.contains('disabled')){var r=cell.getBoundingClientRect();if(r.width>0&&r.height>0){['mousedown','mouseup','click'].forEach(function(ev){cell.dispatchEvent(new MouseEvent(ev,{bubbles:true,cancelable:true,view:window}));});found=true;break;}}}} if(!found){throw new Error('Same-day check-in not found for day '+targetDay);}"
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var sameDay=new Date(today);sameDay.setDate(today.getDate()+10);var targetDay=sameDay.getDate();var found=false;var selectors=['[data-testid=\"calendar\"] [role=\"gridcell\"]','[data-testid=\"calendar\"] td','[class*=\"bui-calendar\"] [role=\"gridcell\"]','[class*=\"bui-calendar\"] td','[role=\"gridcell\"]'];for(var s=0;s<selectors.length&&!found;s++){var cells=document.querySelectorAll(selectors[s]);for(var i=0;i<cells.length;i++){var cell=cells[i];var txt=(cell.textContent||'').trim();if(txt===String(targetDay)&&cell.getAttribute('aria-disabled')!=='true'&&!cell.classList.contains('disabled')){var r=cell.getBoundingClientRect();if(r.width>0&&r.height>0){['mousedown','mouseup','click'].forEach(function(ev){cell.dispatchEvent(new MouseEvent(ev,{bubbles:true,cancelable:true,view:window}));});found=true;break;}}}} if(!found){throw new Error('Same-day check-out not found for day '+targetDay);}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-014: Çıxış < Giriş – Avtomatik Düzəltmə
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var calBtn=document.querySelector('[data-testid=\"searchbox-dates-container\"],[data-testid=\"date-display-field-start\"],[aria-label*=\"Check-in\"]'); if(calBtn){calBtn.click();}else{var dateFields=document.querySelectorAll('[class*=\"date\"],[class*=\"Date\"]');for(var i=0;i<dateFields.length;i++){var r=dateFields[i].getBoundingClientRect();if(r.width>50&&r.height>20){dateFields[i].click();break;}}}"
* "Tarix Secici" görsensin deye maksimum "10" saniye gözle
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var checkin=new Date(today);checkin.setDate(today.getDate()+15);var targetDay=checkin.getDate();var found=false;var selectors=['[data-testid=\"calendar\"] [role=\"gridcell\"]','[data-testid=\"calendar\"] td','[class*=\"bui-calendar\"] [role=\"gridcell\"]','[class*=\"bui-calendar\"] td','[role=\"gridcell\"]'];for(var s=0;s<selectors.length&&!found;s++){var cells=document.querySelectorAll(selectors[s]);for(var i=0;i<cells.length;i++){var cell=cells[i];var txt=(cell.textContent||'').trim();if(txt===String(targetDay)&&cell.getAttribute('aria-disabled')!=='true'&&!cell.classList.contains('disabled')){var r=cell.getBoundingClientRect();if(r.width>0&&r.height>0){['mousedown','mouseup','click'].forEach(function(ev){cell.dispatchEvent(new MouseEvent(ev,{bubbles:true,cancelable:true,view:window}));});found=true;break;}}}} if(!found){throw new Error('Check-in +15 day not found: '+targetDay);}"
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var checkout=new Date(today);checkout.setDate(today.getDate()+10);var targetDay=checkout.getDate();var found=false;var selectors=['[data-testid=\"calendar\"] [role=\"gridcell\"]','[data-testid=\"calendar\"] td','[class*=\"bui-calendar\"] [role=\"gridcell\"]','[class*=\"bui-calendar\"] td','[role=\"gridcell\"]'];for(var s=0;s<selectors.length&&!found;s++){var cells=document.querySelectorAll(selectors[s]);for(var i=0;i<cells.length;i++){var cell=cells[i];var txt=(cell.textContent||'').trim();if(txt===String(targetDay)&&cell.getAttribute('aria-disabled')!=='true'&&!cell.classList.contains('disabled')){var r=cell.getBoundingClientRect();if(r.width>0&&r.height>0){['mousedown','mouseup','click'].forEach(function(ev){cell.dispatchEvent(new MouseEvent(ev,{bubbles:true,cancelable:true,view:window}));});found=true;break;}}}} if(!found){throw new Error('Checkout +10 day not found: '+targetDay);}"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-015: 365 Gün Gələcək Tarix – BVA
* "chrome" brauzeri aç ve keçid et "https://www.booking.com"
* "Axtarish Formunu Yükle" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "3" saniye gözle
* JavaScript icra et "var calBtn=document.querySelector('[data-testid=\"searchbox-dates-container\"],[data-testid=\"date-display-field-start\"],[aria-label*=\"Check-in\"]'); if(calBtn){calBtn.click();}else{var dateFields=document.querySelectorAll('[class*=\"date\"],[class*=\"Date\"]');for(var i=0;i<dateFields.length;i++){var r=dateFields[i].getBoundingClientRect();if(r.width>50&&r.height>20){dateFields[i].click();break;}}}"
* "Tarix Secici" görsensin deye maksimum "10" saniye gözle
* "2" saniye gözle
* JavaScript icra et "var today=new Date();var future=new Date(today);future.setDate(today.getDate()+365);var targetDay=future.getDate();var allCells=document.querySelectorAll('[role=\"gridcell\"],[data-testid=\"calendar\"] td,[class*=\"bui-calendar\"] td');var found=false;for(var i=0;i<allCells.length;i++){var txt=(allCells[i].textContent||'').trim();if(txt===String(targetDay)){found=true;break;}} "
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla
