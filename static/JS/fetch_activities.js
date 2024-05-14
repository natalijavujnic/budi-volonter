function fetch_activities() {
	$.get('http://localhost:8000/budivolonter/api/get_activities', function(response) {
		console.log(response);
		acts = response['active_activities'];
		let str1 = '';
		let index = 0;
		for (let act of acts) {
			index++;
			str1 +=
				`<div class="aktivnost">
				<div class="row align-items-center">
				<div class="col-sm-8">
				<h2 class="mr-3 mb-0">${act.naziv}</h2>
				<a style="color:#00A2C7" href="#" data-toggle="modal" data-target="#exampleModal${index}">Opis aktivnosti</a>
				<div class="modal fade" id="exampleModal${index}" tabindex="-1" role="dialog" aria-labelledby="exampleModal${index}" aria-hidden="true">
				<div class="modal-dialog modal-lg" role="document">
				<div class="modal-content">
				<div class="modal-header">
				<h5 class="modal-title">${act.naziv}</h5>
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
				<div class="mr-2">Broj preostalih mesta: <span id="peopleCount">${act.brmesta}</span></div>
				<div class="plus-minus">
				<button class="btn btn-primary btn-sm" onclick="increaseCount()">+</button>
				<button class="btn btn-primary btn-sm" onclick="decreaseCount()">-</button>
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
		}
		acts = response['archived_activities'];
		let str2 = '';
		index = 0;
		for(let act of acts){
			str2 += `
				<div class="aktivnost">
				<div class="row align-items-center">
				<div class="col-sm-8">
				<div class="d-flex align-items-center">
				<h2 class="mr-3 mb-0">${act.naziv}</h2>
				<div class="mr-3"><i class="bi bi-hand-thumbs-up-fill"></i>&nbsp;12</div>
				<div class="mr-3"><i class="bi bi-hand-thumbs-down-fill"></i>&nbsp;4</div>
				<button type="button" class="recenzije btn btn-secondary btn-sm">Recenzije <i class="bi bi-chevron-down"></i></button>
				</div>
				<a style="color:#00A2C7" href="#" data-toggle="modal" data-target="#example5Modal">Opis aktivnosti</a>
				<div class="modal fade" id="example5Modal" tabindex="-1" role="dialog" aria-labelledby="example5ModalLabel" aria-hidden="true">
				<div class="modal-dialog modal-lg" role="document">
				<div class="modal-content">
				<div class="modal-header">
				<h5 class="modal-title" id="example5ModalLabel">${act.naziv}</h5>
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
			let reviews = act.recenzije;
			let n = 2;
			for(let i = 0;i < n;i++){
				str2 += `
					<div class="dobar row">
					<div class="col-sm-3 ">Ime Prezime: </div>
					<div class="col-sm-9">Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis voluptas officiis error. Veniam, eligendi delectus deserunt tempora modi doloremque similique.</div>
					</div>
					`
			}
			str2 += `
				</div>
				</div>
				`
		}
		// Append str to a container or use it as needed
		$('#otvorene_akt').html(str1);
		$('#arhivirane_akt').html(str2);
	});
}
