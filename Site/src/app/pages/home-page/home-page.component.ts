import { Component, OnInit } from '@angular/core';
import {CalculoFechaInversionService} from "../../services/calculo-fecha-inversion.service";
import {CalculoFechaRequest} from "../../models/CalculoFechaRequest";

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent{
  productos = ['1', '2', '3']; // Productos simulados
  selectedProducto = '2';
  enReinversion = false;
  plazo = 33;
  fechaCreacion = "";

  constructor(private calculo: CalculoFechaInversionService) {
  }

  onSubmit() {
    const request: CalculoFechaRequest = {
      producto: this.selectedProducto,
      enReinversion: this.enReinversion.toString(),
      plazo: this.plazo,
      fechaCreacion: this.fechaCreacion
    }
    // console.log({
    //   producto: this.selectedProducto,
    //   enReinversion: this.enReinversion,
    //   plazo: this.plazo,
    //   fechaCreacion: this.fechaCreacion,
    // });

    this.calculo.calcularFechaInversion(request).subscribe((result)=>{
       console.log({result});
    })
  }


   formatDateToYYYYMMDD(date: Date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');  // Months are 0-indexed in JavaScript
    const day = String(date.getDate()).padStart(2, '0');  // Ensure two digits

    return `${year}-${month}-${day}`;
  }

}


