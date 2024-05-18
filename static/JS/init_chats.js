var socket;
function start_websocket(){
	var user_id = parseInt(document.getElementById('body').getAttribute('user_id'));
	socket = new WebSocket(`ws://${window.location.host}/chat`);
	socket.onmessage = function(e){
		let data = JSON.parse(e.data);
		let type = data['type'];
		if (type == 'chat'){
			let msg = data['message'];
			$('#chat-box').prepend(`<div class="message">`+msg+`</div>`)
		} else {
			get_chats();
		}
		console.log(data);

	}
	var currentChat = null;
	let list = document.getElementById('chats');
	list.addEventListener('click', (e)=> {
		let chatid = parseInt(e.target.getAttribute('name'));
		let chatUserName = e.target.getAttribute('userChatName');
		$('#chatUserName').html(chatUserName);
		console.log(chatid);
		console.log(e.target.getAttribute('name'));
		console.log(e.target);
		if(currentChat != null){
			socket.send(JSON.stringify({
				'type':'close_chat'
            }));
		}
		currentChat = chatid;
		socket.send(JSON.stringify({
			'type':'open_chat',
			'chat_id': chatid
		}));
		$.get('api/get_messages?id='+chatid, function(response){
			let messages = response['messages'];
			var str = '';
			for (let message of messages){
				if(message['sender'] == user_id){
					str = `<div class="message">`+message['text']+`</div>` + str;
				} else {
					str = `<div class="message myMessage ml-auto">`+message['text']+`</div>` + str;
				}
			}
			$('#chat-box').html(str)
		})
	})

	let form = document.getElementById('chat-form');
	form.addEventListener('submit', (e)=> {
		e.preventDefault();
		let message = e.target.newmsg.value;
		$('#chat-box').prepend(`<div class="message myMessage ml-auto">`+message+`</div>`);
		socket.send(JSON.stringify({
			'type':'chat',
			'message':message
		}));
		form.reset();
	})
}
function get_chats(){
	let str1 = ''
	$.get('api/get_chats',function(response){
		let chats = response['chats'];
		console.log(chats)
		for (let chat of chats){
			str1 += `
				<li class="list-group-item d-flex" name="${chat['id']}" userChatName="${chat['user']}">
				<div name="${chat['id']}" userChatName="${chat['user']}"> ${chat['user']}</div>`;
				if(chat['messages_unread'] > 0){
				str1 += `<div name="${chat['id']}" userChatName="${chat['user']}" class="badge bg-danger ml-auto"> ${chat['messages_unread']} </div>`
				}
				str1 += `</li>`;
		}
		$('#chats').html(str1);
	})
}
