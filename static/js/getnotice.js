
// var request1 = new XMLHttpRequest();

// request1.onreadystatechange = function(response) {
//   if (request1.readyState === 4) {
//     if (request1.status === 200) {

//       var NoticeJsonList = JSON.parse(request1.responseText);
//       for(x in NoticeJsonList['notice'])
//       {

//          document.getElementById("notice_marquee").innerHTML+= '<div class=row><div class="col-sm-12" >'+'<a style="color:#252627" href="'+NoticeJsonList['notice'][x].url+'">'+NoticeJsonList['notice'][x].title+'</a></div></div></br>';
//       }
//     }
//   }}

// request1.open('GET', '/notice_get', true);
// request1.send();

$.ajax({
  url: '/notice_get',
  success: function(data){
    if(data.success == true){
      for(x in data.notice)
      {
         document.getElementById("notice_marquee").innerHTML+= '<div class=row><div class="col-sm-12" >'+'<a href="'+data.notice[x].url+'">'+data.notice[x].title+'</a></div></div></br>';
      }
    }else{
      alert('Sorry an errro occured while loading notice');
    }
  },
  error: function(){
    alert('Sorry an error occured while loading notice');
    console.log('AJAZ call not successfull');
  }
});