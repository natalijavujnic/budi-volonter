function fetch_activities() {
	var acts;
	$.get('http://localhost:8000/budivolonter/api/get_activities_vol', function(response) {
		console.log(response);
		acts = response['archived_activities'];
		let str = '';
		let index = 0;
		for (let act of acts) {
			let rev = act['review'];
			var p_str = 
				`<div class="dobar row">
				<div class="col-sm-1 d-flex justify-content-center align-items-center"><i class="bi bi-hand-thumbs-up-fill"></i></div>
				<div class="col-sm-11">${rev.komorg}</div>
				</div>
				</div>`
			var n_str = `

				<div class="los row">
				<div class="col-sm-1 d-flex justify-content-center align-items-center"><i class="bi bi-hand-thumbs-down-fill"></i></div>
				<div class="col-sm-11">${rev.komorg}</div>
				</div>
				`
			index++;
			str = `
				<div class="aktivnost">
				<div class="row align-items-center">
				<div class="col-sm-12">
				<h2 class="mr-3 mb-0">${act.naziv}</h2>
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
				</div>
				<div class="col-sm-4">
				</div>
				</div>
				<div class="recenzije_sekcija container-fluid" style="margin-top: 15px;">`
			if(rev.preporukaorg == 'P') str += p_str;
			else if(rev.preporukaorg == 'N') str += n_str;

		}
		$('#sve_aktivnosti').html(str);
	});
}
