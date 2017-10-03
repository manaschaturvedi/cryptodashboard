$( document ).ready(function()
{
	$(".add-new-coin-button").on("click", function()
	{
		console.log('clickkc');
		$("#new-coin-modal").modal("show");
	});

	display_coin_table();

	function display_coin_table()
	{
		var base_url = document.location.origin;
		$.get(base_url+"/get-coin-table", function( data ) 
		{
			console.log(data)
		  	$( "#coin-table" ).html(data);
		});
	}
});