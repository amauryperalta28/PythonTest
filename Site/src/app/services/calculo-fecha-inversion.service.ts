import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {map} from "rxjs/operators";
import {CalculoFechaRequest} from "../models/CalculoFechaRequest";
import {AuthService} from "./auth.service";

@Injectable({
  providedIn: 'root'
})
export class CalculoFechaInversionService {
  private calculoFechaInversionUrl = 'http://localhost:8000/fechas-inversion/';

  constructor(private http: HttpClient, private auth: AuthService) {
  }

  calcularFechaInversion(request: CalculoFechaRequest): Observable<void> {
    const headers = new HttpHeaders({
      'producto': request.producto.toString(),
      'plazo': request.plazo.toString(),
      'fechaCreacion': request.fechaCreacion,
       'enReinversion': request.enReinversion.toString(),
      //'authorization': `Bearer ${this.auth.getToken()}`
    });

    return this.http
      .get<any>(this.calculoFechaInversionUrl, {headers})
      .pipe(
        map((response) => {
          console.log({response})
        })
      );
  }

}
