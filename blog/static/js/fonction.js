/**
 * Created by bprime on 7/27/17.
 */

var room = 1;
function education_fields() {

    room++;
    var objTo = document.getElementById('education_fields')
    var divtest = document.createElement("div");
    divtest.setAttribute("class", "form-group removeclass"+room);
    var rdiv = 'removeclass'+room;
    divtest.innerHTML = '<div class="col-sm-3 nopadding"><div class="form-group"> <input type="text" class="form-control" id="Amount" name="Amount[]" value="" placeholder="Amount"></div></div>' +
        '<div class="col-sm-3 nopadding"><div class="form-group"> <input type="text" class="form-control" id="Item" name="Item[]" value="" placeholder="Item"></div></div>' +
        '<div class="col-sm-3 nopadding"><div class="form-group"> <input type="text" class="form-control" id="Type" name="Type[]" value="" placeholder="Type"></div></div>' +
        '<div class="col-sm-3 nopadding"><div class="form-group"><div class="input-group"> <input type="text" class="form-control" id="IBU" name="IBU[]" value="" placeholder="% / IBU"><div class="input-group-btn"> <button class="btn btn-danger" type="button" onclick="remove_education_fields('+ room +');"> <span class="glyphicon glyphicon-minus" aria-hidden="true"></span> </button></div></div></div></div><div class="clear"></div>';

    objTo.appendChild(divtest)
}
function remove_education_fields(rid) {
    $('.removeclass'+rid).remove();
}

function mash_step() {

    room++;
    var objTo = document.getElementById('mash_step')
    var divtest = document.createElement("div");
    divtest.setAttribute("class", "form-group removeclass"+room);
    var rdiv = 'removeclass'+room;
    divtest.innerHTML = '<div class="col-sm-3 nopadding"><div class="form-group"> <input type="text" class="form-control" id="Step_time" name="Step_time[]" value="" placeholder="80 min"></div></div>' +
        '<div class="col-sm-3 nopadding"><div class="form-group"> <input type="text" class="form-control" id="Step_name" name="Step_name[]" value="" placeholder="Name"></div></div>' +
        '<div class="col-sm-3 nopadding"><div class="form-group"> <input type="text" class="form-control" id="Description" name="Description[]" value="" placeholder="Description"></div></div>' +
        '<div class="col-sm-3 nopadding"><div class="form-group"><div class="input-group"> <input type="text" class="form-control" id="Step_temp" name="Step_temp[]" value="" placeholder="72.0 C"><div class="input-group-btn"> <button class="btn btn-danger" type="button" onclick="remove_mash_step('+ room +');"> <span class="glyphicon glyphicon-minus" aria-hidden="true"></span> </button></div></div></div></div><div class="clear"></div>';

    objTo.appendChild(divtest)
}
function remove_mash_step(rid) {
    $('.removeclass'+rid).remove();
}

function brixToSg(densB){

    if (densB=='' || isNaN(densB)) {
        alert("Veuillez remplir les champs avec des valeurs numeriques coherentes !");
    }
    else {
        // conversion en densite specifique
        //B = 1.000019 + (0.003865613*densB + 0.00001296425*densB*densB + 0.00000005701128*densB*densB*densB);
        B= (densB / (258.6 - ((densB / 258.2) * 227.1)))+1;
        B2 = B * 1000;
        document.forms['densite_brix'].densS.value = Math.round(B2);
        // conversion en Plato
        P = densB / 1.04;
        document.forms['densite_brix'].densP.value = P.toFixed(2);

    }
}

function brixToSgFerm(densBO,densBC){

    if (densBO=='' || densBC=='' || isNaN(densBO) || isNaN(densBC)) {
        alert("Veuillez remplir les champs avec des valeurs numeriques coherentes !");
    }
    else {
        // conversion en densite specifique
        B= 1.001843-0.002318474*densBO-0.000007775*densBO*densBO-0.000000034*densBO*densBO*densBO+0.00574*densBC+0.00003344*densBC*densBC+0.000000086*(densBC*densBC*densBC);
        B2 = B * 1000;
        document.forms['densite_brix_ferm'].densS.value = Math.round(B2);
    }
}

function calcalc(og, fg, sucre) {

    if (og=='' || fg=='' || sucre=='' || og < fg || isNaN(og) || isNaN(fg) || isNaN(sucre)) {
        alert("Veuillez remplir les champs avec des valeurs numeriques coherentes !");
    }
    else {

        // pour remplir le champ dens avec l'alcool avant refermentation
        dens1 = (og - fg) * 1.05;
        dens1 = (((dens1 / fg) * 100) / 0.795);
        document.forms['calculalc'].dens.value = dens1.toFixed(2);

        // pour remplir le champ referm avec l'alcool apporté par la refermentation
        referm1 = (((sucre * 0.5) / 0.795) /10);
        // document.forms['calculalc'].referm.value = referm1.toFixed(2);

        // pour remplir le champ ref_tot avec l'alcool total dans la bière
        ref_tot1 = dens1 + referm1;
        document.forms['calculalc'].ref_tot.value = ref_tot1.toFixed(2);

        // pour remplir le champ attenuation apparente
        attenuation = (((og - fg) / 1000) / ((og/1000) -1)) * 100;
        // document.forms['calculalc'].attenuation.value = attenuation.toFixed(2);

    }
}