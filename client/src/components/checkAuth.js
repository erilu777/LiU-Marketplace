export function checkAuthStatus() {
    var authData = JSON.parse(sessionStorage.getItem('auth'));
    if (authData && authData.access_token) {
      return true;
    }else{
      return false;
    }
  }