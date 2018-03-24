$(document).ready(function(){	
	$(".question-detail-div").mouseover(function(){
		console.log("in div 1 mouse in");
		$(this).removeClass("compact");
		$(this).addClass("expanded");
	});

	$(".question-detail-div").mouseout(function(){
		console.log("in div 2 mouse out");
		$(this).removeClass("expanded");
		$(this).addClass("compact");
	});
});