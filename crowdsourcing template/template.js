require(['jquery-noconflict'], function(jQuery) {
  
  //Ensure MooTools is where it must be
  Window.implement('$', function(el, nc){
    return document.id(el, nc, this.document);
  });
  
  var $ = window.jQuery;
  var sentence = $('.people').html();
  $('.people').html("");
  
  jQuery.fn.reverse = [].reverse;
 
  $('.cml_field.checkbox input').on('change', function() {
    var that = this;
    
    // highlight option if selected
    $(this).closest('.cml_row').css("background-color", function() {
      return that.checked ? "#99FF99" : "";
    });    
  });
  
    // sort the inserts reversed, otherwise adding text will screw up the index positions.
  function sort_by_column(a,b) {
    return ((a[0] > b[0]) ? -1 : ((a[0] < b[0]) ? 1 : 0));
  }
  
  
  $('.cml_field.checkbox .cml_row label').hover(function() {
    // highlight words in the sentence when mouse over an option
    console.log($(this).html());
    console.log($($(this).html()).filter(".relations").val());
    var events = $($(this).html()).filter(".relations").val().split("--");
    if (events.length == 1) {
      events = $($(this).html()).filter(".relations").val().split("-r-");
    }
    var event1 = events[0].split("_");
    var event2 = events[1].split("_");
    
  
  // Preprocess
  // load and parse the clusters

  var eventList = [];
  eventList.push([parseInt(event1[1]),'<span id="' + event1[0] + '" class="term selected" range="' + event1[1] + '-' + event1[2] + '" >']);
  eventList.push([parseInt(event1[2]),'</span>']);
  eventList.push([parseInt(event2[1]),'<span id="' + event2[0] + '" class="term selected" range="' + event2[1] + '-' + event2[2] + '" >']);
  eventList.push([parseInt(event2[2]),'</span>']);
 
  eventList.sort(sort_by_column);
 
  $(".alignment #people").html(sentence);
 
  $(".alignment #people").html(function(i, val) {
    var output = val;
    for(i = 0; i < eventList.length; i++) {
      output = [output.slice(0, eventList[i][0]), eventList[i][1], output.slice(eventList[i][0])].join('');
    }
    return output;
  }); 
 
  });

});