
var li_items = document.querySelectorAll(".sidebar ul li");
var hamburger = document.querySelector(".hamburger");
var wrapper = document.querySelector(".wrapper");
li_items.forEach((li_item)=>{
	li_item.addEventListener("mouseenter", ()=>{
       li_item.closest(".wrapper").classList.remove("hover_collapse");
     
	})
})
li_items.forEach((li_item)=>{
	li_item.addEventListener("mouseleave", ()=>{
	li_item.closest(".wrapper").classList.add("hover_collapse");

	})
})


document.addEventListener('DOMContentLoaded', function() {
	var datetimeContainer = document.getElementById('datetime')
		setInterval(updateDateTime, 1000);
		function updateDateTime() {
		  var date = new Date();
		  var options = {
			year: 'numeric',
			month: 'long',
			day: 'numeric',
			hour: 'numeric',
			minute: 'numeric',
			second:'numeric'
		  };
		  var formattedDateTime = date.toLocaleString(undefined, options);
		  datetimeContainer.textContent = formattedDateTime;
		}
	  });