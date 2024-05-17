//Kosta Novokmet
//dinamicki updatuje html kod ubacujuci aktivnosti i salje backend-u info da treba da menja broj slobodnih mesta kad se klikne
//komuncira sa bazom, postavlja button listenere na + i -, salje get i put ajax zahteve ka api-ju
function fetch_activities(curr_id,id) {
	var acts;
	$.get('api/get_activities_org?id='+id, function(response) {
		console.log(response);
		acts = response['active_activities'];
		let str1 = '';
		let index = 0;
		for (let act of acts) {
			index++;
			str1 +=
				`<div clqss="aktivnost">
				<div class="row align-items-center">
				<div class="col-sm-8">
				<h2 class="mr-3 mb-0">${act.naziv}</h2>
				<a style="color:#00A2C7" href="#" data-toggle="modal" data-target="#exampleModal${index}">Opis aktivnosti</a>
				<div class="modal fade" id="exampleModal${index}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel${index}" aria-hidden="true">
				<div class="modal-dialog modal-lg" role="document">
				<div class="modal-content">
				<div class="modal-header">
				<h5 class="modal-title" id="exampleModalLabel${index}">${act.naziv} </h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close">
				<span aria-hidden="true">&times;</span>
				</button>
				</div>
				<div class="modal-body">
				<div class="row" style="margin-top: 10px;">
				<div class="col-sm-6 d-flex justify-content-center"><i class="bi bi-pin-map"></i>&nbsp;&nbsp;${act.drzava}</div>
				<div class="col-sm-6 d-flex justify-content-center"><i class="bi bi-calendar4-week"></i>&nbsp;&nbsp;${act.datumStart}</div>
				</div>
				<div class="row" style="margin-top: 15px;">
				<div class="col-sm-12 text-justify">${act.opis}</div>
				</div>
				<div class="row d-flex align-items-center" style="margin-top: 10px;">
				<div class="col-sm-6">
				<div>Kategorija: ${act.oblasti}</div>
				<div>
				Potrebne veštine:
				<ul style="padding-left: 25px; ">
				<li type="square">${act.zahtevi}</li>
				</ul>
				</div>
				</div>
				<div class="col-sm-6">
				<div>Poslednji dan za prijavu: ${act.datumRok}</div>
				<div>Broj slobodnih mesta: ${act.brmesta}</div>
				</div>
				</div>
				</div>
				</div>
				</div>
				</div>
				</div>
				<div class="col-sm-4">
				<div class="d-flex justify-content-end align-items-center" style="margin-bottom: 5px;">
				<div class="mr-2">Broj preostalih mesta: <span id="peopleCount${index}">${act.brmesta}</span></div>`

			if(curr_id == id)
				str1+=
			`<div class="plus-minus">
				<button id="inc${index}" class="btn btn-primary btn-sm"">+</button>
				<button id="dec${index}" class="btn btn-primary btn-sm"">-</button>
				</div>
				</div>
				<div class="prijave d-flex justify-content-end">
				<a href="#">
				<button type="button" class="btn btn-primary btn-block btn-sm float-right">Pristigle prijave</button>
				</a>
				</div>
				</div>
				</div>
				</div>`;
			else str+=`
				<div class="prijave d-flex justify-content-end">
				<a href="activity_form.html">
				<button type="button" class="btn btn-primary btn-block btn-sm float-right">Prijavi se</button>
				</a>
				</div>
				</div>
				</div>
				</div>
				`
		}
		acts = response['archived_activities'];
		let str2 = '';
		for(let act of acts){
			index++;
			let reviews = act.reviews;
			let cntP = 0;
			let cntN = 0;
			for(let rev of reviews){
				if (rev.preporukavol == 'P') cntP++;
				else cntN++;

			}
			str2 += `
				<div class="aktivnost">
				<div class="row align-items-center">
				<div class="col-sm-8">
				<div class="d-flex align-items-center">
				<h2 class="mr-3 mb-0">${act.naziv}</h2>
				<div class="mr-3"><i class="bi bi-hand-thumbs-up-fill"></i>&nbsp;${cntP}</div>
				<div class="mr-3"><i class="bi bi-hand-thumbs-down-fill"></i>&nbsp;${cntN}</div>
				<button onclick="toggleRevs()" type="button" class="recenzije btn btn-secondary btn-sm">Recenzije <i class="bi bi-chevron-down" ></i></button>
				</div>
				<a style="color:#00A2C7" href="#" data-toggle="modal" data-target="#exampleModal${index}">Opis aktivnosti</a>
				<div class="modal fade" id="exampleModal${index}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel${index}" aria-hidden="true">
				<div class="modal-dialog modal-lg" role="document">
				<div class="modal-content">
				<div class="modal-header">
				<h5 class="modal-title" id="exampleModalLabel${index}">${act.naziv}</h5>
				<button type="button" class="close" data-dismiss="modal" aria-label="Close">
				<span aria-hidden="true">&times;</span>
				</button>
				</div>
				<div class="modal-body">
				<div class="row" style="margin-top: 10px;">
				<div class="col-sm-6 d-flex justify-content-center"><i class="bi bi-pin-map"></i>&nbsp;&nbsp;${act.drzava}</div>
				<div class="col-sm-6 d-flex justify-content-center"><i class="bi bi-calendar4-week"></i>&nbsp;&nbsp;${act.datumStart}</div>
				</div>
				<div class="row" style="margin-top: 15px;">
				<div class="col-sm-12 text-justify">${act.opis}</div>
				</div>
				<div class="row d-flex align-items-center" style="margin-top: 10px;">
				<div class="col-sm-6">
				<div>
				Kategorija: ${act.oblasti}
				</div>
				<div>
				Potrebne veštine:
				<ul style="padding-left: 25px; ">
				<li type="square">${act.zahtevi}</li>   
				</ul>
				</div>
				</div>
				<div class="col-sm-6">
				<div>Poslednji dan za prijavu: ${act.datumRok}</div>
				<div>Broj slobodnih mesta: ${act.brmesta}</div>
				</div>
				</div>
				</div>
				</div>
				</div>
				</div>
				</div>
				<div class="oceni-volontere col-sm-4">
				<a href="./org_review_volonteers.html">
				<button type="button" class="btn btn-primary btn-block btn-sm float-right">Ostavi recenzije volonterima</button>
				</a>
				</div>
				<div class="recenzije_sekcija container-fluid" style="margin-top: 15px;">
				`;
			for(let rev of reviews){
				if(rev.preporukavol == 'P')
					str2 += `
					<div class="dobar row review">
					<div class="col-sm-3 ">Ime Prezime:${rev.volname} ${rev.vollastname} </div>
					<div class="col-sm-9">Komentar:${rev.komvol}</div>
					</div>
					`
				else if(rev.preporukavol == 'N')
					str2 += `
					<div class="los row review">
					<div class="col-sm-3 ">Ime Prezime:${rev.volname} ${rev.vollastname} </div>
					<div class="col-sm-9">Komentar:${rev.komvol}</div>
					</div>
					`
			}
			str2 += `
				</div>
				</div></div>
				`
		}
		// Append str to a container or use it as needed
		$('#otvorene_akt').html(str1);
		$('#arhivirane_akt').html(str2);
		if(curr_id == id){
			var debouncer;
			acts = response['active_activities'];
			for(let i = 1; i <= acts.length;i++){
				$('#inc'+i).on('click',function(){
					clearTimeout(debouncer);
					debouncer = setTimeout(() => {
						$.ajax({
							url: 'http://localhost:8000/budivolonter/api/update_free_spaces',
							type: 'PUT',
							contentType: 'application/json',
							data: JSON.stringify({
								val: parseInt($('#peopleCount'+i).text()) + 1,
								idakt: acts[i-1]['id']
							}),
							success: function(response) {
								let n = $('#peopleCount'+i).text();
								n = parseInt(n);
								n++;
								$('#peopleCount' + i).text(n);
							},
							error: function(xhr, status, error) {
								console.error(xhr.responseText);
							}
						});
					}, 300);
				});

				$('#dec'+i).on('click',function(){
					clearTimeout(debouncer);
					debouncer = setTimeout(() => {
						$.ajax({
							url: 'http://localhost:8000/budivolonter/api/update_free_spaces',
							type: 'PUT',
							contentType: 'application/json',
							data: JSON.stringify({
								val: parseInt($('#peopleCount'+i).text()) - 1,
								idakt: acts[i-1]['id']
							}),
							success: function(response) {
								let n = $('#peopleCount'+i).text();
								n = parseInt(n);
								n--;
								$('#peopleCount' + i).text(n);
							},
							error: function(xhr, status, error) {
								console.error(xhr.responseText);
							}
						});
					}, 300);
				});
			}
		}
	});
}
function toggleRevs(){
	$('.review').toggle()
}
