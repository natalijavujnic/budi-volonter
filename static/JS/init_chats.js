var socket;
function start_websocket(){
	socket = new WebSocket(`ws://${window.location.host}/chat`);
	socket.onmessage = function(e){
		let data = JSON.parse(e.data);
		console.log(data);

	}
	$('#submit').on('click',function(){
		socket.send(JSON.stringify({
			'text':'hello world'
		}));
	});
}
function get_chats(){
	let str1 = ''
	$.get('api/get_chats',function(response){
		let chats = response['chats'];
		console.log(chats)
		for (let chat of chats){
			str1 += `
				<li class="list-group-item">
				<div class="d-flex">
				<div> ${chat['user']}</div>
				<div class="badge bg-danger ml-auto"> 3 </div>
				</div>
				</li>
			`

		}
		let messages = chats[0]['messages'];
		console.log(messages);
		$('#chats').html(str1);
	})
}
