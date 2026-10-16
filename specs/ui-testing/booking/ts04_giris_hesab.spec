# TS-04: Giriş/Hesab

## TC-BK-036: Mövcud hesabla email ilə giriş
* "chrome" brauzeri aç ve keçid et "https://account.booking.com/sign-in/with-email"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* "Giris Formu" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "var emailInp=document.querySelector('[name=\"username\"],[name=\"email\"],[type=\"email\"],[data-testid=\"username-input\"],#username,#email,input[type=\"text\"]');if(emailInp){['mousedown','mouseup','click','focus'].forEach(function(t){emailInp.dispatchEvent(new MouseEvent(t,{bubbles:true,cancelable:true}));});var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(emailInp,'test@example.com');['input','change'].forEach(function(t){emailInp.dispatchEvent(new Event(t,{bubbles:true}));});}else{throw new Error('Email input not found');}"
* "1" saniye gözle
* JavaScript icra et "var continueBtn=document.querySelector('[data-testid=\"login-button\"],[type=\"submit\"],button[class*=\"submit\"]');if(!continueBtn){var allBtns=document.querySelectorAll('button');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||'').toLowerCase();if(t.indexOf('continue')>=0||t.indexOf('next')>=0||t.indexOf('sign in')>=0){continueBtn=allBtns[i];break;}}} if(continueBtn){continueBtn.click();}else{throw new Error('Continue button not found');}"
* "3" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-046: Google SSO ilə giriş
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/signin"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* JavaScript icra et "var googleBtn=document.querySelector('[data-testid=\"google-login-button\"],[aria-label*=\"Google\"],[class*=\"google\"],[href*=\"google\"]');if(!googleBtn){var allBtns=document.querySelectorAll('button,a');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||'').toLowerCase();if(t.indexOf('google')>=0){googleBtn=allBtns[i];break;}}} if(googleBtn){googleBtn.click();}else{throw new Error('Google SSO button not found');}"
* "5" saniye gözle
* JavaScript icra et "var url=window.location.href;var isGoogleOrBooking=url.indexOf('google')>=0||url.indexOf('accounts.google')>=0||url.indexOf('booking.com')>=0;if(!isGoogleOrBooking){throw new Error('Google SSO did not redirect: '+url);}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-047: Hesab yaratma – CAPTCHA davranışı
* "chrome" brauzeri aç ve keçid et "https://www.booking.com/register"
* "2" saniye gözle
* JavaScript icra et "var captcha=document.querySelector('[class*=\"captcha\"],[class*=\"CAPTCHA\"],[class*=\"recaptcha\"],[data-testid*=\"captcha\"],[id*=\"captcha\"]');var hasCaptcha=!!captcha;return hasCaptcha?'CAPTCHA_PRESENT':'CAPTCHA_NOT_VISIBLE';"
* "2" saniye gözle
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-048: SQL İnjektion – giriş forması
* "chrome" brauzeri aç ve keçid et "https://account.booking.com/sign-in/with-email"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* "Giris Formu" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "var emailInp=document.querySelector('[name=\"username\"],[name=\"email\"],[type=\"email\"],[data-testid=\"username-input\"],#username,#email,input[type=\"text\"]');if(emailInp){var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(emailInp,\"' OR '1'='1\");['input','change'].forEach(function(t){emailInp.dispatchEvent(new Event(t,{bubbles:true}));});}else{throw new Error('Email input not found');}"
* "1" saniye gözle
* JavaScript icra et "var continueBtn=document.querySelector('[data-testid=\"login-button\"],[type=\"submit\"],button[class*=\"submit\"]');if(!continueBtn){var allBtns=document.querySelectorAll('button');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||'').toLowerCase();if(t.indexOf('continue')>=0||t.indexOf('next')>=0){continueBtn=allBtns[i];break;}}} if(continueBtn){continueBtn.click();}"
* "4" saniye gözle
* JavaScript icra et "var url=window.location.href;var loggedIn=url.indexOf('/myaccount')>=0||url.indexOf('/dashboard')>=0||document.querySelector('[data-testid=\"user-menu\"]');if(loggedIn){throw new Error('SQL injection bypass successful - security vulnerability!');}"
* URL "booking.com" içermelidir
* Brauzeri bağla

## TC-BK-049: Email formatı validasiyası
* "chrome" brauzeri aç ve keçid et "https://account.booking.com/sign-in/with-email"
* "5" saniye gözle
* JavaScript icra et "document.querySelectorAll('[data-bui-trap-root] button,[data-testid=\"header-sign-in-prompt-close\"],[aria-label=\"Dismiss sign in information.\"],[data-testid=\"dismiss-button\"]').forEach(function(e){try{e.click();}catch(ex){}});"
* "1" saniye gözle
* "Giris Formu" görsensin deye maksimum "15" saniye gözle
* JavaScript icra et "var emailInp=document.querySelector('[name=\"username\"],[name=\"email\"],[type=\"email\"],[data-testid=\"username-input\"],#username,#email,input[type=\"text\"]');if(emailInp){var niv=Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype,'value').set;niv.call(emailInp,'notanemail');['input','change'].forEach(function(t){emailInp.dispatchEvent(new Event(t,{bubbles:true}));});}else{throw new Error('Email input not found');}"
* "1" saniye gözle
* JavaScript icra et "var continueBtn=document.querySelector('[data-testid=\"login-button\"],[type=\"submit\"],button[class*=\"submit\"]');if(!continueBtn){var allBtns=document.querySelectorAll('button');for(var i=0;i<allBtns.length;i++){var t=(allBtns[i].textContent||'').toLowerCase();if(t.indexOf('continue')>=0||t.indexOf('next')>=0){continueBtn=allBtns[i];break;}}} if(continueBtn){continueBtn.click();}"
* "3" saniye gözle
* JavaScript icra et "var errMsg=document.querySelector('[data-testid=\"error-message\"],[class*=\"error\"],[role=\"alert\"],[class*=\"invalid\"],[aria-invalid=\"true\"]');var emailInp=document.querySelector('[name=\"username\"],[name=\"email\"],[type=\"email\"],[data-testid=\"username-input\"]');var htmlValid=emailInp&&emailInp.validity&&!emailInp.validity.valid;if(!errMsg&&!htmlValid){throw new Error('Invalid email format not rejected');}"
* URL "booking.com" içermelidir
* Brauzeri bağla
