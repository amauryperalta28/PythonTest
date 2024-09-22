import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from "@angular/common/http";
import {Observable} from "rxjs";
import {map} from "rxjs/operators";
import {CalculoFechaRequest} from "../models/CalculoFechaRequest";
import {AuthService} from "./auth.service";
import {CalculoFechaResponse} from "../models/CalculoFechaResponse";

@Injectable({
  providedIn: 'root'
})
export class CalculoFechaInversionService {
  private calculoFechaInversionUrl = 'http://localhost:8000/fechas-inversion/';

  constructor(private http: HttpClient, private auth: AuthService) {
  }

  calcularFechaInversion(request: CalculoFechaRequest): Observable<CalculoFechaResponse> {
    const headers = new HttpHeaders({

      'authorization': `Bearer ${this.auth.getToken()}`
    });

    let queryParams = new HttpParams();
    queryParams = queryParams.append("producto", request.producto.toString())
    queryParams = queryParams.append("plazo", request.plazo.toString())
    queryParams = queryParams.append("fechaCreacion", request.fechaCreacion.toString())
    queryParams = queryParams.append("enReinversion", request.enReinversion.toString())


    return this.http
      .get<any>(this.calculoFechaInversionUrl, {params: queryParams})
      .pipe(
        map((response) => {
          console.log({response})
          return response
        })
      );
  }

}
