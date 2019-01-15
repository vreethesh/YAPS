function openTab(cityName, elmnt) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = $('.tabcontent');
    tabcontent.each(function() {
      $(this).css('display', 'none');
    })
  
    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].style.backgroundColor = "";
    }
  
    // Show the specific tab content
    $('#'+cityName).css('display', 'block');
    // Add the specific color to the button used to open the tab conten
    elmnt.style.backgroundColor = getComputedStyle(document.getElementById(cityName)).backgroundColor;
  }
  
  // Get the element with id="defaultOpen" and click on it
  //document.getElementsByClassName("defaultOpen")[0].click();
  
  String.prototype.replaceAt=function(index, replacement) {
    return this.substr(0, index) + replacement+ this.substr(index + replacement.length);
}

  $('#newGuest').click(function(e) {
    e.preventDefault()
    var gs = $('#guests')
    var g = $('.guest').last()
    var gr = g.clone()
    var nP = $('#nPas')
    nP.val((Number(nP.val()) + 1))
    gr.find('#usr').val("")
    gS = g.find('#usr').attr('name')
    gS = gS.substr(0, gS.length - 1) + (Number(gS.charAt(gS.length - 1)) + 1)
    console.log(gS)
    gr.find('#usr').attr('name', gS)

    gr.appendTo(gs)
  });

  $(document).ready(function() {
    $(".submitBtn1").click(function(e) {
      $(this).addClass("loading");
      setTimeout(function() {
        $(".submitBtn1").addClass("hide-loading");
        // For failed icon just replace ".done" with ".failed"
        $(".done").addClass("finish");
        $('#passng').submit()
      }, 3000);
      setTimeout(function() {
        $(".submitBtn1").removeClass("loading");
        $(".submitBtn1").removeClass("hide-loading");
        $(".done").removeClass("finish");
        $(".failed").removeClass("finish");
      }, 5000);
    })
    
    $(".submitBtn2").click(function(e) {
      $(this).addClass("loading");
      setTimeout(function() {
        $(".submitBtn2").addClass("hide-loading");
        // For failed icon just replace ".done" with ".failed"
        $(".done").addClass("finish");
        $('#car').submit()
      }, 3000);
      setTimeout(function() {
        $(".submitBtn2").removeClass("loading");
        $(".submitBtn2").removeClass("hide-loading");
        $(".done").removeClass("finish");
        $(".failed").removeClass("finish");
      }, 5000);
    })
  });