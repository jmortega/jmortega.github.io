
	/*
		CSS3 Polaroid Slideshow
		-----------------------
		Author:			samhs
	*/
	
	
	var zindex = 50;
	
	$(document).ready(function(){
		// Create your interaction code here
		$("#pinboard ul li").each(function(){
			xpos = Math.floor(Math.random()*920);
			ypos = Math.floor(Math.random()*420);
			rotation = Math.floor(Math.random()*15);
			if(Math.floor(Math.random()*11)>5) {
				rotation = rotation * -1;
			}
			$(this).data("rotation",rotation);
			$(this).delay(1000).animate({top:ypos,left:xpos}).css({webkitTransform:"rotate("+rotation+"deg)",MozTransform:"rotate("+rotation+"deg)",msTransform:"rotate("+rotation+"deg)",transform:"rotate("+rotation+"deg)"});
		}).draggable({
			start: function(){
				zindex = zindex + 1;
				$(this).css({zIndex:zindex});					
			},
			stop: function(){
				rotation = Math.floor(Math.random()*15);
				if(Math.floor(Math.random()*11)>5) {
					rotation = rotation * -1;
				}
				$(this).data("rotation",rotation);
				$(this).css({webkitTransform:"rotate("+rotation+"deg)",MozTransform:"rotate("+rotation+"deg)",msTransform:"rotate("+rotation+"deg)",transform:"rotate("+rotation+"deg)"});
			}
		});
		

		
	});