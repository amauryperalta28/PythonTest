import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.scss']
})
export class HomePageComponent{
  productos = ['Producto 1', 'Producto 2', 'Producto 3']; // Productos simulados
  selectedProducto = '';
  enReinversion = false;
  plazo = 0;
  fechaCreacion = new Date();

  onSubmit() {
    console.log({
      producto: this.selectedProducto,
      enReinversion: this.enReinversion,
      plazo: this.plazo,
      fechaCreacion: this.fechaCreacion,
    });
  }

}
