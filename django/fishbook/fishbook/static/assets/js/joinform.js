
$(function(){
  /*이메일 중복 or 탈퇴 확인*/

  /*이메일 형식 확인 */
  $("#email").keyup(function(){

    var email = $('#email').val()

      $.ajax({
        url:'/users/api/checkemail?email='+email,
        type:'get',
        dataType:'json',
        success:function(response){
          if(response.result != 'success'){
            console.error(response.data)
            return;
          }
          if(response.data == 'exist'){
              $("#email_msg").text("이미 사용중인 이메일입니다.")
              .attr("style", "color: red; font-size:15px;");
              $("#btn_join").attr("email_check_result", "fail");
            $('#email').val('').focus();
            return;
          } else{
            if (validateEmail($.trim($("#email").val()))){
                $("#email_msg").text("사용 가능한 이메일 입니다.")
                .attr("style", "color: green; font-size:15px")
                $("#btn_join").attr("email_check_result", "success");

            } else {
                $("#email_msg").text("이메일 형식이 틀렸습니다.")
                .attr("style", "color: red; font-size:15px;");
                $("#btn_join").attr("email_check_result", "fail");
            }
            return;
            }
          // console.log(response)
        },
        error : function(xhr, error){
          alert("서버와의 통신에서 문제가 발생했습니다.");
          console.error("error : " + error);
        }
      })
  });

  /*id 형식 확인 */
//   $("#id").keyup(function(){
//     if(validateId($.trim($("#id").val()))){
//         $("#id_msg").text("사용 가능한 아이디입니다.")
//         .attr("style", "color: green; font-size:15px");
//     } else{
//         $("#id_msg").text("5자리 이상 입력")
//         .attr("style", "color: red; font-size:15px");
//     }
// });
  /* 비밀번호 형식 확인 */
  // 비밀번호 규칙 정규식
// : 숫자, 특문 각 1회 이상, 영문은 2개 이상 사용하여 8자리 이상 입력
  $("#pw").keyup(function(){
    if(validatePassword($.trim($("#pw").val()))){
        $("#pw_msg").text("사용 가능한 비밀번호입니다.")
        .attr("style", "color: green; font-size:15px");
        $("#btn_join").attr("pw_check_result", "success");
    } else{
        $("#pw_msg").text("숫자, 특수문자 각 1회 이상, 영문은 2개 이상 사용하여 8자리 이상 입력")
        .attr("style", "color: red; font-size:15px");
        $("#btn_join").attr("pw_check_result", "fail");
    }
});



  /*비밀번호 재확인*/
  $("#pw_check, #pw").keyup(function(){
      if($("#pw").val()==$('#pw_check').val()){
          $("#pw_check_msg").text("비밀번호가 일치합니다.")
          .attr("style", "color: green; font-size:15px");

          $("#btn_join").attr("pw_check_check_result", "success");
      } else{
          $("#pw_check_msg").text("비밀번호가 일치하지 않습니다.")
          .attr("style", "color: red; font-size:15px");
          $("#btn_join").attr("pw_check_check_result", "fail");

      }
  });

  $('#join_f').submit(function() {
    if($("#btn_join").attr("email_check_result") == "fail") {

      $("#email_msg").text("사용 가능한 이메일을 입력해주세요.")
      .attr("style", "color: red; font-size:15px;");
       $("#email").focus();
       return false;
    }
     if($("#btn_join").attr("pw_check_result") == "fail") {

        $("#pw_msg").text("비밀번호를 확인해주세요.")
        .attr("style", "color: red; font-size:15px");
       $("#pw").focus();
       return false;
    }

     if($("#btn_join").attr("pw_check_check_result") == "fail") {

        $("#pw_check_msg").text("비밀번호를 확인해주세요.")
        .attr("style", "color: red; font-size:15px");
       $("#pw_check").focus();
       return false;
    }
  });

  /*Ajax */
  var $form = $("#join_f");

  //
  // $form.on("submit", function(e){
  //   e.preventDefault();
  //   var newUser = $form.serialize();
  //
  //   $.ajax({
  //     type:"POST",
  //     url: "js/user.json",
  //     data:newUser,
  //     success:function(res){
  //       if (validateEmail($.trim($("#email").val()))){
  //         $(".input_row #email")
  //         .attr("style", "border: 1px solid green;")
  //       } else {
  //         $(".input_row #email")
  //         .attr("style", "border: 1px solid red;")
  //         .focus();
  //       }
  //     },
  //     error:function(){
  //       if (validateEmail($.trim($("#email").val()))){
  //         $(".input_row #email")
  //         .attr("style", "border: 1px solid green;")
  //       } else {
  //         $(".input_row #email")
  //         .attr("style", "border: 1px solid red;")
  //         .focus();
  //       }
  //     }
  //   });
  // });


  /* 정규표현식을 이용하여 email형식에 맞는지 확인하는 함수*/
  function validateEmail(email) {
      var re = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;
      return re.test(email);
  }
  /* 정규표현식을 이용하여 id형식에 맞는지 확인하는 함수*/
  function validateId(id) {
    var re = /[a-zA-Z0-9]{5,}/i;
    return re.test(id);
}
  /* 정규표현식을 이용하여 password형식에 맞는지 확인하는 함수*/
  // : 숫자, 특문 각 1회 이상, 영문은 2개 이상 사용하여 8자리 이상 입력
  function validatePassword(pw) {
    var re = /(?=.*\d{1,50})(?=.*[~`!@#$%\^&*()-+=]{1,50})(?=.*[a-zA-Z]{2,50}).{8,50}$/;
    return re.test(pw);
}
});
