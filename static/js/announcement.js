$.ajax({
  url: '/get_announcements',
  success: function(data){
    if(data.success == true){
      for(x in data.notice)
      {
         document.getElementById("announcement_marquee").innerHTML+= '<div class=row><div class="col-sm-12" >'+'<a href="'+data.notice[x].url+'">'+data.notice[x].title+'</a></div></div></br>';
      }
    }else{
      document.getElementById("announcement_marquee").innerHTML+= '<div class=row><div class="col-sm-12" >No Updates</div></div></br>';
    }
  },
  error: function(){
    alert('Sorry an error occured while loading notice');
    console.log('AJAX call not successfull');
  }
});