$(document).ready(function(){
    $('#confirm_password').keyup(function(){
      var pwd = $('#password').val();
      var cpwd = $('#confirm_password').val();

      if(cpwd!=pwd){
        $('#showpwderror').html('**Password Does Not Match');
        $('#showpwderror').css('color','red');
        return false;
      } else{
        $('#showpwderror').html('');
        return true;
      }
    });
  });