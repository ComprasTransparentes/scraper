function checkOverflow(el)
{
   var curOverflow = el.style.overflow;
   if ( !curOverflow || curOverflow === "visible" )
      el.style.overflow = "hidden";

   var isOverflowing = el.clientWidth < el.scrollWidth;

   el.style.overflow = curOverflow;

   console.log(isOverflowing);
   return isOverflowing;
};

$(document).ready(function() {
  
  // Select2

  	$(".standard").select2();

	$(".no-search").select2({
	  minimumResultsForSearch: Infinity
	}); 


	// Unable spinner on input[type="number"]

	// $(":input[type=number]").on('mousewheel', function(e){
	//     e.preventDefault();
	// });

	//checkOverflow($(".long-text"));

	var col = $(".long-text");
	for(var i=0; i<col.length; i++) {
		console.log(i);
		if(!checkOverflow(col[i])) {
			$(col[i]).siblings('.more-text').toggleClass('hidden');
		}
	}

	$('.more-text').click(function(){
		$(this).closest('.collapsable-text').toggleClass('kitten');
	});

	$('.ho-btn').click(function(){
		$('.ho').toggleClass('show');
		$('.lower-searchbar').toggleClass('hidden');
	})

	$('.bo-btn').click(function(){
		$(this).closest('.panel-footer').siblings('.bo').slideToggle();
	})

	$('#addrule').click(function(){
		$('.no-filters').toggleClass('hidden');
		$('.cosa-temporal').toggleClass('show');
	})

	$('.clickable-table tbody tr').click(function(){
		$(this).closest('tbody').find('tr').removeClass('active');
		$(this).toggleClass('active');
	})

});

$(document).ready(function(){
    $('#toTop').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });
});